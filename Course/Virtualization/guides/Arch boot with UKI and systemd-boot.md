---
title: "Arch boot with UKI and systemd-boot"
topics:
  - "Arch Linux"
  - "UKI"
  - "systemd-boot"
  - "UEFI"
  - "LVM root"
tags:
  - virtualization
  - virtual-machines
  - arch-linux
  - uki
  - systemd-boot
  - lvm
source:
  - "https://wiki.archlinux.org/title/Unified_kernel_image"
  - "https://wiki.archlinux.org/title/Systemd-boot"
  - "https://wiki.archlinux.org/title/LVM"
---

# Arch boot with UKI and systemd-boot

This is the pure UEFI branch: UKI, systemd-boot, no GRUB. Start from [[guides/Arch VM base install on LVM|Arch VM base install on LVM]] and boot the installer with OVMF/UEFI.

UKI requires UEFI. Check in the installer:

```bash
test -d /sys/firmware/efi && echo UEFI || echo BIOS
```

If this prints `BIOS`, reboot the installer with OVMF before continuing.

## Partition and format

With `if=virtio`, the VM disk is usually `/dev/vda`.

Check before destroying anything:

```bash
lsblk
```

Create a GPT disk with an ESP and an LVM PV:

```bash
sgdisk -n1:1MiB:+512MiB -t1:EF00 -c1:ESP /dev/vda
sgdisk -n2:0:0          -t2:8E00 -c2:arch-lvm /dev/vda

mkfs.fat -F32 /dev/vda1

pvcreate /dev/vda2
vgcreate arch /dev/vda2
lvcreate -L4G -n swap arch
lvcreate -l 100%FREE -n root arch

mkfs.ext4 -L arch-root /dev/arch/root
mkswap /dev/arch/swap
```

Mount the system:

```bash
mount /dev/arch/root /mnt
mkdir -p /mnt/efi
mount /dev/vda1 /mnt/efi
swapon /dev/arch/swap
```

## Install the base system

Install Arch without GRUB:

```bash
pacstrap -K /mnt base linux linux-firmware lvm2 sudo nano openssh efibootmgr
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
```

Optional microcode (ignore if you don't know):

```bash
pacman -S intel-ucode
# or
pacman -S amd-ucode
```

## Configure the installed system

Set time:

```bash
ln -sf /usr/share/zoneinfo/Asia/Kuwait /etc/localtime
hwclock --systohc
```

Set locale:

> If you are human, instead of `sed` you can do: `nano /etc/locale.gen` -> Where/Find -> `en_US` -> remove `#`.
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

## Configure mkinitcpio for LVM

Edit:

```bash
nano /etc/mkinitcpio.conf
```

> **⚠️⚠️⚠️Make sure `lvm2` is between `block` and `filesystems`⚠️⚠️⚠️**

```bash
HOOKS=(base udev autodetect microcode modconf kms keyboard keymap block lvm2 filesystems fsck)
```

## Set the UKI command line

Create the kernel command line file:

```bash
mkdir -p /etc/kernel
ROOT_UUID="$(blkid -s UUID -o value /dev/arch/root)"
echo "root=UUID=$ROOT_UUID rw" > /etc/kernel/cmdline
```

> The `root=` value points to the root filesystem UUID, not the host LV and not the ESP.
> If the `()` don't work for you for some reason, you can pipe the `blkid` to the file and edit with nano.
## Configure UKI output

Edit:

```bash
nano /etc/mkinitcpio.d/linux.preset
```

Use UKI outputs under the ESP mounted at `/efi`:

```bash
ALL_config="/etc/mkinitcpio.conf"
ALL_kver="/boot/vmlinuz-linux"

PRESETS=('default' 'fallback')

default_uki="/efi/EFI/Linux/arch-linux.efi"

fallback_uki="/efi/EFI/Linux/arch-linux-fallback.efi"
fallback_options="-S autodetect"
```

Comment out normal initramfs image outputs if they are present:

```bash
#default_image="/boot/initramfs-linux.img"
#fallback_image="/boot/initramfs-linux-fallback.img"
```

`/boot/vmlinuz-linux` remains the input kernel. The bootable artifact is the UKI under `/efi/EFI/Linux/`.

## Install systemd-boot and build UKIs

Install the bootloader:

```bash
bootctl --esp-path=/efi install
```

Optional loader config:

```bash
nano /efi/loader/loader.conf
```

```ini
default arch-linux.efi
timeout 3
editor no
```

Build the UKIs:

```bash
mkdir -p /efi/EFI/Linux
mkinitcpio -p linux
```

Verify (check):

```bash
ls -lh /efi/EFI/Linux
bootctl --esp-path=/efi list
bootctl kernel-identify /efi/EFI/Linux/arch-linux.efi
```

`kernel-identify` should identify the file as a UKI.

## Boot from the installed disk

Exit and shut down:

```bash
exit
umount -R /mnt
poweroff
```

Boot the installed VM with OVMF/UEFI and the same OVMF variables file:

```bash
sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
  -drive if=pflash,format=raw,file=./OVMF_VARS_arch.fd \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci
```

After first boot, continue to [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]].

## Troubleshooting

Empty systemd-boot menu:

- ESP was not mounted at `/efi` before `mkinitcpio -p linux`.
- UKIs were not generated under `/efi/EFI/Linux`.

Root device not found:

- `lvm2` is missing from `HOOKS`.
- `/etc/kernel/cmdline` has the wrong `root=`.

Boots as BIOS:

- QEMU was started without OVMF.
- The OVMF variables file is missing or not writable.
