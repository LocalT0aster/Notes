---
title: "Alpine VM with LVM and networking"
topics:
  - "Alpine Linux"
  - "QEMU"
  - "LVM-backed virtual disks"
  - "networking branch"
tags:
  - virtualization
  - virtual-machines
  - alpine
  - qemu
  - lvm
  - networking
source: "2026-04-11 Compose profiles and VM intro.md"
---

# Alpine VM with LVM and networking

This is the Alpine branch from [[guides/VM setup with LVM - branching guide|VM setup with LVM - branching guide]]. Alpine uses its own installer and OpenRC networking, then merges into [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]] for NAT, SSH forwarding, and bridge notes.

Assumptions:

- Host volume group: `astra`
- Host logical volume: `vm-alpine`
- Alpine ISO is in the current directory.
- QEMU uses the host LV as a raw disk.

## Select the image

Use Alpine's `virt` ISO for a VM. The exact version changes over time, so pick the current `alpine-virt-...x86_64.iso` from Alpine's latest stable x86_64 release directory.

Example from the lecture:

```bash
wget https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-virt-3.23.3-x86_64.iso
```

## Create the host LVM disk

```bash
sudo lvcreate -L2G -n vm-alpine astra
ls -l /dev/astra/vm-alpine
```

Use `format=raw` because an LVM LV is already a block device.

## Boot the installer

```bash
sudo qemu-system-x86_64 \
  -m 256 \
  -enable-kvm \
  -cpu host \
  -nographic \
  -cdrom alpine-virt-3.23.3-x86_64.iso \
  -boot d \
  -drive file=/dev/astra/vm-alpine,format=raw \
  -nic user,model=virtio-net-pci
```

## Bring up live ISO networking

Log in as `root`; the live ISO has no root password.

```bash
ip a
ip link set dev eth0 up
udhcpc -i eth0
ping -c 3 1.1.1.1
ping -c 3 alpine.org
```

## Install Alpine

Run:

```bash
setup-alpine
```

Use these choices for the lecture setup:

- Network interface: `eth0`
- IP configuration: `dhcp`
- NTP client: `chrony`
- Disk: `sda`
- Install mode: `sys`

Then shut down:

```bash
poweroff
```

## Boot from the installed disk

```bash
sudo qemu-system-x86_64 \
  -m 256 \
  -enable-kvm \
  -cpu host \
  -nographic \
  -drive file=/dev/astra/vm-alpine,format=raw \
  -nic user,model=virtio-net-pci
```

Continue to [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]].

## Alpine-specific persistence

If DHCP does not persist after install, `/etc/network/interfaces` should contain:

```ini
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```

Enable and restart networking:

```bash
rc-update add networking boot
rc-service networking restart
```

For SSH:

```bash
apk update
apk add openssh
rc-update add sshd default
rc-service sshd start
```

See [[guides/VM networking with QEMU and libvirt#SSH service in the guest|SSH service in the guest]] for the shared SSH notes.
