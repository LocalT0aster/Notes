---
title: "Feb 21 - Docker ports, processes, and images"
date: 2026-02-21
topics:
  - "Docker port forwarding"
  - "docker-proxy"
  - "GUI applications in containers"
  - "Docker image import"
  - "Podman"
tags:
  - virtualization
  - containers
  - docker
  - podman
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Feb 21 - Docker ports, processes, and images

## Docker port forwarding

```bash
docker run --rm -p 8080:80 nginx:1.29.5-alpine3.23
```

run container with port forwarding

```bash
ss -tanp
```

I won't see the process, who has opened the port

```bash
sudo ss -tanp
```

I'll see all the processes

users:(("docker-proxy",pid=755975,fd=4))

this is the one, who has opened port 8080

docker-proxy is clutch, which allow Docker to behave the same way on Linux, Windows, macOS

it's performance is terrible, never ever use it in production!

to disable this bad performance disable the usage of docker-proxy at all

```json
"userland-proxy": false
```

just to notice: Docker still is not very good at supporting nftables, they have plans to complete full support of nftables to July 2026

Run graphical applications inside Docker container

We have usually two ways to run any graphical app in Docker

* forward the X-socket to container to allow it to use it (host and container are the same)
* forward X-socket using SSH, but you need to run SSH server inside a container

The ultimate goal of container usage in Docker is to run **one process** and do it right

This makes easy way to understand the status of the container

We can run multiple services inside one container, but it makes it's state tricky

If we run ServiceA and ServiceB, and ServiceA has crashed. What is the state of the container?

Here we can understand the limitation of Docker - run one process is a model, which won't give us the ability to run a full fledged OS.

```bash
df -h
```

we have enough of free space, let's move on

```bash
sudo mkdir /var/tmp/dockerastra
```

create a directory for rootfs of my container

```bash
sudo ./makeastra /var/tmp/dockerastra
```

If I would like just to run some software, this rootfs is absolutely correct. This image won't be runnable in LXC, for example, because it lacks some Astra-specific components.

```bash
sudo chroot /var/tmp/dockerastra
```

But if you would like to install these components to run it as a complete operating system in LXC, you have to install these

```bash
apt install -qy parsec parsec-tests linux-astra-modules-common astra-safepolicy ca-certificates
rm -rf /var/cache/apt/archives/*.deb
```

delete some cached .deb files to make image smaller

```bash
echo "ru_RU.UTF-8 UTF-8" >> /etc/locale.gen
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
```

let's add two locales, russian and english one

```bash
locale-gen
```

build locales from the source accourding to /etc/locale.gen file

```bash
update-locale ru_RU.UTF-8
```

make russian locale as a default one

```bash
exit
exit the chroot
nano dockerimport
#!/bin/bash

tar -C $1 -cpf - . | \
docker import - $2 \
    --change "ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
    --change 'CMD ["/bin/bash"]' \
    --change "ENV LANG=ru_RU.UTF-8"
```

Ctrl+S, Ctrl+X

```bash
chmod +x dockerimport
sudo ./dockerimport /var/tmp/dockerastra astra:1.8.4.48
```

I've created the basic container and tagged it with the exact version

```bash
sudo docker image list
user@user30-generic1:~$ sudo docker image list
REPOSITORY    TAG                 IMAGE ID       CREATED              SIZE
astra         1.8.4.48            267d6d707947   About a minute ago   416MB
```

My task is quite simple: I would like to run Firefox inside

I can do this two ways:

1. (quick and dirty) Run a container, jump inside, do apt install, get away
2. (good one) Make a Dockerfile, explaining what we would like to do with a container (using our astra:1.8.4.48 as FROM)

```bash
cd
mkdir firefox
```

```dockerfile
FROM astra:1.8.4.48

RUN apt update && apt install -qy firefox openssh-server

RUN adduser --disabled-password --gecos "" test && echo test:test | chpasswd

COPY start.sh /

ENTRYPOINT ["/start.sh"]
```

let's save the content of this file to firefox directory and name the file **Dockerfile**

create a new file in Kate

```bash
#!/bin/bash

sed -i /pam_parsec/d /etc/pam.d/sshd && mkdir /run/sshd && exec /usr/sbin/sshd -D
```

we have to replace some text in PAM-module of sshd, because we would like to run an SSH-daemon without some security components of the Astra

save the file as start.sh to firefox directory

```bash
chmod +x firefox/start.sh
```

make start.sh executable

```bash
cd firefox
sudo docker build . -t astra:firefox
docker run --name firefox -d -p 2022:22 --rm astra:firefox
```

run it with port forwarded to port 2022 of out host machine

```bash
ssh -X -l test 127.0.0.1 -p 2022 firefox
```

yes

test

```bash
docker stop firefox
```

also please note, docker container runs each time clean.

```bash
docker run --name firefox -d -p 2022:22 --rm astra:firefox
```

pstree

shows us the parent process of a container - we have sshd in a container, so we see containerd-shim as a parent of our sshd process

Docker uses containerd to run containers

At some version Kubernetes moved to direct support of containerd instead of Docker.

Was: Kubelet (agent on the host) -> Docker -> containerd -> container running

Now: Kubelet -> containerd -> container running

Just a side note: Docker is still required to build a container, and Docker is super friendly for anyone trying to begin a container journey.

**containerd**

this is a service, it runs along dockerd and runs container

```bash
sudo systemctl status containerd
```

this is a one-binary thing - service is being written in Go, so you need nothing but the binary

Configuration file

/etc/containerd/config.toml

It has a service

/lib/systemd/system/containerd.service

Binary

/usr/bin/containerd

containerd-shim-runc-v2

this is the only binary left (because we have runc of v2.x)

containerd-shim-runc-v1

this was legacy binary to support old runc, but it is removed now

/usr/bin/ctr

binary to control and to communicate with containerd

/run/containerd/containerd.sock

it has a socket for a communication using it's binary

only root user can communicate

ctr

sudo ctr i ls

list container images, don't have any

sudo ctr c ls

don't see any running containers

but there are! docker ps shows me at least two of them running

containerd has a thing called namespaces, it can separate multiple clients using containerd to run something

sudo ctr ns ls

we can see namespace called moby, this is docker

sudo ctr -n moby c ls

now I see them running

```bash
ps auxf
```

it will give me the chain of processes

/usr/bin/containerd-shim-runc-v2 -namespace moby -id b4fcdc9b69811a8ac5000234cb491ad8ce21fd45aa50a98828fdfad62811816a -address /run/containerd/containerd.sock

\_ nginx: master process nginx -g daemon off;

\_ nginx: worker process

## Task

run a container with a containerd without any help from Docker

First of all we need to pull an image

If we use Docker Oficial Image, it has a name like nginx:TAG

```bash
docker pull nginx:TAG
```

but it won't work with containerd

In Docker I can also pull images from other hubs/registries

```bash
docker pull gcr.io/test/nginx:1.27-alpine
```

sudo ctr i pull docker.io/library/nginx:1.29.5-alpine3.23

for official images I have to prepend "library", for all others there will be name prefix

sudo ctr i pull docker.io/library/hello-world:latest

also pull hello-world container

sudo ctr run docker.io/library/hello-world:latest hello1

run a container using containerd

it looks like a Docker, nothing fancy

sudo ctr c ls

list containers

sudo ctr c rm hello1

remove stopped container

sudo ctr run --help

a lot of thing we can use to run containers

run = create + start

we can have it completely separated way: create, then run, when ready

sudo ctr c create docker.io/library/nginx:1.29.5-alpine3.23 nginx1

we will create nginx1 container from image nginx:1.29.5-alpine3.23

sudo ctr c ls

will show nginx1 ready to go

containerd has a specific name for a running process from a container - it's called a task

sudo ctr task ls

no tasks here still

sudo ctr task start --detach nginx1

we would like to run it detached from our terminal

the task = what was defined by ENTRYPOINT or CMD for a container entry point

```bash
ps auxf | less
```

/usr/bin/containerd-shim-runc-v2 -namespace default -id nginx1 -address /run/containerd/containerd.sock

this is the command line of a process from containerd

/usr/bin/containerd-shim-runc-v2 -namespace moby -id b4fcdc9b69811a8ac5000234cb491ad8ce21fd45aa50a98828fdfad62811816a -address /run/containerd/containerd.sock

this is the command line from Docker - containerd has an option to join any existing namespace when starting container. Docker prepares all the things we ask for (creates network, creates network namespace, creates veth adapters, put it to the according namespace, run a container and join it to the namespace)

Also Docker uses it's own way to store images (overlayfs), so it prepares mount namespace and mount all the layers it would like to.

How can we see difference between two running containers?

```bash
docker inspect
docker inspect d3237f5ae3e6
```

it will give me a long JSON list of all the options of the container

sudo ctr c info nginx1

container information, once again, JSON, could be parsed or processed with other tools

containerd gives me nothing about network connection, because it doesn't manage it

network namespace was created for my nginx1 task, but can I take a look at it?

```bash
sudo nsenter -t <pid> --net bash
```

I switch network namespace, not the mount or pid, or uts

```bash
ip a
```

I can see lo interface, but no veth

1. Docker prepares all the layers and gets a complete directory with a filesystem of a future container
2. Docker creates network namespace and veth adapters, put one veth to the bridge, second is still here
3. Network namespace created, veth adapter moved to it

We can configure veth adapter, and then move it to the other namespace.

The container itself has the full control of the adapter - lately it can change IP address if likes to

4. Container is run with containerd, and docker specify network namespace it has created for a container to join

containerd is in use by all major players in containerization: Docker, Kubernetes, Nomad, they all use it

If we would like to use a host network namespace, we can run a container with --net-host (containerd option, not Docker)

Docker -> containerd -> runc

dpkg -L runc

runc --version

```bash
cd
mkdir testrunc
cd testrunc
```

runc spec

please, create a default configuration to run a container

it creates a config.json file, it has all the options about the container

"root": {

"path": "rootfs",

"readonly": true

```bash
},
```

this part of the config.json tells us where to store a rootfs

it doesn't work with symlinks, so don't try

when you copy a directory with a cp command, you write a resulting directory with your uid:gid

rootfs may have uids or gids linked to it's own files /etc/passwd

```bash
sudo cp -ar /var/tmp/dockerastra rootfs
```

copy full rootfs

sudo runc run astra1

run it!

we can switch to other tab, and run

```bash
sudo lsns
```

to see we are in different namespace

Right now we fully understand the way containers are run:

Docker -> containerd -> runc

Docker is still the only one, who can build containers

## Homework

take a good look as config.json - to understand what we can do with runc

**podman and RedHat**

```bash
podman is a RedHat project. NIH-syndrome. Because then RH spends time for a support of Docker on it's platform, it invests money to Docker, not to RH
```

Docker was never intented to have a paid support. podman as a part of RH ecosystem has a full paid support for anyone who would like to buy it.

you can't have this support in Russia right now, but for any internation businness it's a big deal

```bash
sudo apt install podman
```

we can install it

the main difference between podman and Docker is an architecture

Docker always has it's daemon running, it runs as root, and it allows us to create things, which require elevated privileges: like creating veth adapters or bridged, or whatever

**access to Docker socket = root rights**

one can always run a container, which will mount the rootfs of the host and have a root user

```bash
podman has no daemon running, if you run podman without sudo, it will happily do all the things without root access. but if you run it with sudo, it will do all the things docker do.
```

What RH states: it usually says, that you can substitute docker command with podman command and everything will be working

```bash
sudo podman image ls
```

have no images

```bash
sudo podman pull hello-world
sudo podman pull registry.astralinux.ru/library/astra/ubi18-nginx1263:1.8.4-mg16.0.0
```

try to pull nginx from astralinux registry

as soon as we run podman as root, it pulls images to /var/lib/container, not to home directory of the user
