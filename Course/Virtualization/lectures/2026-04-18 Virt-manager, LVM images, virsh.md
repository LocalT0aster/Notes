---
title: "Apr 18 - Virt-manager, LVM images, virsh"
date: 2026-04-18
topics:
  - "virt-manager"
  - "Astra VM installation"
  - "LVM-backed images"
  - "virsh templates"
  - "Debian cloud image"
tags:
  - virtualization
  - virtual-machines
  - virt-manager
  - lvm
  - virsh
  - debian
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Apr 18 - Virt-manager, LVM images, virsh

## Creating VM images with virt-manager

Usually virt-manager makes this process like two step:

1. install OS
2. reboot and just load it

We create a new virtual machine and select Manual install

When got to virtual disk, we have to SSH to our hypervisor

```bash
ssh 172.30.44.XX -l demoXX
sudo vgs
```

to see which volume groups I do have here

alse18

```bash
sudo lvcreate -n vm-astraXX -L16G alse18
```

I create a new logical volume

Add netfs1.8.3.08-21.08.25_15.43.iso

nfs.corp

/opt/nfs/astra/1.8

1.8.3.08-21.08.25_15.43.iso

Created VM, then:

1. Changed boot to UEFI (OVMF_CODE_4M.fd)
2. Add a CD-ROM with 1.8.3.08-21.08.25_15.43.iso
3. Boot order - select CD-ROM and move it to the top

Kernel: 6.12 (or any more recent kernel)

Software: remove all but "Base packages" and "Fly desktop"

The only thing we have to think about is partitioning profile.

We have two approaches here (both with their own pros and cons):

1. Use the simplest partitioning without KVM

Pro:

- simple
- easy to mount partition from the hypervisor (if needed)

Cons:

- you don't have KVM inside (means no backups from the VM itself)

What's the problem with making a snapshot outside - using hypervisor?

The troublemaker here is a database. Why? You can't guarantee at any given moment, that the content of the RAM cache was flushed to disk. This could be guaranteed only inside of VM (you shutdown DB server and it flushes all the caches).

2. Use LVM when database is inside (or you need to do a consistent backup from VM itself)

What scheme I would recommend for the simplest VM?

1. 1GiB for EFI boot
2. 4-8 GiB for swap
3. The root FS

Users manager

Login: preseed

Password: Qwerty78

By default Astra protects the boot settings with the same login/password, we can remove it later, but in the installer

After the installation we have to remove CD-ROM and reboot.

I remove CD-ROM from the devices and boot.

Log in using my preseed account

Open up the terminal and run

```bash
ip a
```

to take a look at network settings.

```bash
ping ya.ru
```

I do have an internet connection, and some strange IP address like 192.168.122.XX

What do I have in resolvers?

```bash
cat /etc/resolv.conf
```

resolver is at 192.168.122.1

Basically I don't use this OS as OS, but as image - I usually rename and make the image readonly, and then use it as a base for other VMs.

Let's do an image and let's use it. Shut down the VM and let's delete it.

```bash
sudo lvrename alse18/vm-astraXX alse18/image-astraXX
```

now I have to protect it from being written to

```bash
sudo lvchange -p r alse18/image-astraXX
```

make it readonly

```bash
sudo lvcreate -n vm-astraXX -L20G alse18
```

create a slightly bigger image

```bash
sudo dd if=/dev/alse18/image-astraXX of=/dev/alse18/vm-astraXX bs=4M conv=fsync status=progress
```

copy the source to dest

Now I can create VM from image

Remember to change boot to UEFI!

But I have to use all the remaining space, how can I do that?

In VM, I would like to have an openssh-server

I can't install it right now, because OS would like to use CD as a package source and I don't have it connected.

```bash
sudo nano /etc/apt/sources.list
```

uncomment two first lines, comment line with CD-ROM

replace "stable" with "frozen"

after 1.8_x86-64/ type 1.8.3/uu/1/

Ctrl+S, Ctrl+X

```bash
sudo apt update
sudo apt install openssh-server
```

now I can connect my VM from my hypervisor using SSH

my "default" network is perfectly visible from the host

on my hypervisor I can do

```bash
ip a
```

to see that I have a virbr0 inteface with IP address 192.168.122.1

```bash
ssh 192.168.122.53 -l preseed
```

What's the deal? The disk of the VM is bigger, than the disk of the origin. How can I use it fully?

```bash
sudo fdisk -l
```

First, let's fix the GPT table

```bash
sudo sgdisk -e /dev/vda
```

but I don't have it now, so let's install it

```bash
sudo apt install gdisk
sudo fdisk -l
```

I see no warnings

Here I have to remember the number of my partition

```bash
sudo parted /dev/vda resizepart 3 100%
```

it could be done non-interactively with -s

```bash
sudo fdisk -l
```

should show me the new size of the partition, but still, my filesystem is not resized

```bash
sudo resize2fs /dev/vda3
df -h
```

Next task: how to create VM quickly?

By now we were using the virt-manager to create a new VM. This is not the best way to do that.

To make it faster we should know about the virsh command

Let's use our VM as a template

We get back to hypervisor

```bash
sudo virsh list
```

this will show you only the running VMs

```bash
sudo virsh list --all
```

this will show you even the stopped ones

```bash
sudo virsh destroy astra20
```

I will stop it forcefully

```bash
sudo virsh list --all
```

I would like to export the configuration of my VM

The configuration of VMs is stored in XML format somewhere in /etc/libvirt directory, but I can export it (and then edit to make fit)

```bash
sudo virsh dumpxml astraXX
```

will dump XML to stdout, which is not very good but useful for testing

```bash
sudo virsh dumpxml astraXX > template_astra.xml
```

save it to file called template_astra.xml

right now file is perfectly editable by us

```bash
nano template_astra.xml
```

What should be changed to make a good template?

Please use Ctrl+K to remove a line

1. remove `<uuid>` section
2. remove currentMemory line
3. change KiB to GiB and edit value to 2

```xml
<memory unit='GiB'>2</memory>
```

4. remove mac address

Ctrl+S, Ctrl+X

now I can copy and change the template

all lines with the name of the VM could be changed automatically

let's create VM called astraXX-new

```bash
cp template_astra.xml astraXX-new.xml
grep astraXX astraXX-new.xml
```

let's use sed to replace "astraXX" to "astraXX-new"

```bash
sed -i s/astraXX/astraXX-new/g astraXX-new.xml
```

this replaces automatically

check it is working

now we have to import the .xml file back again

```bash
sudo virsh define astraXX-new.xml
Domain 'astraXX-new' defined from astraXX-new.xml
```

To create a disk, let's rename the old one.

```bash
sudo lvrename alse18/vm-astraXX alse18/vm-astraXX-new
```

and now I would like to start a VM from a command line

```bash
sudo virsh start astraXX-new
```

How can we create other VM without installing?

All the major Linux OS have an image already prepared to be used as a VM

Let's do that with Debian 13

https://cloud.debian.org/images/cloud/trixie/20260402-2435/

```bash
wget https://cloud.debian.org/images/cloud/trixie/20260402-2435/debian-13-nocloud-amd64-20260402-2435.raw
```

on hypervisor

```bash
sudo lvcreate -n vm-debianXX -L4G alse18
```

create a logical volume for a debian image

```bash
sudo dd if=debian-13-nocloud-amd64-20260402-2435.raw of=/dev/alse18/vm-debianXX bs=4M conv=fsync
```

do not change BIOS, because Debian image uses BIOS to boot

change console to Serial

timezone name Europe/Moscow

```bash
root password - 123
```
