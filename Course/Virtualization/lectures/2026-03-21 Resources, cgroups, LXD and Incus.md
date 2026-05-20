---
title: "Mar 21 - Resources, cgroups, LXD and Incus"
date: 2026-03-21
topics:
  - "resource limits"
  - "cgroups"
  - "LXD"
  - "Incus"
  - "LVM sizing"
tags:
  - virtualization
  - containers
  - cgroups
  - lxd
  - incus
  - lvm
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Mar 21 - Resources, cgroups, LXD and Incus

## LXC resources and cgroups

start the ubuntu-snap container

```bash
sudo lxc-start -n ubuntu-snap
sudo lxc-attach -n ubuntu-snap
```

uptime

you will see 0 min uptime, so you see uptime of your container

it was not always like that

this isolation is done using service called lxcfs

on the host:

```bash
sudo systemctl status lxcfs
```

just to remind you, use lxcfs service (check it is installed and check it is enabled)

## Resources

How can we limit the resources of the container?

Usually we do have only two resources important for us:

CPU

Memory

The size of the rootfs for a container is managed using LVM:

when you create a thin snapshot, it has the same size as the origin

```c
if you need more space, you can increase the size of the snapshot
```

The container is just a bunch of an isolated processes on a host. The mechanism behind limiting process resources is called cgroups.

For a long time there was cgroups v1, a liitle bit complicated and not very popular.

Let's limit our container to 512MiB of the RAM

```bash
sudo nano /var/lib/lxc/ubuntu-snap/config
lxc.cgroup2.memory.max = 512M
lxc.cgroup2.memory.high = 512M
lxc.cgroup2.memory.low = 256M
```

I would like to have at least 256 MiB of the RAM, but not more that 512MiB

Ctrl+S, Ctrl+X

In classic LXC you have to restart the container to make this work

```bash
sudo lxc-stop -n ubuntu-snap
sudo lxc-start -n ubuntu-snap
```

second thing to limit is CPU

CPU is limited in two ways:

first, you can bind a container to some CPUs (often used to bypass NUMA limitations)

second, you can limit the time CPU spends executing commands from the container (usually about the performance)

I would like to limit my container to 50% of the first CPU I do have.

```bash
sudo nano /var/lib/lxc/ubuntu-snap/config
lxc.cgroup2.cpuset.cpus = 0
lxc.cgroup2.cpu.max = 50000 100000
```

cpuset sets CPU binding (there could be some strings like 0-3 or comma separated lists, like 1,2,3,6,7)

cpu.max is microseconds and it has a format of MAX PERIOD

for a period of 100ms I do allow only 50ms of execution

Ctrl+S, Ctrl+X

```bash
sudo lxc-stop -n ubuntu-snap
sudo lxc-start -n ubuntu-snap
```

restart container again

We do have our ubuntu-snap as a snapshot from the origin, it has the same size (when it's created), but we can change it.

```bash
sudo lvresize -L4G astra/ubuntu-snap
```

but there is a catch!

there is an option to LVM to resize the filesystem! but I wouldn't recommend that in a prod env. why?

I do recommend manual resizing to be sure it is safe

because actually the resize of the LVM and resize of filesystem are done as two separate steps (they are separate, because each one is atomic)

we have to stop the container

```bash
sudo lxc-stop -n ubuntu-snap
sudo e2fsck -f /dev/astra/ubuntu-snap
sudo resize2fs /dev/astra/ubuntu-snap
sudo lxc-start -n ubuntu-snap
```

Size of the snapshot (thin snapshot!) does not matter, pool size and it's usage - that's what matters!

How can we check the limits imposed?

Let's try to run something complicated

```bash
lxc-attach -n ubuntu-snap
dd if=/dev/zero of=/dev/null bs=4M &
```

when run, dd uses only one core and uses 100% percent of it

okay, and what about memory?

I can use a small C program to use my memory

```bash
kill %1
kill %2
kill %3
apt install build-essential
apt install nano
nano memory.c
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  while (1) {
      void *ptr = malloc(100 * 1024 * 1024);

      if (ptr == NULL) {
        printf("Memory exhausted!\n");
        break;
      }

      memset(ptr, 1, 100 * 1024 * 1024);
      printf("Allocated 100MB...\n");
  }
  return 0;
}
```

small program to eat up memory

```bash
gcc memory.c -o memory
```

compile it

run it and see - container uses 512MiB of it's RAM, and then all of the swap

as soon as it was broken at line 14, it means, it was able to allocate 1500 MiB. why? because 500 MiB as RAM, all other as swap

we did not limit the swap, so container was able to use all of the available swap memory from host

```bash
lxc.cgroup2.memory.swap.max = 0
```

no swap for a container

## LXD

One of the well known developers of LXC was (and is) Stephane Graber, we was working with Canonical to create LXC, and then to lead the development of LXD

As podman was a Red Hat vision of Docker, LXD was a Canonical vision of Docker.

The main difference between LXC and LXD is architecture

LXD is more like Docker - it has a daemon to talk with and manage all the containers

LXD uses images

LXD was a step forward to use centralized management across a lot of LXD hosts

LXD was a step forward to configure some properties of a container

LXC gives you only a config file, you have to edit it - no declarative way here

LXD brings docker-compose way of managing properties of a container

Graber moved on from Canonical somewhere at 2018 or like that. In 2023 Canonical changes the licence for the LXD. The licence made it almost the property of the Canonical, not the opensource project.

The previous team of LXD decided to make a fork. And they did it, it's called **incus**

LXD - project of the Canonical

Incus - project of the original team

linuxcontainer.org (the source of all images) was shut down for LXD users, not for Incus users.

Ubuntu now has two packages: lxd and incus (because the original team of LXD created and maintained a package)

Incus is perfectly installable from the bare packages (you can just drop a bunch of packages and install it manually)

Always use a separate disk (or multiple disks) with incus

I have 32GiB disk on my machine

sudo vgcreate incus /dev/sdb

```bash
sudo apt install incus
```

Note while installing:

Incus has been installed. You must run `sudo incus admin init` to perform the initial configuration of Incus.

Be sure to add user(s) to either the 'incus-admin' group for full administrative access or the 'incus' group for restricted access, then have them logout and back in to properly setup their access.

```bash
sudo incus admin init --minimal
```

minimal configuration with all the defaults

```bash
sudo incus admin init
```

usual init procedure

Would you like to use clustering? (yes/no) [default=no]:

Do you want to configure a new storage pool? (yes/no) [default=yes]:

Name of the new storage pool [default=default]:

Name of the storage backend to use (dir, lvm, lvmcluster, btrfs) [default=btrfs]: lvm

Create a new LVM pool? (yes/no) [default=yes]:

Would you like to use an existing empty block device (e.g. a disk or partition)? (yes/no) [default=no]: yes

Path to the existing block device: /dev/sdb

Would you like to create a new local network bridge? (yes/no) [default=yes]:

What should the new bridge be called? [default=incusbr0]:

What IPv4 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: auto

What IPv6 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: none

Would you like the server to be available over the network? (yes/no) [default=no]:

Would you like stale cached images to be updated automatically? (yes/no) [default=yes]:

Would you like a YAML "init" preseed to be printed? (yes/no) [default=no]: yes

As soon as I have already created a VG called incus, the storage creation at the init failed. Let's fix it manually

```bash
sudo incus storage create default lvm source=incus
sudo incus image list images:
```

when looking at the images list, you can see that there is a VIRTUAL-MACHINE

images.linuxcontainers.org

this is a default download option for containers and vms

```bash
sudo incus image list images: debian amd64
sudo incus launch images:debian/13 thirteen
sudo incus profile device add default root disk pool=default path=/
```

this is to fix the default profile for network

I'll just run init once again without storage pool configuration and it will create incusbr0

```bash
sudo lvs
```

a lot of strings to understand

containers_thirteen - thin volume, which stores only the difference from images_XXX

images_XXXX - thin volume with image itself

Once again, this is not usual LVM logical volumes, these are thin volumes

The network is running, but I don't know - do I have SSH in this container or not

```bash
incus does not have attach command, but it has exec command
sudo incus exec thirteen bash
apt install openssh-server
adduser demo
```

the main goal of LXD was to create a scriptable Docker-like managed environment

```bash
sudo incus config set thirteen limits.memory=512MiB
sudo incus exec thirteen -- free -m
```

How can I manage files inside a container?

I can push/pull files within a container

```bash
sudo incus file pull thirteen/etc/hosts .
```

download a file from a container

upload file back

```bash
sudo incus file push <file> thirteen/<path>
```

what about kernel namespaces? which namespaces were created, when we started the container?

4026532249 user       10  2907 1000000          /sbin/init

we can see the user namespace, we didn't see that yet

UID is changed and some number is added to UID

Inside a container I'm root

Outside of container I'm UID of 1000000, which has no account at all

sudo pstree -u

├─incusd───systemd(1000000)─┬─agetty

│                           ├─dbus-daemon(1000997)

│                           ├─polkitd(1000990)───3*[{polkitd}]

│                           ├─sshd

│                           ├─systemd-journal

│                           ├─systemd-logind

│                           ├─systemd-network(1000998)

│                           ├─systemd-resolve(1000996)

│                           └─systemd-udevd

incusd, the daemon of the incus, runs with root privileges and changes the UID of running process of a container to a safe one

Homework (it's up to you): try to turn on user kernel namespace in Docker and see, how it works

```bash
incus has a way to make a backup (snapshot)
sudo incus snapshot list thirteen
sudo incus snapshot create thirteen snap1
```

attach and remove /usr/sbin

now I want my container back

```bash
sudo incus snapshot restore thirteen snap1
```

what was done? the parent of the incus container was changed

this is a good example of a usage of LVM for profit

LVM is very important for a modern storage

## -L vs -l

```bash
lvcreate / lvresize commands use -L or -l
lvcreate -L5G - create 5GiB lv
lvresize -L+2G - increase the size of the lv plus 2GiB
lvcreate -s -l10%ORIGIN - create a snapshot holding 10% of the origin size
lvresize -l+10%FREE - add 10% of free space in vg to lv
```
