---
title: "Alpine VM with LVM and networking"
topics:
  - "Alpine Linux"
  - "QEMU"
  - "LVM-backed virtual disks"
  - "user-mode networking"
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

This flow creates a small Alpine VM using an LVM logical volume as the disk. QEMU provides a virtual network card and a built-in DHCP/NAT network by default, so the VM can reach the internet without extra host-side bridge setup.

Assumptions:

- The volume group is called `astra`.
- The logical volume will be called `vm-alpine`.
- The Alpine ISO is in the current directory.
- Commands that access the LVM block device run with `sudo`.

## Select the image

Use Alpine's `virt` ISO for a VM. The exact version changes over time, so pick the current `alpine-virt-...x86_64.iso` from Alpine's latest stable x86_64 release directory.

Example from the lecture:

```bash
wget https://dl-cdn.alpinelinux.org/alpine/latest-stable/releases/x86_64/alpine-virt-3.23.3-x86_64.iso
```

## Install QEMU tools

```bash
sudo apt install --no-install-recommends qemu-system-x86 qemu-utils
```

## Create the LVM disk

Create a 2 GiB logical volume:

```bash
sudo lvcreate -L2G -n vm-alpine astra
```

Check that the block device exists:

```bash
ls -l /dev/astra/vm-alpine
```

The QEMU disk format is `raw` because an LVM logical volume is already a block device. Do not use `qcow2` here.

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

Options:

- `-m 256` gives the VM 256 MiB of RAM.
- `-enable-kvm -cpu host` uses hardware virtualization when available.
- `-nographic` keeps the VM in the terminal.
- `-cdrom ... -boot d` boots from the Alpine ISO.
- `-drive file=/dev/astra/vm-alpine,format=raw` uses the LVM volume as the VM disk.
- `-nic user,model=virtio-net-pci` gives the VM outbound NAT networking with DHCP.

## Bring up networking in the live ISO

Log in as `root`; the live ISO has no root password.

Check that the virtual NIC exists:

```bash
ip a
```

Bring up `eth0` and request an address:

```bash
ip link set dev eth0 up
udhcpc -i eth0
```

Verify connectivity:

```bash
ip a show eth0
ip route
ping -c 3 1.1.1.1
ping -c 3 alpine.org
```

If the IP ping works but the domain ping fails, check DNS:

```bash
cat /etc/resolv.conf
```

## Install Alpine to the LVM disk

Run the installer:

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

Start QEMU without the ISO:

```bash
sudo qemu-system-x86_64 \
  -m 256 \
  -enable-kvm \
  -cpu host \
  -nographic \
  -drive file=/dev/astra/vm-alpine,format=raw \
  -nic user,model=virtio-net-pci
```

After boot, networking should come up from the installed configuration. If it does not:

```bash
ip link set dev eth0 up
udhcpc -i eth0
```

For persistent DHCP, `/etc/network/interfaces` should contain:

```ini
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```

Enable and restart networking if needed:

```bash
rc-update add networking boot
rc-service networking restart
```

## Optional SSH access from the host

QEMU user-mode networking lets the VM reach the internet, but the host cannot directly connect into the VM unless you forward a port.

Boot with host port `2222` forwarded to guest port `22`:

```bash
sudo qemu-system-x86_64 \
  -m 256 \
  -enable-kvm \
  -cpu host \
  -nographic \
  -drive file=/dev/astra/vm-alpine,format=raw \
  -nic user,model=virtio-net-pci,hostfwd=tcp::2222-:22
```

Inside Alpine, install and start SSH:

```bash
apk update
apk add openssh
rc-update add sshd default
rc-service sshd start
```

Connect from the host:

```bash
ssh -p 2222 root@127.0.0.1
```

For real use, create a normal user and use SSH keys instead of logging in as root.

## Troubleshooting

No `eth0`:

```bash
ip link
```

If there is no NIC at all, make sure QEMU was started with `-nic user,model=virtio-net-pci` and not `-nic none`.

No IP address:

```bash
ip link set dev eth0 up
udhcpc -i eth0
```

No DNS:

```bash
cat /etc/resolv.conf
```

Cannot boot from disk:

```bash
sudo fdisk -l /dev/astra/vm-alpine
```

If the disk is empty or not marked as installed, boot from the ISO again and rerun `setup-alpine`, selecting `sda` and `sys`.
