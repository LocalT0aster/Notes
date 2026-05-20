---
title: "Feb 7 - Namespaces and chroot"
date: 2026-02-07
topics:
  - "Linux namespaces"
  - "debootstrap"
  - "chroot"
  - "mount namespaces"
  - "pivot_root"
tags:
  - virtualization
  - containers
  - linux-namespaces
  - chroot
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Feb 7 - Namespaces and chroot

## Kernel namespaces and chroot

```bash
lsns
```

shows us the namespaces of the kernel

even Chromium is using container technologies to have a security separation of the processes

```bash
sudo lsns
```

more details

We need only three commands to fully utilize the power of namespaces:

```bash
lsns
unshare
nsenter
```

these commands come from util-linux package (usually the are present in any system)

```bash
sudo ls -l /proc/1/ns
```

we can see system namespaces this way

let's create a small container, but we have to start somewhere

we use Astra Linux, it is Russian Linux distribution, based on Debian, in Debian we have a debootstrap utility, which helps us to create a basic rootfs of a container

but we don't have a debootstrap right now, so we have to install it

to install a packet we have to know what are the sources of installation?

```bash
sudo nano /etc/apt/sources.list
```

Use Ctrl+K to cut the line, and then press Ctrl+U twice

change repository-main to repository-extended on the second line

Ctrl+S to save, Ctrl+X to exit

we have to update package index, so

```bash
sudo apt update
sudo apt install debootstrap
```

let's create a script to wrap up the long lines

```bash
nano makeastra
```
```bash
#!/bin/bash
debootstrap \
--include ncurses-term,locales,nano,gawk,lsb-release \
--components=main,contrib,non-free 1.8_x86-64 \
$1 \
```

http://dl.astralinux.ru/astra/stable/1.8_x86-64/repository-main

Ctrl+S, Ctrl+X

```bash
chmod +x makeastra
```

made my script an executable

```bash
sudo mkdir /var/tmp/astra1
```

I would like to create a directory to hold a root fs of my future container

```bash
sudo ./makeastra /var/tmp/astra1
```

start creating rootfs of container

right now we have a base root filesystem of a future container, how can we use it?

```bash
sudo du -hs /var/tmp/astra1
```

we can see it is 500+MB, but we have to know it is not optimized

Grandfather's way to use a container is called chroot

without any fancy containerization techniques we can switch to root fs of our container

```bash
cat /etc/astra/build_version
```

let see the version of our operating system

```bash
sudo chroot /var/tmp/astra1
cat /etc/astra/build_version
1.8.4.48
```

what is that? by using our makeastra script we've created the most recent version of Astra

but version of Astra for our Desktop is different

```bash
ls -l /boot
```

it's empty!

by default debootstrap doesn't install the kernel, and container doesn't need one - right now we are using kernel from our operating system

```bash
apt list -i | wc -l
```

I can see 260 packages installed, this is a system without graphical interface

```bash
df -h
```

ooops, not working, why? chroot only changes rootfs, nothing more

```bash
ps ax
```

nope, this doesn't work too

a lot of commands in modern Linux system use /sys and /proc

```bash
mount -t sysfs sys /sys
mount -t proc proc /proc
```

we kindly ask kernel to mount special filesystems

```bash
ps ax
```

working now!

```bash
df -h
```

still no luck

One can say: how can you guarantee no new namespaces created?

```bash
sudo lsns
```

no new namespaces here, because chroot

I would like to use a new tools with namespaces to achieve same result with root fs

what is the usage of the chroot in real life?

If you have a broken system (it doesn't boot up), you can use any boot device (CD or thumb drive), boot from it and chroot to your broken system to fix it up

to be polite, I should unmount what I've mounted, so:

```bash
umount /sys
umount /proc
exit
```

leaving container

## Task

we have to do the same, but with the modern tools

```bash
sudo unshare -m bash
```

I ask to run a bash in a new mount namespace

it means, that bash will have it's own list of mounts, completely separated from the basic system

-m means new mount namespace

```bash
sudo lsns
```

second tab

I can see my root bash process with mnt (mount) namespace created

go back to first tab

all the previous mount were copied to newly created namespace. why? you can't live without filesystem at all

```bash
cd /var/tmp
```

go to /var/tmp directory

```bash
mount --bind astra1 astra1
```

bind a directory to itself

this is where my container and my OS have different mounts

```bash
mount | grep astra1
```

I can see a line in a container, not in my VM

this is where I split

```bash
cd astra1
```

I go to astra1 directory

to change my rootfs I must use any directory to save the previous one, this is how kernel works

```bash
mkdir old_root
```

create an old_root directory

```bash
pivot_root . old_root
```

switch

nothing fancy happens, I mean you don't notice anything

```bash
ls -l /
```

I see root directory of my container, not from my real system

```bash
ls -l /old_root
```

this is the rootfs of my real system

```bash
mount -t sysfs sys /sys
mount -t proc proc /proc
```

once again, I mount my special kernel directories

```bash
df -h
```

now it finally works

it shows me the old picture. why? we still have old_root mounted

```bash
umount -l /old_root
df -h
```

now perfect

let's increase the size of our rootfs in VM

second tab

```bash
sudo lvresize -L16G astra/root --resizefs
```

increase the size of the rootfs in our real system
