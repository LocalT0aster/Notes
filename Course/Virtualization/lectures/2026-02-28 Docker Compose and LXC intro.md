---
title: "Feb 28 - Docker Compose and LXC intro"
date: 2026-02-28
topics:
  - "Docker cleanup"
  - "Docker Compose"
  - "container networking"
  - "LXC intro"
tags:
  - virtualization
  - containers
  - docker-compose
  - lxc
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Feb 28 - Docker Compose and LXC intro

## Docker cleanup and Compose

```bash
sudo docker ps
```

to see what we have running now

```bash
sudo -i
```

```bash
docker stop $(docker ps -q)
```

ctr c ls

see containers

ctr t ls

I see I have a nginx1 running

ctr t kill nginx1

ctr t delete nginx1

ctr c delete nginx1

we have everything cleaned up

```c
podman pull registry.astralinux.ru/library/astra/ubi18-nginx1263:1.8.4-mg16.0.0
if you haven't pulled that, please do
podman run --rm registry.astralinux.ru/library/astra/ubi18-nginx1263:1.8.4-mg16.0.0
```

run a container

open a new tab in terminal

```bash
ip a
```

we see bridge podman0 and veth0

right now we see absolutely same way of making network as Docker

in earlier versions podman was creating and assigning IP address to each veth, why? because there was no podman0 bridge. as a result there was a lot of items in routing table (each veth is a separate route)

why this could be not very comfortable? ease of debugging. all you need to monitor container network is a bridge. you run tcpdump of a bridge and voila - you can see all the traffic.

```bash
sudo lsns
```

nothing new here, once again, all 6 namespaces, no user namespace

Problem 1: In a real life almost everywhere you have to manage multiple containers

for example, the most basic web application setup is a database + application itself

Problem 2: In a real life it is not very comfortable to run Docker containers by commands. Why?

Because there will be a lot of options, like:

- ports forwarded
- volumes (directories, Docker volumes)
- rm, readyonly root fs, etc.

At the end of the day you will have a giant command, usually wrapped up to a shell script. In most cases you do not have any standard of running containers.

And this is where Docker Compose comes in.

Why do we need it?

1. Standard way to run one or more containers in a declarative way
2. It has a file with all the options written down
3. Docker offers a way to isolate a networking for a container or multiple containers, but it requires manual set up. Docker Compose manages it automatically - it creates a separate network for your project.

In the beginning of the Docker Compose it was a separate tool, separate binary, called **docker-compose**

As it's popularity rose, it became a part of a Docker. But as a plugin, so it's not available everywhere without additional packages. And as soon as docker-compose is just a binary (Go), some users would like to have it not a part of Docker installation, but bring it manually.

In most cases you have a time lag between release of new version of Docker Compose and it's inclusion to major distributions, even if you have a very quick release cycle, like Arch or Alpine.

```bash
apt show docker-compose
```

Version: 1.29.2-3+b2

```bash
apt show docker-compose-v2
```

Version: 25.0.5.astra3+ci18+b2

```bash
sudo apt install docker-compose-v2
```

install it

we can easily see what files were brought to our system

dpkg -L docker-compose-v2

Now you have to ways to run it:

```bash
docker-compose (as a standalone Go binary, ready to go)
docker compose (as a part of Docker)
```

In a lot of guides you have references to docker-compose standalone, and that's for good. Because compose as a plugin was a different version for a some time.

Docker Compose has a declarative way of running containers. You must describe what you want, not the steps to achieve that. It uses YAML syntax file, and default filename is docker-compose.yaml (or .yml, whatever)

```bash
cd
```

go to the home directory

```bash
mkdir webapp
```

create a directory webapp

we would like to run two containers:

- PostgreSQL database engine
- adminer - small web application to manage database engine (create database, table, etc)

adminer = 5.4.2-standalone

postgres = 18.3-alpine3.22

create a new file in Kate and put this code there

```yaml
services:
  adminer:
    image: adminer:5.4.2-standalone
    ports:
      - "8080:8080"
  postgres:
    image: postgres:18.3-alpine3.22
    environment:
      POSTGRES_PASSWORD: password
```

we have to save the file to our webapp directory and name it docker-compose.yml

in a real world you use a specific directory for docker-compose.yml file and all the related data

move back to terminal and change directory to webapp

```bash
cd webapp
docker-compose -> talking to Docker with our username (using our credentials)
newgrp docker
docker compose up
```

we have docker-compose running containers in our TTY

open a new tab in browser and have it in localhost:8080

Select PostgresSQL as an engine

Server: postgres

Username: postgres

Password: password

Logged in.

What configuration was created when we started docker-compose.yml?

new tab

```bash
ip a
```

let's see interfaces

we see a new bridge, it's called br-XXXXXXXXXX

we see two veth-adapters, they are connected to the bridge

```bash
sudo docker network ls
```

we can see docker networks, and new network created, called webapp_default

6abdeaf10cdd   webapp_default   bridge    local

when you just run a container using docker run command, without any network specification, it uses default network

```c
if you create a new network, and specify it's name when running a container, it will go to this network
```

from the OS perspective you just specify the bridge to put a veth in.

but default network in Docker has no DNS support.

we've used "postgres" as an address for server to connect to and inside container it was resolved to IP-address

```bash
sudo docker compose exec adminer sh
```

run a command inside a container

```bash
ping postgres
```

you can see it's resolved to 172.18.0.2

how does it work?

/etc/resolv.conf has a special address nameserver 127.0.0.11

go back to tab with docker compose running

Ctrl+C

now the containers are stopped, but they are not deleted yet

```bash
docker compose ps
```

empty, no containers running right now

```bash
docker compose ps -a
```

same way the docker command has it

```bash
docker compose up
```

means create containers, and then run it

```bash
docker compose up -d
```

let's run containers in background, detached from our teminal

```bash
docker compose ps
docker compose down
```

removes everything, leaving to traces

right now we have our database destroyed completely. why? becase /var/lib/postgres directory was inside a container, and it was destroyed. in most cases you would like it to be more persistent (I would like to save a database), how can we do that?

usually we have two options:

you can use a volume option to bind directory from the host to the container

Docker Volume, which is a still directory bound from host, but located in a cryptic docker /var/lib directory

I would like to use a persistent storage for my database.

```yaml
volumes:
```

postgres:

then edit postgres service definition like that:

```bash
  postgres:
```

```yaml
    image: postgres:18.3-alpine3.22
    volumes:
    - postgres:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: password
```

And now I have it as Docker Volume.

Don't forget to save the file!

```bash
docker compose up -d
```

? Network webapp_default       Created

? Volume "webapp_postgres"     Created

? Container webapp-postgres-1  Started

? Container webapp-adminer-1   Started

Effectively it has created all the things I've asked for.

```bash
docker volume ls
```

show us a webapp_postgres volume

we did selected a wrong place to put a volume in, okay

but now container is already created

never ever edit a compose file, when you have it running

```bash
docker compose down
```

this command will not remove the volume!

```c
if we would like to destroy a volume too, add -v
```

Volume will be destroyed, never use Docker Volume for a production, use a bind directory instead

edit docker-compose to

- postgres:/var/lib/postgresql

save it, and run it

When you use Docker Volume, you just put your file to /var/lib/docker/volumes/... somewhere

Never ever use Docker Volume for a production data, only for testing, development and etc

For a production grade system, use a bind directory

```bash
docker compose down -v
```

stop it

change the volume to:

- ./data:/var/lib/postgresql

and remove volumes section completely, we don't need it anymore

```bash
user@user30-generic1:~/webapp$ ls -al data/18
drwxr-xr-x  3 root root 4096 ??? 28 18:21 .
drwxr-xr-x  3 root root 4096 ??? 28 18:21 ..
drwx------ 19   70 root 4096 ??? 28 18:21 docker
```

we have a docker directory, owned by uid = 70, but we don't have it on the host

our container with postgres is starting as root, but then uses setuid call to become uid = 70

this is a common practice

so we have a directory, but we can't manage it

to create a directory with other uid and own it - you have to be root

this could be different with other containers - elasticsearch runs as it's user with uid = 1000

```bash
docker compose down
```

data directory could be anywhere, just use a full path to point at it

in most cases I do recommend put docker-compose.yml to

/opt/<name of the project/docker-compose.yml

In some cases you would like to have one database for all the applications:

1. You create docker-compose.yml for a database service and run it with host network

It will open the port on the host, and usually it is 0.0.0.0 - listen to all interfaces

2. You can create separate docker-compose for your application, but to point to database you use default router address.

We've talked about databases today, and the most important part of databases are the backups

When running a database inside a container, you should think about backing up on the host, not inside container

If you have a database inside a container, you have two ways:

1. If your application could have a downtime (at night, for example):

you do docker-compose stop (it just stops the containers)

snapshot of the LVM for a database

```bash
docker-compose start
```

2. If your application could not be stopped, then use a pg_dump (or something like this) to have a .sql file dumped from the database. The downside of this method is speed of the backup - it could take ages with a big database.

Sometimes you need to restart a container (you've deployed a new certificate and you would like web server to pick it up)

```bash
docker compose restart
```

it will restart all the containers

```bash
docker compose restart adminer
```

**Homework (if you'd like to practice):**

Try to create a two-networks docker-compose

Or try to create a multiple networks in Docker without docker-compose

## LXC

As I've told you, LXC was created long before Docker.

First release in 2008. Canonical (creators of the Ubuntu distribution) were looking for a project to be a frontman of the distribution.

LXC is just a set of binaries, which allow you to run containers.

When Docker released and it was loud and astonishing, Canonical did a re-architecture of LXC project, making it Docker-like.

New project name was LXD.

LXC: no daemon running, you just run container with a command, that's it

Docker: has daemon, you communicate with a daemon with a client, run containers.

LXD: has daemon, same way, but the client you communicate with it is called **lxc**

LXC and LXD are still projects in development, LXC has a low momentum right now, because there is nothing to develop any more. LXD has more momentum right now, it is not so popular as LXC or Docker.

What is the main difference:

LXC/LXD is all about running a full fledged OS inside a container.

OS:

1. It's own systemd/or whatever
2. cron (run scheduled tasks)
3. it's own logging (syslog-ng, rsyslog, whatever)
4. (optional) you can have a dbus running inside a container

LXC is a perfect tool to run an OS, and then burn it.

LXC desing goals were simple: do not create an instrument, if we have one.

Docker: assigns IP-addresses to containers

LXC: uses a DHCP-server, which is configured and running on a host

Docker: uses aufs (prevously), overlays (now)

LXC: use a simple directory on a host, but also supports things like LVM, ZFS, etc.

LXC was created for system administrators, Docker was created for developers
