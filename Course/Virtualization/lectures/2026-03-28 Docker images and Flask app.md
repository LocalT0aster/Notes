---
title: "Mar 28 - Docker images and Flask app"
date: 2026-03-28
topics:
  - "container image lifecycle"
  - "Dockerfile basics"
  - "static site image"
  - "Flask image"
tags:
  - virtualization
  - containers
  - docker
  - dockerfile
  - flask
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Mar 28 - Docker images and Flask app

## Container image recap

Quick recap so far:

1. Docker - to run one process in a controlled environment
2. LXC/LXD/Incus - to run a full operating system (it has some init daemon)

As a result we do have different approaches to configuration:

1. Docker container may not have a SSH service
2. LXC container would have a SSH
1. Docker - you must build a container and leave only config files for some changes (in most cases configuration files are bind from the host)
2. LXC - you can run a clean image of the operating system, and then you can configure it any way you would like to, but in most cases this is some IaC approach

In most cases you run docker container with readonly filesystem, because it helps to keep container secure.

This leads us to a problem - Docker has a more complicated approach, because in most cases Dockerfile is created by developer.

We will install VSCodium, telemetry free version of VSCode.

In Astra 1.8 you can install latest version of VSCodium, when talking about 1.7 - there are some difficulties, version 1.85 works

now we should create a filesystem structure, useful for building Docker containers

create **docker** directory inside of your home

we should add this directory (not open, but add) to VSCodium

File - Add Folder to Workspace

right click docker directory and create directory inside called nettools

right click nettools directory and create a new file, called Dockerfile

this is the content of the Dockerfile

```dockerfile
FROM ubuntu:24.04

RUN apt update

RUN apt install -qy traceroute iproute2 iputils-ping
```

don't forget to save the file

now I would like to build my container image, so I need a Terminal to give a command

Ctrl+J opens and hides Terminal

we are now ready to build a container

```bash
docker build .
```

please note the dot at the end - dot means "current directory"

you should be in nettools directory to build a container

we see this warning, and it's important

DEPRECATED: The legacy builder is deprecated and will be removed in a future release.

Install the buildx component to build images with BuildKit:

https://docs.docker.com/go/buildx/

we are using legacy builder right now, it works, but it has some strings attached

```bash
docker image ls
```

we've built a container, but it has no name right now. we can always add name later

copy image ID, and use this command:

```bash
docker tag 91a554cf2539 nettools:1.0
docker image ls
```

to see it's tagged successfully

you can use any name you would like to, but if you are going to publish your container to Docker Hub, you should use naming convention:

`<org>`/`<name>`:`<version>`

why we've used ubuntu container without organization?

Official images from docker team do not have an `<org>` part

If you have a custom container storage, like self-hosted GitLab, you should give a full name with url

registry.domain.tld -> the address of the GitLab

registry.domain.tld/`<project group>`/`<project>`

this name tells Docker to publish your container to your GitLab installation

in most cases you combine the building process and tagging

```bash
docker build -t nettools:1.0 .
```

this command builds and tags the result

run it again, you see it runs instantly. why? cache works.

sometime cache is not what you need, so

```bash
docker build --no-cache -t nettools:1.0 .
```

the problem with cache is - it's just a text based cache

```dockerfile
RUN apt updated will be cached and as soon as it is text-based, it knows nothing about the updates on the other side (version of the packages in apt repo can change)
FROM means starting point for a container
```

each RUN instruction is a layer

right now the build process is simple: run a command, if it returns non-zero exit code, the build stops

when we are talking about Astra Linux you can use repository URL to stabilize the version of the Astra you are using

I would like to add a curl package, so I change the line 5 to

```dockerfile
RUN apt install -qy traceroute iproute2 iputils-ping curl
docker build -t nettools:1.1 -t nettools:latest .
```

we tag one image with multiple names

```bash
docker image ls
REPOSITORY    TAG                 IMAGE ID       CREATED          SIZE
nettools      1.1                 2ecc88dd5489   45 seconds ago   152MB
nettools      latest              2ecc88dd5489   45 seconds ago   152MB
nettools      1.0                 91a554cf2539   33 minutes ago   144MB
```

right now I use 152+144Mb

best way is not to replace a big layer completely, but add to it

layers of the container are downloaded in parralel, so use it to you power

one big layer = bad

multiple layers, created to use cache effectively = good

we have a special command to inspect layers in a container

```bash
docker image inspect <name or ID>
docker image inspect ubuntu:24.04
```

always use inspect on base images (on those you mention in FROM instruction)

let's see another (not very good) example of layers

```dockerfile
FROM debian:12
RUN wget https://...
RUN tar xzvf ...
RUN rm ...
```

don't ever do that!

the problem is - last command makes no sense here, because .tar.gz file is already stored twice in layers, done before

how to deal with that? you can use --squash key of docker build and this will merge all three layers, removing the wasted space. you can't analyze the steps later and one layer means downloaded in one thread.

the best way - combine commands to make it one layer

```dockerfile
FROM debian:12
RUN wget ... && tar xzvf ... && rm ...
```

this is an optimized way to do that

to make it more readable you can use backslash

```dockerfile
FROM debian:12
RUN wget ... && \
tar xzvf ... && \
rm ...
```

this is the modern way of doing it

&& makes the simple thing - do next command only of previous was a success

## Let's create a next container image

create a **static** directory inside **docker**

inside **static** directory create another directory called **site**

inside of the **site** directory create a new file **index.html**

put this as a content of a file

```bash
<h1>Hello, world!</h1>
```

before ever building my container image I can check with an already available image of nginx whether it works or not

I should run a nginx container and bind my directory inside it

```bash
docker run --rm -v $(pwd)/site:/usr/share/nginx/html -p 8080:80 nginx:1.29.5-alpine3.23
```

before I run it, I should open terminal on my static directory

right click static directory, Open in Intergrated Terminal

run the command

as soon as directory is bound, not copied, you can change it and just refresh the page to see the result

I use subshell $(pwd) which is replaced by the directory of the site when command is run

I would like to add a picture with a kitten to my site

right click **site**, add **img** directory

edit index.html, and add two more lines

```bash
<img style="width: 300px" src="img/kitten.jpeg" />
<a href="contact.html">Contact me</a>
```

create a contact.html file

```bash
<a href="mailto:mail@example.com">Drop me a line</a>
```

right click static directory, create a new file called Dockerfile

don't forget to stop our running container with nginx

the content of Dockerfile will be:

```dockerfile
FROM nginx:1.29.5-alpine3.23

COPY site/* /usr/share/nginx/html/
```

just two lines, remember to save the file

let's build and tag the container image

```bash
docker build -t static:1.0 .
docker run --rm -p 8080:80 static:1.0
```

the pic is broken

let's drop a shell inside and take a look

```bash
docker ps
```

to get the ID of the running container, because we didn't provide a name

```bash
docker exec -ti 81086b971bdc sh
```

most safe shell is usually sh, bash is not always available even if container has a shell

```bash
ls -l /usr/share/nginx/html
```

I can't see img directory, why?

the problem of an asterisk is the way it is processed

it will be expanded, then executed

```dockerfile
COPY site/index.html site/contact.html site/img/kitten.jpeg /usr/share/nginx/html
```

it will copy all the files without any subdirectory

```dockerfile
COPY site /usr/share/nginx/html/
```

this is the command we would like to see

stop the container

rebuild

run once again

We have created a simple container with just a static directory with files. Let's build something more complicated, like Flask web application in Python

Python web application

docker/pytime

create app directory inside docker/pytime

inside app directory create one more directory called pytime

create a file

app/pytime/__init__.py

```c
import os
import json
import datetime
import socket
import string
import random
from pathlib import Path

from flask import Flask
from flask import request
from flask import jsonify

def create_app():
  app = Flask(__name__)

  @app.route("/")
  def root():
    now = str(datetime.datetime.now())
    hostname = socket.gethostname()
    return("Datetime now is {0} from {1}".format(now, hostname))

  @app.route("/api/", methods=["GET", "POST"])
  def api():
    x = datetime.datetime.now()
    return jsonify(year=x.year, month=x.month, day=x.day)

  @app.route("/status/")
  def status():
    return jsonify({ "status": "ok" })

  return app
```

I will not use other modules here, but the structure I've created allow it

I would create app/modules/`<module>` directories for my code to use

app/requirements.txt

Flask==3.1.3

please note, I use the exact version

create Dockerfile in top level directory

```dockerfile
FROM debian:12-slim

RUN apt update && \
    apt install -qy --no-install-recommends \
    python3 python3-pip && \
    rm -rf /var/cache/apt/archives/*

ADD ./app/requirements.txt /requirements.txt
RUN pip3 install --break-system-packages -r /requirements.txt

COPY ./app /app/

EXPOSE 80

WORKDIR /app

ENTRYPOINT ["flask", "--app=pytime", "run", "--host=0.0.0.0", "--port=80"]
```

Open a terminal in my pytime directory and run

```bash
docker build -t pytime:1.0 .
```

Let's try to run it

```bash
docker run --rm -p 8080:80 pytime:1.0
```

It runs, it works, but what if it's not?

I do have an ENTRYPOINT defined, so what if I replace ENTRYPOINT from flask to sh?

```bash
docker run --rm -p 8080:80 -ti --entrypoint /bin/sh pytime:1.0
```

overriding the entrypoint

```c
cd /app
flask --app=pytime run --host=0.0.0.0 --port=80
if a container has an editor inside, you can even change files or add some parameters
```

you can add --debug to run Flask web application with a debugger

Problems:

1. we run web application as root (bad for security)
2. we did not fixed the version of the Debian (only the major one), and we did not fixed the version of the software - I do rely on my base image to have a suitable Python version
3. using Debian as base image is not very good idea - usually Debian has a quite old versions of the software

when using FROM and some base image, you must have a good understanding of a lifecycle of a software inside your base image

## Homework

1. Try to find the safer way to run a Flask web application
2. Take a look at the other Dockerfiles
