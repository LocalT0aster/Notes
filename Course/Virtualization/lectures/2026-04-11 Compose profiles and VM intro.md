---
title: "Apr 11 - Compose profiles and VM intro"
date: 2026-04-11
topics:
  - "Compose variables"
  - "Compose profiles"
  - "virtual machines"
  - "QEMU"
  - "KVM"
  - "libvirt"
tags:
  - virtualization
  - docker-compose
  - virtual-machines
  - qemu
  - kvm
  - libvirt
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Apr 11 - Compose profiles and VM intro

## Compose variables and profiles

We will use env variables to make same docker-compose.yml be fit for production or development.

Let's replace volume definition with this string:

- ${DB_DIR:-postgres}:/var/lib/postgresql

If there is DB_DIR variable defined, use it's value to provide a source for the volume

If it is not defined, the use a default value of "postgres" - meaning there will be the volume

What's about env variables? There are two main thing to know:

1. docker-compose.yml supports using env variables and it reads automatically file called .env from current directory to fill it. Thing to remebers: these variables are not available to containers! Only to docker-compose.yml
2. If you would like to use same variables within a container, you should use env_file and specify the file to use (you can point to the same .env file if it fits)

```bash
DB_DIR=./data docker compose up
```

This is for a one-run condition, not very useful for a production, but I can make .env file and put all the variables there

```bash
DB_DIR=./data
```

and remember, that docker compose allows me to use a dot as a current directory

what about variables in container?

first way: drop only thouse you need, by using the environment: block

```yaml
environment:
  FIRST: $FIRST
```

second way: I can use env_file block and pass all the things

```bash
env_file: .env
```

you must know, that root user can see all the env variables of any process running on a host.

once again about building flexible docker-compose.yml

in some cases there is not enough to specify a variable, but you need to customize the way you run an application or do any other thing with it

going back to our pytime container

create a new file docker-compose.yml

```yaml
services:
  pytime:
    image: pytime:2.0-compose
    restart: unless-stopped
    build: .
    ports:
      - "8080:8080"
```

right now this suits the production requirements, but makes very complicated way to develop it

1. I would like to run it with a --debug parameter, but not always, only for a dev
2. I would like to change the code directly, not rebuilding each time I've changed the file
3. I would like to have a clear separation of prod and dev

I will create a new file called docker-compose.override.yml

```yaml
services:
  pytime:
    command: --debug
    volumes:
      - ./app:/app
```

I specify --debug to add and also binding a directory from a host.

Don't be tricked by the override word: it combines the new docker-compose.yml by using your docker-compose.yml

You can't cancel the parameter, you can override it with variable defined in docker-compose.yml (but not with arrays or objects yet)

In future versions it's promised to make a flag, which will mean "override the value completely"

In a production area you do not have .override file, and best way not to have it in a production is not to commit it to the repo!

Instead you create README.md with instructions how to create .override file for a development, or you can create it and commit it with the different name (I usually add minus to it) docker-compose.override.yml-

## Profiles and other small things

the same docker container could be run differently even in production. why?

1. You may (and will) have tests. In Python you can distribute them with you app. Why? To have a command to check the application sanity before running it.
2. There are combination of different ways of running application

dev: run flask server, fast, not very productive, don't care

prod: run special WSGI server with tailored configuration, memory requirements, parallel execution etc.

first thing to know: you don't have ENTRYPOINT any more. now you don't have anything at all.

```dockerfile
ENTRYPOINT is removed, each way to run a container requires you to have a command
```

docker-compose.yml

```bash
x-app-base: &app-base
```

```yaml
  image: pytime:2.0-compose
  restart: unless-stopped
  build: .
  ports:
    - "8080:8080"

services:
  app:
    <<: *app-base
    command: this is command to run in a production way
    profiles: ["prod", "dev"]
    # this section will be run with override (dev)
    # and without override (prod)
  stage:
    <<: *app-base
    profiles: ["stage"]
    command: this is command to run almost as a production
    # runs without override, but runs as dev
  tests:
    <<: *app-base
    profiles: ["test"]
    command: this is a command to run a test
```

docker-compose.override.yml

```yaml
services:
  app:
    command: this is command to run as a development
    volumes:
      - ./app:/app
  adminer:
    ...
```

And as long as I have profiles defined, I run this like this:

```bash
docker compose --profile dev up
```

## Virtual Machines

First of all, small overview:

QEMU (+KVM)

VirtualBox

We have to divide all the technologies here:

1. User-defined VM (VirtualBox, VMware Player, Virtual PC)

Run a user-defined VM, limited performance in networking, more features for a user, like snapshots or anything else.

It uses files as backend to hold the disks of the VM. Performance problems, but for user it's unimportant.

2. System-defined VM

**Hyper-V (Windows)** - part of the Windows Server (buy a Windows Server), standalone Hyper-V server available

Standalone Hyper-V server requires you to have a management tools (they are only Windows versions!)

**Proxmox** - it exists as a complete OS or could be installed if packaged for your system

Their complete OS is a strage abomination - it has a kernel from Ubuntu (because Ubuntu Kernel Team are the gods of the fixes), but the package base is from Debian. They do have a paid support. Inside it is a web-interface for KVM and LXC/LXD

**oVirt** - KVM the way Red Hat would like you to use

**VMware ESXi** (vSphere for a money) - this is a complete UNIX-base OS, allows you to run VM. It has a specific management software, available only for Windows. ESXi was always free, but not open source. Broadcom bought VMware and first removed ESXi from availability.

**KVM** - Kernel Virtual Machines, Linux vision of VM. NIH syndrome was not used here, QEMU was a emulator for a x86 for a while, so there was created a way to offload the QEMU instructions to the real CPU. libvirt was created as a wrapper around running all of this.

QEMU can run any VM without KVM support. The only problem is speed. 10-100 times slower without KVM, but once again it is possible.

First of all, we have to install QEMU binaries to run something.

```bash
sudo apt install --no-install-recommends qemu-system-x86 qemu-utils
```

Now we need something to play with, I do recommend Alpine as a small and funny distribution.

```bash
wget https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-virt-3.23.3-x86_64.iso
qemu-system-x86_64 -m 256 -nographic -cdrom alpine-virt-3.23.3-x86_64.iso -boot d -cpu max
```

-m - amount of memory, 256MiB (Alpine is small)

-nographic means output a text to the Terminal, no dedicated graphic device

-cdrom - attach a file to be a CD

-boot d - boot from CD

-cpu max - boosts a little bit

Just wait up for it to boot

```bash
root (no password)
```

Quick check of parameters we have:

```bash
nproc (1 CPU)
free -m
ip a
```

we can see eth0!

```bash
ip l set dev eth0 up
```

no IP here, as far as I have no DHCP client running

```bash
udhcpc -i eth0
```

Alpine uses udhcpc as a DHCP-client

I can have an IP-address from a DHCP-server

```bash
ping ya.ru
```

Actually QEMU makes a software emulation of the DHCP-server and also provides you with a network adapter.

If you specially don't want to have network adapter

-nic none

We cannot install OS now, because we have no disk! We have CPU, memory, and networking but no disk.

Which ways do we have to have a disk?

1. qcow files are the only option, if you would like to run rootless
2. LVM is a way to provide a storage - usually only root is allowed to use a device with write permissions

```bash
sudo lvcreate -L2G -n vm-alpine astra
```

If you don't have enough free space, remove these

```bash
sudo lvremove astra/homesnap
```

astra/ubuntu-snap

astra/ubuntu-noble

astra/test

Now we would like to run a VM with a disk

```c
sudo qemu-system-x86_64 -m 256 -nographic -cdrom alpine-virt-3.23.3-x86_64.iso -boot d -drive file=/dev/astra/vm-alpine,format=raw -cpu max
if you would like to run a vm with LVM without sudo, you can use disk group - it has a write permission to the block devices. from the security perspective group disk equals root (you can edit sudoers file with a filesystem debugger)
ls -l /dev/sda
fdisk -l /dev/sda
```

it is our LV of 2G

```bash
setup-alpine
```

Timezone: Europe/Moscow

chrony for NTP

```bash
sda
sys
poweroff
```

Now I can run my VM without CD, because I don't need it.

```bash
sudo qemu-system-x86_64 -m 256 -nographic -drive file=/dev/astra/vm-alpine,format=raw -cpu max
```

right now we run our VM manually, but we can create a systemd-unit and run it with the system

once again, we run a VM right now with a software emulation of the x86 CPU. How can we use a Linux machine as full fledged hypervisor?

I would like to use bare metal machines to run VMs, and also I would like to have a GUI to manage them.

Usually for beginners we start with the same machine: in a class you use a physical machine to run VMs

we have to provide ourselves with a bare-metal machine, so lets generate SSH-keys

```bash
ssh-keygen
ls -l .ssh
```

Depending on your user number:

1-4

```bash
172.30.44.103
```

5-8

```bash
172.30.44.65
```

9-12

```bash
172.30.44.122
```

13-16

```bash
172.30.44.91
```

17-19

```bash
172.30.44.93
```

we should access them with a different login - your login will be demoXX (and password 123)

right now we have to copy the key to allow us to log in without password

```c
ssh-copy-id demoXX@172.30.44.XX
if my key was installed, I can log in with SSH without anything
ssh demoXX@172.30.44.XX
```

open a new tab and let's install the tool required

```bash
sudo apt install --no-install-recommends virt-manager gir1.2-spiceclientgtk-3.0
```

virt-manager - is a tool to manage VMs with GUI

File - New connection

We use SSH to connect
