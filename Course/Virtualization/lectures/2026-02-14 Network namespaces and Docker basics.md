---
title: "Feb 14 - Network namespaces and Docker basics"
date: 2026-02-14
topics:
  - "mount namespace recap"
  - "network namespaces"
  - "veth"
  - "Docker basics"
tags:
  - virtualization
  - containers
  - networking
  - docker
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Feb 14 - Network namespaces and Docker basics

## Mount namespace recap

Short summary of mount namespace

```bash
sudo unshare -m bash
mount --bind astra1 astra1
pivot_root . old_root
umount -l /old_root
```

Any container will do this when starting, but not the container, it will be done by a containerization suite you use.

Docker uses overlayfs, well, it's a choice, sometimes it is useful (containers can share same layers), sometimes it is not, but each containerization suite has it's own way to do it.

LXC has a number of options to offer when talking about filesystem. You can use just a directory as a root filesystem, but more comfortable it is when you use LVM (LVM partition could be a root fs).

Once more, to remember, that if you run a container with it's own filesystem, you still have all the mounts the host had.

```bash
sudo unshare -m --propagation=slave bash
```

This will propagade the changes in mounts on the host to the container.

## Network isolation

You will use ip command to manipulate all the network things. Please note, that ifconfig command is a deprecated stuff, don't use that.

To manage network interfaces we need CAP_NET_ADMIN privilege in Linux, so the easiest way to have it is to be root.

```bash
sudo -i
```

```bash
ip netns
```

show me the list of the network namespaces already created

one network namespace (of the host system) was created when the system started up, but you won't see it with this command

when you will be creating any network namespace, you will have new files in /run/netns directory

```bash
ip netns add test
```

create a new network namespace called test

```bash
ip netns exec test /bin/bash
```

I ask ip to run bash in my newly created test namespace

```bash
ip a
```

let me see what we have here

1: lo: `<LOOPBACK>` mtu 65536 qdisc noop state DOWN group default qlen 1000

link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00

we see new namespace, it's completely empty

```bash
exit
ip a
```

what's the deal with this new namespace? it's empty! how can we use it?

magic: you can move any network interface between namespaces.

```c
if we move our enp2s0 interface to test namespace, we will lose a connectivity
```

we will use a specific network interface type called veth

veth interfaces are always created as a pair. we will create a pair. pair means data transfer point-to-point.

how can we create a veth pair? simple

```bash
ip link add host type veth peer name container
ip link add <veth1> type veth peer name <veth2>
ip a
ip link set container netns test
```

I move container interface (it's called container) to the container

```bash
ip a
```

no inteface container any more here

```bash
ip a add 192.168.1.11/24 dev host
```

please add an IP-address and network mask to my interface

```bash
ip l set dev host up
```

enable interface and that's it!

```bash
ip netns exec test /bin/bash
```

run a bash in the other network namespace

```bash
ip r
```

no luck here, no routing table exist

```bash
ip l set dev lo up
ip l set dev container up
```

put all the interfaces up

```bash
ip a add 192.168.1.12/24 dev container
```

please add an IP-address and network mask

```bash
ip r
```

finally, a routing table

```bash
ping 192.168.1.11
```

Left Ctrl+C to stop it

What we have just seen is a classic container networking stack.

LXC, Docker, Podman, they all can use veth (and they do like it)

The problem: to create a veth interface you need CAP_NET_ADMIN privilege. And looks like you have to be root to obtain it. If you would like to run a rootless container (unprivileged user would like to run a container)

slirp4netns - this is rootless network stack for a container (Podman uses it by default)

pasta - same thing, but newer

they all create tap interface and run a process to serve it's data

We have one more way to provide a networking for a container. We can just leave a container in host's network namespace.

When you are using veth, you have to do something with a networking - your host has to be a gateway for all the traffic of a container. You have to understand the configuration.

And also we can have one more way to provide a network communication for a container: we can just put the real interface to the container.

For a container it's network connectivity is out of it's line of sight, but you have to think about on the host's side.

Host have some ways to manage a lot of veth interfaces.

1. Put all veth to a bridge and group them as we want. Docker can do that. LXC does not.
2. We can leave them all as simple interfaces (some Kubernetes network providers like Calico does that)

What about traffic management? How can I do that?

As long as host is a gateway for a container, you have a full control of it's traffic. Why? Because you have a FORWARD chain.

The big difference between router and usual host: when usual host receives an IP-packet not addressed to it, it will discard the packet. When router gets an IP-packed not addressed to it, it tries to deliver it (using it's routing table)

INPUT chain gets packets addressed to local processes, runing on the host

FORWARD chain gets packets addressed to other hosts (mostly containers, running on the host)

Let's destroy all the things we've created.

```bash
exit
ip link del host
```

I delete a veth adapter (it also deletes the other side)

```bash
ip netns del test
```

delete a namespace

## Homework

please, do it once again.

## Docker

```bash
apt install docker.io
```

install Docker

```bash
docker ps
```

show me the list of running containers

Docker communicates with docker daemon using socket. Socket is a very specific beast in Linux, so let's discuss it a little bit.

Socket = pair IP-address+port

Imagine we have to communicate only within one computer (two processes). They can use this pair to communicate, but it's a little bit redundant. Because two processes will use some predefined IP-address.

Socket file = uses filename as identification (you can't have two files with the same name)

It uses standard kernel ACL (rwx) to handle permissions

srw-rw---- 1 root docker  0 ??? 14 17:42 docker.sock

Who can communicate with docker socket?

To talk to docker daemon as a regular user I have to be in a docker group

we have a user called "user" and right now it's not in the docker group, so let's fix that

```bash
adduser user docker
newgrp docker
```

add docker group (as long as we are a member of it)

```bash
docker ps
```

run it as user

right now our Docker installation will use Docker Hub to download container images. this is usually a good idea, but not in a broken world

```bash
sudo mkdir /etc/docker
sudo nano /etc/docker/daemon.json
{
```

"registry-mirrors": ["https://docker.rosatom.education"]

```bash
}
```

Ctrl+S, Ctrl+X

we kindly ask docker to use our caching server to download images.

```bash
sudo systemctl restart docker
```

restart docker daemon

I would like to run a docker image called hello-world

This is a special image, it does nothing, but showing us a welcome message

```bash
docker run hello-world
```

1. Now we have some version of a container image, called hello-world
2. We have a dead body of a container right now

It is not running any more, but the body is here

```bash
docker ps -a
```

I can see dead body

dead containers are useful for understanding, what went wrong (or right)

as long as you don't a centralized logging solution, it's best to keep a body of a container

```bash
docker image ls
```

REPOSITORY

this is the full name of the image (sometimes it can include the address of the registry you've downloaded it from)

TAG - another way to say "version"

when you issue a command like

```bash
docker run hello-world
```

you are not saying anything about the version (tag), "latest" will be used

using "latest" version is bad practice

latest is bad because of time:

one would like to use nginx:latest

and second one would like to use it nginx:latest, but 6 months later

Please: always be specific about the version!

```bash
docker pull nginx:1.29.5-alpine3.23
```

it's specific not only about the version of nginx, but also about the operating system underneath

```bash
docker run --rm nginx:1.29.5-alpine3.23
```

open a new tab

```bash
sudo lsns
```

let's see what we have

```text
4026532611 mnt         2 395659 root nginx: master process nginx
4026532612 uts         2 395659 root nginx: master process nginx
4026532613 ipc         2 395659 root nginx: master process nginx
4026532614 pid         2 395659 root nginx: master process nginx
4026532615 cgroup      2 395659 root nginx: master process nginx
4026532616 net         2 395659 root nginx: master process nginx
```
six namespaces created, but which namespace we would like to see and we don't?

we don't see time namespace (we don't need it), but we also don't see user namespace (which will make this all more secure, but it does not)

## Homework

try to make Docker use user namespace

I can see PID in lsns: in my case it's 395659

```bash
sudo nsenter --net -t 395659
```

welcome to nginx network namespace

```bash
ip a
```

> [!important] what did I change?

I didn't changed mount namespace - I still have rootfs of my Astra Linux

I have all the tools to debug!

I can change only the part of the namespaces to debug a container.

```bash
exit
```

how can I run a shell inside a container?

```bash
docker exec -ti <id or name> bash
```

what's the problem with it? who told you there is a bash inside?

```bash
docker exec means you would like to switch all the namespaces to a container (and filesystem too, because of mount namespace)
docker ps
```

to know id of a container

```bash
docker exec -ti c919c183bee9 /bin/sh
```

why sh? because there is no bash in container

so I switch all namespaces to container, and now I see it's filesystem, not filesystem of the host with all the shiny tools

```bash
exit
```

let's examine what we have of the host side, it will be funny

Linux is bad at explaining type of interface

```bash
ip a
5: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
9: vethd9af296@if8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default
ip -d link show vethd9af296
```

I can see veth line, so it is veth

bridge_slave state

it means it is in a bridge right now

```bash
docker uses docker0 bridge to combine all the veth interfaces
```

it uses it only if you don't create an isolated network for your container

how can I run a container without network isolation?

```bash
docker run --rm --net=host nginx:1.29.5-alpine3.23
# --net=host - it says "do not create a network namespace, run it with a host network namespace"
4026532681 mnt         2 396277 root nginx: master process nginx -g daemon off
4026532682 uts         2 396277 root nginx: master process nginx -g daemon off
4026532683 ipc         2 396277 root nginx: master process nginx -g daemon off
4026532684 pid         2 396277 root nginx: master process nginx -g daemon off
4026532685 cgroup      2 396277 root nginx: master process nginx -g daemon off
```

we see only 5 namespaces, and no network namespace for it
which ports I do have opened right now?
```bash
sudo ss -tanp
```

you know about port forwarding, don't you?

## Homework

run nginx with port forward, take a look at the opened ports, and tell me who will open the port? and why?