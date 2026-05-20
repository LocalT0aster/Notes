---
title: "Arch VM with LVM and networking"
topics:
  - "Arch Linux"
  - "QEMU"
  - "LVM-backed virtual disks"
  - "systemd-networkd"
tags:
  - virtualization
  - virtual-machines
  - arch-linux
  - qemu
  - lvm
  - networking
source:
  - "2026-04-11 Compose profiles and VM intro.md"
  - "https://wiki.archlinux.org/title/Installation_guide"
  - "https://archlinux.org/download/"
---

# Arch VM with LVM and networking

This flow creates an Arch Linux VM using an LVM logical volume as the disk. It uses QEMU user-mode networking for simple outbound internet access and configures `systemd-networkd` inside the installed system for persistent DHCP.

This note deliberately uses a manual install instead of `archinstall`, because the goal is to understand the disk, bootloader, and network pieces.

Assumptions:

- The volume group is called `astra`.
- The logical volume will be called `vm-arch`.
- The Arch ISO is in the current directory.
- The VM uses classic BIOS boot, not UEFI.
- Commands that access the LVM block device run with `sudo`.

## Select the image

Download the current Arch ISO from the official download page or an official mirror. The filename changes monthly, so either keep the downloaded filename or rename it locally.

Example:

```bash
wget https://geo.mirror.pkgbuild.com/iso/latest/archlinux-x86_64.iso
```

Optional but recommended: verify the ISO checksum and signature using the current values from the Arch download page.

## Install QEMU tools

```bash
sudo apt install --no-install-recommends qemu-system-x86 qemu-utils
```

## Create the LVM disk

Arch needs more room than Alpine. A small but usable test VM can start with 20 GiB:

```bash
sudo lvcreate -L20G -n vm-arch astra
```

Check that the block device exists:

```bash
ls -l /dev/astra/vm-arch
```

The QEMU disk format is `raw` because an LVM logical volume is already a block device. Do not use `qcow2` here.

## Boot the installer

Use a graphical QEMU window if available:

```bash
sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -cdrom archlinux-x86_64.iso \
  -boot d \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci
```

Options:

- `-m 2048` gives the VM 2 GiB of RAM.
- `-enable-kvm -cpu host` uses hardware virtualization when available.
- `-cdrom ... -boot d` boots from the Arch ISO.
- `-drive file=/dev/astra/vm-arch,format=raw,if=virtio` uses the LVM volume as a virtio disk, usually visible as `/dev/vda`.
- `-nic user,model=virtio-net-pci` gives the VM outbound NAT networking with DHCP.

If you need a terminal-only display, try:

```bash
sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -display curses \
  -cdrom archlinux-x86_64.iso \
  -boot d \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci
```

Do not assume `-nographic` will work cleanly with every Arch ISO boot path; the installer console may be on VGA rather than the serial console.

## Check live ISO networking

The Arch live ISO normally starts DHCP networking automatically through `systemd-networkd` and `systemd-resolved`.

Check the interface and address:

```bash
ip -br link
ip -br addr
ip route
```

Verify connectivity:

```bash
ping -c 3 1.1.1.1
ping -c 3 archlinux.org
```

If the interface has no address, restart networkd and inspect the link:

```bash
systemctl restart systemd-networkd
networkctl
```

If IP connectivity works but DNS fails:

```bash
resolvectl status
cat /etc/resolv.conf
```

## Partition and format the LVM disk

With `if=virtio`, the disk should usually be `/dev/vda`.

Check before destroying anything:

```bash
lsblk
```

Create a simple BIOS/MBR partition table with one root partition:

```bash
parted -s /dev/vda mklabel msdos
parted -s /dev/vda mkpart primary ext4 1MiB 100%
mkfs.ext4 -L arch-root /dev/vda1
```

Mount it:

```bash
mount /dev/vda1 /mnt
```

## Install the base system

Install a minimal bootable system plus GRUB, an editor, OpenSSH, and sudo:

```bash
pacstrap -K /mnt base linux linux-firmware grub sudo nano openssh
```

`linux-firmware` is often not strictly necessary for a simple VM, but including it keeps the install closer to the official generic package set.

Generate `fstab`:

```bash
genfstab -U /mnt >> /mnt/etc/fstab
```

Check it:

```bash
cat /mnt/etc/fstab
```

Enter the installed system:

```bash
arch-chroot /mnt
```

## Configure the installed system

Set time:

```bash
ln -sf /usr/share/zoneinfo/Asia/Kuwait /etc/localtime
hwclock --systohc
```

Set locale:

```bash
sed -i 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
locale-gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
```

Set hostname:

```bash
echo archvm > /etc/hostname
```

Set root password:

```bash
passwd
```

## Configure persistent DHCP networking

Create a simple `systemd-networkd` DHCP config for Ethernet-like interfaces:

```bash
nano /etc/systemd/network/20-wired.network
```

```ini
[Match]
Name=en*

[Network]
DHCP=yes
```

Enable networking and DNS:

```bash
systemctl enable systemd-networkd
systemctl enable systemd-resolved
ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

The broad `Name=en*` match is intentional for a VM, because the virtio interface name can vary, for example `ens3` or `enp0s3`.

## Install the bootloader

Install GRUB for BIOS boot:

```bash
grub-install --target=i386-pc /dev/vda
grub-mkconfig -o /boot/grub/grub.cfg
```

Exit and shut down:

```bash
exit
umount -R /mnt
poweroff
```

## Boot from the installed disk

Start QEMU without the ISO:

```bash
sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci
```

Log in as `root`, then verify networking:

```bash
ip -br addr
networkctl
resolvectl status
ping -c 3 1.1.1.1
ping -c 3 archlinux.org
```

If the VM has an IP address and both pings work, networking is ready.

## Optional SSH access from the host

QEMU user-mode networking gives the VM outbound access, but the host cannot connect into the VM unless you forward a port.

Boot with host port `2222` forwarded to guest port `22`:

```bash
sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci,hostfwd=tcp::2222-:22
```

Inside Arch, enable SSH:

```bash
systemctl enable --now sshd
```

Create a normal user:

```bash
useradd -m -G wheel -s /bin/bash preseed
passwd preseed
```

Allow the `wheel` group to use sudo:

```bash
EDITOR=nano visudo
```

Uncomment:

```sudoers
%wheel ALL=(ALL:ALL) ALL
```

Connect from the host:

```bash
ssh -p 2222 preseed@127.0.0.1
```

For real use, add SSH keys and avoid password-based root login.

## Troubleshooting

No disk:

```bash
lsblk
```

If `/dev/vda` is missing, check that QEMU started with:

```bash
-drive file=/dev/astra/vm-arch,format=raw,if=virtio
```

No IP address:

```bash
ip -br addr
systemctl status systemd-networkd
networkctl
```

No DNS:

```bash
systemctl status systemd-resolved
resolvectl status
ls -l /etc/resolv.conf
```

Cannot boot from disk:

```bash
sudo fdisk -l /dev/astra/vm-arch
```

If there is no partition table, boot the ISO again and redo partitioning. If partitions exist but GRUB fails, boot the ISO, mount `/dev/vda1` to `/mnt`, `arch-chroot /mnt`, and rerun:

```bash
grub-install --target=i386-pc /dev/vda
grub-mkconfig -o /boot/grub/grub.cfg
```

## References

- [Arch Linux downloads](https://archlinux.org/download/)
- [ArchWiki installation guide](https://wiki.archlinux.org/title/Installation_guide)
- [ArchWiki systemd-networkd](https://wiki.archlinux.org/title/Systemd-networkd)
