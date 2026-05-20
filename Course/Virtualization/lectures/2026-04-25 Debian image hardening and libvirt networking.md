---
title: "Apr 25 - Debian image hardening and libvirt networking"
date: 2026-04-25
topics:
  - "Debian image hardening"
  - "systemd-networkd"
  - "systemd-resolved"
  - "disk layout"
  - "libvirt networking"
tags:
  - virtualization
  - virtual-machines
  - debian
  - systemd-networkd
  - libvirt
  - networking
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Apr 25 - Debian image hardening and libvirt networking

## Debian image preparation

We have created a new Debian installation from nocloud image. This is not suitable for a production setup, at least it has two problems:

1. it has only root account - you should not never ever use root to login remotely
2. we don't have any remote access right now - openssh is not installed

Additionaly I personally prefer to configure network using systemd-networkd. Why? Because in most cases this is the most comfortable way.

Let's create a user with a name preseed and password 12345678

Debian uses adduser (interactive), which wraps useradd (non-interactive)

```bash
adduser preseed
```

In Debian in most cases the best way to have an administrative privileges is sudo utility, and to be able to use it in default installation you have to be a member of sudo group

```bash
which sudo
adduser preseed sudo
```

adds user to sudo group

Now our preseed user is able to use sudo to become a superuser (root)

```bash
exit
```

log in as user preseed

now I can check if I'm able to become a root user

```bash
sudo -i
```

type in my password

We have created our account, but root still can log in with password (not remotely, but locally)

In most systems nowadays you can have a single-user mode, or recovery mode. To protect the physical console single user mode requires us to enter root password. And if root user do not have any, it fails.

You have to decide: will you support recovery mode or not.

I'll show you the way to remove root password.

```bash
passwd -dl root
```

this removes root password (cleans) and disables any login with password for root

```bash
cat /etc/shadow
```

we can see line starting with root:!:

it means this user has no password and no ability to log in with password at all by any means

```bash
apt update
apt install openssh-server
```

now we can continue remotely (but we won't right now)

let's move on to remote connection

```bash
ip a
```

find out the address

```bash
ssh 192.168.122.XX -l preseed
```

connect remotely

last step - make sure our VM initializes network correctly

for servers systemd-networkd is a best solution

```bash
sudo systemctl is-enabled systemd-networkd
```

systemd-networkd is enabled, good

```bash
sudo systemctl status networking
```

we don't have the old service

```bash
apt list -i | grep ifupdown
```

we don't have the old package

```bash
apt list -i | grep netplan
```

this shows we have netplan.io package

netplan is a special wrapper, which generates systemd-networkd config or NM config from it's own YAML config

```bash
sudo apt purge netplan.io
sudo apt autoremove
sudo rm -rf /etc/netplan
```

remove netplan completely

now we have to create a simple systemd-networkd configuration for any network interface to have a DHCP enabled

```ini
sudo nano /etc/systemd/network/dhcp.network
[Match]
Name=*
[Network]
DHCP=ipv4
```

Ctrl+S, Ctrl+X

now we have only one thing left - /etc/resolv.conf configuration

```bash
ls -l /etc/resolv.conf
```

this file is right now symlink to stub-resolver

```bash
sudo apt install iproute2
sudo ss -uanp
```

we can see port 53 opened

stub-resolver is a localhost bound resolver, which helps us to provide DNSSEC-aware resolver for all the internal needs

but this config is not very suitable for a server

we have to edit systemd-resolved configuration

```bash
sudo nano /etc/systemd/resolved.conf
```

what we have to change here?

uncomment and change to no

```ini
MulticastDNS=no
LLMNR=no
DNSStubListener=no
```

Ctrl+S, Ctrl+X

we have to restart systemd-resolved to pick up new config

```bash
sudo systemctl restart systemd-resolved
```

how we have to change the /etc/resolv.conf symlink - it should point to other file

```bash
sudo ln -svi /run/systemd/resolve/resolv.conf /etc/resolv.conf
```

make a new symlink

/run/systemd/resolve/resolv.conf file holds DNS resolvers, obtained via DHCP or other static configuration

```bash
sudo reboot
ssh 192.168.122.118 -l preseed
```

Now we have a complete small image, easily used for any VM for a future configuration.

Now we have only one thing left: what about disk? What is the partition layout?

```bash
sudo fdisk -l
```

we don't even have fdisk

usually you have to install following utilities

```bash
sudo apt install -qy fdisk gdisk parted
sudo fdisk -l
```

we see a lot of problems :)

```bash
Disk /dev/vda: 4 GiB, 4294967296 bytes, 8388608 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 985815F8-36C9-451D-A44D-3EE492D4C944
Device      Start     End Sectors  Size Type
/dev/vda1  262144 6289407 6027264  2.9G Linux root (x86-64)
/dev/vda14   2048    8191    6144    3M BIOS boot
/dev/vda15   8192  262143  253952  124M EFI System
```

What do we know from here?

1. we do have a modern partition table, which allows us to use any number of partitions up to 128
2. there are two partitions, both for booting the system either way: BIOS or UIEFI

```bash
/dev/vda14   2048    8191    6144    3M BIOS boot
/dev/vda15   8192  262143  253952  124M EFI System
/dev/vda1  262144 6289407 6027264  2.9G Linux root (x86-64)
```

3. numbers of partitions is mixed up for a good: if you would like to create more partitions, you can use free numbers like 2, 3, 4, etc.
4. I don't have a swap right now

We have a two options here:

1. create a swap, and resize root partition before - we can fix the size of rootfs to 32G or 64G and leave it
2. we can use a swap file instead of swap partition - swap file is usually create in root directory

swap file is worse than swap partition (LVM shaphot will hold it too)

let's reconnect to Astra now, and analyze the partition layout

```bash
efibootmgr
```

we see our OS boots to UEFI by failsafe default, and we don't have a dedicated record for Astra OS

this is a problem of a dd copy of an image - there is no information about boot records in image

what we should know: reinstall of the bootloader will bring everything back

```bash
sudo grub-install
```

reinstall the bootloader

```bash
BootCurrent: 0001
Timeout: 0 seconds
BootOrder: 0003,0001,0000,0002
Boot0000* UiApp
Boot0001* UEFI Misc Device
Boot0002* EFI Internal Shell
Boot0003* astra
```

remember to run `sudo grub-install` with any copy of your VM

## Networking

we've been using default network so far. it has a DHCP, it has it's own private IP subnet 192.168.122.0/24

```bash
sudo virsh net-list
```

right now we see default network defined, it's permanent (as soon as defined by files, not by command), it's not autostarting (can be a problem)

libvirt supports two types of connection:

1. when you create the object called network and VM references not the device itself, but network
2. when your VM references the bridge on the host to connect to

first way is better as long as you can migrate easily

in most cases you keep your configuration of network objects consistent (same) between all hypervisors to make migration easier

```bash
sudo virsh net-autostart default
```

this sets autostart for a network

always autostart network after creating it

there are two ways to utilize network adapter

1. create bridge, put vlanXX adapter to it, create network object pointing to bridge
2. use it with macvtap adapter, which was faster alternative to bridges many years ago

Since Linux kernel 5.0+ bridges were multiple times rewritten, so they are fast enough right now.

macvtap has one specific problem - you can't talk to VM from host using this type of adapter

we would like to use a bridged networking right now

I prefer create network objects using XML definition

you create a file, then you import it

our config is simple right now (on hypervisor)

we have br0 bridge, and we would like to use it

```bash
nano bridge.xml
```

```xml
<network>
  <name>bridge</name>
  <forward mode="bridge"/>
  <bridge name="br0"/>
</network>
```

this is a network object called bridge, using br0 as bridge

Ctrl+S, Ctrl+X

```bash
sudo virsh net-define bridge.xml
sudo virsh net-list --all
```

why? because our network is not active now

```bash
sudo virsh net-start bridge
```

start the network

```bash
sudo virsh net-autostart bridge
```

make it autostart
