---
title: "Mar 14 - LXC snapshots and LVM"
date: 2026-03-14
topics:
  - "lxc-copy"
  - "LXC configuration"
  - "LVM snapshots"
  - "thin pools"
tags:
  - virtualization
  - containers
  - lxc
  - lvm
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Mar 14 - LXC snapshots and LVM

## Copying LXC containers and snapshots

If we would like to copy a container, all we have to do - copy it's root filesystem, but there is a little bit more.

We have to copy not only the root filesystem, but also we have a configuration of the container.

The easiest way - lxc-copy command, you don't have to know anything about storage details

But LVM is a quite an interesting tool and it allows us to do much more interesting things, so you have to know all the details.

To copy the lv you can do that in two steps:

1. you create a new lv
2. copy old lv byte for byte to a new lv

We didn't create the first lv, so how can we do that?

```bash
sudo lvcreate -n astra2 -L2G astra
```

Now I can copy the old volume to a new one

```bash
sudo dd if=/dev/astra/astra of=/dev/astra/astra2 bs=4M conv=fsync status=progress
```

Beware: you'd better stop container before attempting to make a copy

In most cases you can get a clean copy even of working container, but I'd recommend to stop it.

If you can't afford a long downtime, make a snapshot, run the container and copy the snapshot.

We have a copy of rootfs right now, but how to create a new container?

```bash
sudo -i
```

```bash
cd /var/lib/lxc
cp -ar astra astra2
```

a - leave all ownership info intact (don't change it)

r - recursive (even copy the directory)

```bash
lxc-ls -f
```

new container for LXC - just a directory with a config inside /var/lib/lxc

LXC allows a simple management with any tool like Ansible - create a directory, put a config, good to go

we've seen container creation using templates, and templates were using debootstrap command. why is it this way? because you don't have to maintain any other infrastructure for it. you already have a repo with packages for a linux distro.

debootstrap (or any other similar way) has a lot of flexibility - you can script up the creation of the image, and create it the way you would like to

debootstrap has two disadvantages:

1. it takes time
2. it's poorly understood by most of the developers

LXC team decided to move to images

they started to maintain the image directory for LXC to create containers faster and with less time to way

```bash
lxc-stop -n astra
lxc-destroy -n astra
```

beware! by default it will also destroy the lv

beware! lcx-destroy will fail if it could not delete the storage for the container

```bash
lxc-destroy -n astra2
```

an error!

we have two options here:

1. we just delete directory manually, as we've created it
2. we edit the config to point to a valid storage

```bash
nano astra2/config
lxc.rootfs.path = lvm:/dev/astra/astra2
```

Ctrl+S, Ctrl+X

```bash
lxc-destroy astra2
```

success

I would like to create a new container using images!

to create a container using images, you have to use a different template called download

```bash
exit
exit the root shell
sudo lxc-stop -k -n ubuntu1
sudo lxc-destroy -n ubuntu1
sudo lxc-create -t download -n ubuntu-noble --bdev lvm --vgname astra --fssize=2G  -- --dist ubuntu --release noble --arch amd64
```

noble = codename for 24.04

with docker, you always use Docker Hub by default! and what is the source of the download now?

The source is

https://images.linuxcontainers.org/

Container images do not have any predefined user account, as we've seen previously. Why? You can always have a root shell, why bother?

```bash
sudo lxc-start -n ubuntu-noble
sudo lxc-ls -f
```

you can see container running and available (IP address is here)

After 2014 almost all the development of LXC moved to images

No more templates

How can we use that?

1. Install the SSH Server
2. Create a user
3. Log in by SSH

```bash
sudo lxc-attach -n ubuntu-noble
apt update
```

remember about default Docker configuration of the FORWARD with DROP policy!

```bash
apt install openssh-server
adduser demo
```

use password demo

```bash
adduser demo sudo
```

add user demo to sudo group and enabling the use of sudo command

now I can test this user account for a SSH access

```bash
exit
```

get back to host

```bash
sudo lxc-ls -f
ssh -l demo 10.0.3.X
```

what we've done so far? we have created a small basic image to be a starting point

LXC gives us no way to use it like a Docker does

But we can do that with LVM!

What I want to do:

1. I would like to use my image as a reference for other containers I'd create
2. I would like to create more containers, and store only the difference from image, not the whole container again

We will be working with the thin pool LVM

Usually thin pool is a feature, which allows us to trick the system

thin provisioning means you can create lv of any size without enough storage to back it

```c
exit
exit
sudo lxc-stop -n ubuntu-noble
if we would like to use any lv as a reference point, we must ensure it is stabilized
```

readonly and cannot be opened

```bash
sudo lvchange -p r astra/ubuntu-noble
```

makes it readonly

```bash
sudo lvchange -a n astra/ubuntu-noble
```

makes it unaccessible

```bash
sudo lvs
```

we have to create a pool - special logical volume to store the changes

```bash
sudo lvcreate -L5G --thinpool test astra
```

we create a thin pool, it is called test and it's size is 5G

now we can create a snapshot, but not the usual one

thin snapshot holds only the difference from the origin

```bash
sudo lvcreate -s --thinpool astra/test astra/ubuntu-noble --name ubuntu-snap
```

-s - this is a snapshot

```bash
--thinpool - we select a thinpool to store differences
```

astra/ubuntu-noble - the origin

```bash
--name - the name of the snapshot
```

Now all I have to do is to create a new container and point it to ubuntu-snap lv

```bash
sudo -i
```

```c
cd /var/lib/lxc
cp -ar ubuntu-noble ubuntu-snap
if you use directory as a storage backend, then container directory will hold the rootfs, beware
nano ubuntu-snap/config
lxc.rootfs.path = lvm:/dev/astra/ubuntu-snap
```

Ctrl+S, Ctrl+X

```bash
exit
exit root shell
sudo lxc-start -n ubuntu-snap
```

start the container

```bash
sudo lxc-ls -f
ssh -l demo 10.0.3.X
```

```bash
sudo -i
```

```bash
apt install apache2
exit
exit
sudo lvs
```

Right not we do have the same feature with storage as with Docker, but with much more flexible and controllable manner

LVM thin snapshot can hold up to 100% changes

Usual snapshots are rarely created with 100% capacity

**NEVER EVER run out of a space in a pool!**

Running out of space in a thin pool will corrupt filesystems of all snapshots there

thin pool is just an lv, you can resize it any minute

First problems you will at 90-95% capacity filled

This will cause speed degradation at large
