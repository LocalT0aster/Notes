---
title: "Apr 4 - Dockerfile, users, compose, postgres"
date: 2026-04-04
topics:
  - "base images"
  - "non-root container users"
  - "Docker builders"
  - "ENTRYPOINT vs CMD"
  - "Compose"
  - "PostgreSQL"
tags:
  - virtualization
  - containers
  - docker
  - docker-compose
  - postgres
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Apr 4 - Dockerfile, users, compose, postgres

Let's solve the problems

## FROM container

Right now we use Debian as FROM image. It has some advantages (a lot of examples how to build and run), but actually too uncomfortable for real production.

As soon as we have a python web-application, there are special versions of containers with better security approach.

Use official image, decide the version of Python

What version to use?

3-alpine - means "take any most recent stable version of Python 3 and any most recent stable version of Alpine"

I would recommend to fix up the version of Python and version of Alpine. Why? It helps with debugging problems.

python:3.14.3-alpine3.23

We should change the first line of the Dockerfile to

```dockerfile
FROM python:3.14.3-alpine3.23
```

and delete RUN command with all the installation details

```bash
docker build . -t pytime:1.0-alpine
REPOSITORY    TAG                 IMAGE ID       CREATED          SIZE
pytime        1.0-alpine          405e52ecaac2   16 seconds ago   62MB
pytime        1.0                 9451368ad9ca   6 days ago       170MB
```

this is a common situation, I mean in most cases alpine images are smaller and you can build them faster

the image we've built is smaller, and more secure

we've also fixed the versions of the software used - Python version right now is fixed and is not dependant on the version of the OS

## Run my web application as a user

first - let's do it

1. we have to create a user - this is not a straitforward thing as you may think, because it depends on the OS used

```bash
ARG USER=pytime
ARG ID=2000
```

```dockerfile
RUN addgroup -g ${ID} ${USER} && \
    adduser -D -H -G ${USER} -u ${ID} -h /nonexistent -s /sbin/nologin ${USER}
```

usually it's done like that.

and before WORKDIR

```dockerfile
USER ${USER}
```

we use ARG here to have a variable, which exists only at a build time

and second - this variable (ARG) could be overriden at build time

```bash
docker build . -t pytime:1.1
```

you should always remember, that adding user to the system - just a line in two files:

/etc/passwd

/etc/group

/etc/shadow

we can see the difference

```bash
docker run --rm --entrypoint sh -ti --user root pytime:1.1
```

you can see, we run it as a user root

```bash
grep pytime /etc/passwd
grep pytime /etc/group
grep pytime /etc/shadow
```

you can use this trick to create user same way in any Linux based OS - by just adding lines to these files

here is the moment, when "scratch" images goes away - it has no ability to create a user.

```c
if we would like to check our application, we can run it
docker run --rm pytime:1.1
```

the problem is - in most Linux OS you do have ports under 1024 marked as privileged

only root user can open them (CAP_NET_BIND_SERVICE)

now we are user pytime with no additional permissions, so we can't open port 80

usually we have two ways to solve that

- we can change port of the application to 8080 (usual port to run something as non root user)
- we can override the setting of the OS to allow anyone to open any port (I do remember this was as a default in Ubuntu)

we will change port number to 8080

```dockerfile
ENTRYPOINT ["flask", "--app=pytime", "run", "--host=0.0.0.0", "--port=8080"]
```

now we've done everything to make our contrainer run as an unprivileged user

We can see some container running as root: mysql, postgres, etc

Why do the do that? The reason is simple - data directory preparation and log files

Log files is not the big deal for Docker (strategy is simple - just log to standard ouput and hope for the best)

Data files are still the problem

All these applications have an internal user change mechanism, which is simply the setuid call, but done later by the application itself.

How we can move an image from machine to machine without any registry?

```bash
docker save / docker load
docker save pytime:1.1 > pytime.tar
```

this is to save the image to the file with all the layers required

```bash
docker image rm pytime:1.1
```

Untagged: pytime:1.1

Deleted: sha256:32e249b35ff29b6006ba4b0edfb355fdfc4b1fcda4a7ee332d36dc6e42cfd730

```bash
docker load < pytime.tar
```

load the image from the file

## Builder and legacy builder

when talking about the Docker build process, it was always a mess

most of the commands were created and didn't change a lot

the was strictly no definition to Dockerfile syntax version

the problem is - Dockerfile is a unified way to dictribute information about building process

Dockerfile has no information about minimum version of Docker used

the architecture was solid and there was no ability to decouple build process from the Docker

BuildKit is a modern way to build Docker containers, but it has to be installed

usually you can use BuildKit and don't see any big difference on a simple Dockerfiles

BuildKit has to be installed, usually it's packed as docker-buildx package (in Debian/Ubuntu/Astra)

```bash
sudo apt install docker-buildx
```

after we have installed it, it is used automatically

when you run docker build now - it just uses new builder available and builds container with it

the heart of the new building process is a LLB format

this is like compiled code - you can't read it, but it allows the separation of the concept

```bash
docker build -> LLB -> BuildKit
```

as soon as you have frontend and backend now, backend (BuildKit) doesn't care who has produced the LLB

you can make your own frontend, which will support your own syntax of Dockerfile

it allows you to make a simplified version of Dockerfile, tailored to your team or standard

In classic Docker builder you must use FROM and RUN to install packages

In modern concept, you make custom syntax, where user can just name the list of packages

Frontend will generate all the commands to install packages

Right now, some new features of Docker require you to use a specific syntax

Our current Dockerfile copies the requirements.txt twice

```dockerfile
RUN --mount=type=bind,source=app/requirements.txt,target=/tmp/requirements.txt \
    pip3 install --break-system-packages -r /tmp/requirements.txt
```

now we can remove the ADD command completely

but we still don't have any version reference, it works out of the box because BuildKit right now understands, what we want

```dockerfile
# syntax=docker/dockerfile:1.2
```

and change COPY command to

```dockerfile
COPY ./app/pytime /app/pytime
```

fix EXPOSE

```dockerfile
EXPOSE 8080
```

now our Dockerfile is not compatible with old builder

how can we summon the old builder?

we can control the version of the builder with a environment variable

```bash
DOCKER_BUILDKIT=0 docker build .
```

it will fail to process our Dockerfile

## ENTRYPOINT vs CMD

best way to memorize that is this one

```dockerfile
ENTRYPOINT + CMD - what will be run in a container (any component could be empty, but not both of them)
```

let's see how we run flask

we use ENTRYPOINT, so it gives us an interesting ability

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

COMMAND here means CMD

```c
docker run --rm pytime:1.1 --debug
--debug is a command line, which will be converted to CMD and transferred to the container
if you define ENTRYPOINT in your Dockerfile, you mean
```

my command to run an application is perfect, I think you should only add parameters to it

in enterprise, you may run Java code to do some things. usually Java code is run like

java `<a lot of options here>` -jar `<file>`

you have a base container with java installed and it has ENTRYPOINT

```dockerfile
ENTRYPOINT: java <a lot of options here> -jar
```

all you have to do is to provide the path to the .jar file to run it

```dockerfile
FROM <base>
```

...

```dockerfile
CMD myfile.jar
```

your code will be run with all the options from `<base>` container, which is good

Even if container has an ENTRYPOINT, it could be easily overriden by the --entrypoint parameter to docker run

```bash
docker run --rm -ti --entrypoint sh pytime:1.1
```

I can still override the CMD part of this, but I don't need it right now

entrypoint is a standard way to define a starting point and good way to have it changed, when you need it

When you use most of the OS images in Docker, they do not define the ENTRYPOINT (you will override it later)

But what they do define - they define CMD (in most cases - it is a shell binary)

```bash
docker run --rm -ti ubuntu:24.04
```

container image has CMD defined as /bin/bash

## More advanced container usage

in most of the cases you use Docker, you have to "dockerize" the application. for example, you may have a PHP project, which doesn't use docker right now, but you want it to use it

in most cases the configuration of the running software is done using the configuration files, and you should have good understanding, how to manage it and how to use it

```bash
docker run --rm -ti nginx:1.29.5-alpine3.23 /bin/sh
```

/etc/nginx directory has two interesting parts:

first, you have conf.d directory - we can add our configuration files to this directory

second, we can see nginx.conf file with basic configuration

as soon as we have a symlink inside /etc/nginx directory, we can't override the whole directory

I would like to have both config parts overriden by me: nginx.conf and conf.d directory

I would like to also keep the original config, so I can use it as a starting point

open the second tab

```bash
docker ps
```

to see the list of containers and copy the ID

```bash
docker cp 1d34cb7146cf:/etc/nginx/nginx.conf .
```

remember to replace ID by your own

```bash
docker cp 1d34cb7146cf:/etc/nginx/conf.d .
```

also copy conf.d directory

create a new directory called nginx and move both file and directory there

how to use that?

Options are:

1. Copy these files and directory at the build time (this is not the best option)
2. Bind these directories from the host into container

Second option is popular, because you can combine the best of two worlds: you run a container, which is pretty standartized, but you can drop the files inside of the container (bind)

As a result you can just "docker run", becase the command itself becomes too long and unusable. This is where docker compose comes in

create a file named docker-compose.yml

```yaml
services:
  static:
    image: static:2.0-compose
    build: .
    restart: unless-stopped
    volumes:
    - ./nginx/conf.d:/etc/nginx/conf.d:ro
    - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    ports:
    - 8080:80
```

edit nginx.conf and change to

worker_processes 8;

now I can change any configuration of nginx and run it

now let's play with the volumes and env variables

## Postgres

we would like to have a setup, suitable for a development and production separation

I would like to have a postgres running, and sometimes I may need the adminer to control it (create users or databases)

```yaml
services:
  postgres:
    image: postgres:18.3-alpine3.23
    restart: unless-stopped
    volumes:
    - postgres:/var/lib/postgresql
    environment:
      POSTGRES_PASSWORD: password
  adminer:
    image: adminer:5.4.2-standalone
    ports:
      - "8080:8080"

volumes:
  postgres:
```

simple and clean compose file

```bash
docker compose up
docker compose down
```

volumes are not deleted

```bash
docker compose down -v
```

this will also delete the volumes

## Homework

How can I use one docker-compose.yml for a production and development

Production = store data for postgres not in the volume
