---
title: "Arch boot with GRUB"
topics:
  - "Arch Linux"
  - "GRUB"
  - "BIOS boot"
  - "QEMU"
tags:
  - virtualization
  - virtual-machines
  - arch-linux
  - grub
  - qemu
source:
  - "Arch VM with LVM and networking.md"
  - "https://wiki.archlinux.org/title/GRUB"
---

# Arch boot with GRUB

This is the simple BIOS/GRUB branch for an Arch VM. It assumes the host exposes the VM disk as:

```bash
/dev/astra/vm-arch
```

Inside the Arch installer, that disk is usually:

```bash
/dev/vda
```

Start from [[guides/Arch VM base install on LVM|Arch VM base install on LVM]] before using this note.

## Partition and format

Check the disk before destroying anything:

```bash
lsblk
```

Create one MBR root partition:

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

Install a minimal system with GRUB:

```bash
pacstrap -K /mnt base linux linux-firmware grub sudo nano openssh
genfstab -U /mnt >> /mnt/etc/fstab
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

Set hostname and root password:

```bash
echo archvm > /etc/hostname
passwd
```

## Install GRUB

Install GRUB to the VM disk, not to the partition:

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

After first boot, continue to [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]].

## Troubleshooting

If GRUB fails to boot, boot the ISO again, mount the system, enter it, and reinstall GRUB:

```bash
mount /dev/vda1 /mnt
arch-chroot /mnt
grub-install --target=i386-pc /dev/vda
grub-mkconfig -o /boot/grub/grub.cfg
```

If `/dev/vda` is missing, confirm the host QEMU command uses:

```bash
-drive file=/dev/astra/vm-arch,format=raw,if=virtio
```
