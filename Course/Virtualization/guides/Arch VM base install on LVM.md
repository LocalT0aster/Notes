---
title: "Arch VM base install on LVM"
topics:
  - "Arch Linux"
  - "QEMU"
  - "LVM-backed virtual disks"
  - "manual install"
tags:
  - virtualization
  - virtual-machines
  - arch-linux
  - qemu
  - lvm
source:
  - "2026-04-11 Compose profiles and VM intro.md"
  - "https://wiki.archlinux.org/title/Installation_guide"
  - "https://archlinux.org/download/"
---

# Arch VM base install on LVM

This is the common Arch branch before the bootloader-specific split. It uses an LVM logical volume on the hypervisor as the VM disk.

Continue to one bootloader note before partitioning:

- [[guides/Arch boot with UKI and systemd-boot|UKI + systemd-boot]]
- [[guides/Arch boot with GRUB|GRUB]]

## Host-side disk

Create a host LV for the VM disk:

```bash
sudo lvcreate -L20G -n vm-arch astra
ls -l /dev/astra/vm-arch
```

QEMU should see this as a raw virtio disk:

```bash
-drive file=/dev/astra/vm-arch,format=raw,if=virtio
```

## Select the image

Download the current Arch ISO. The filename changes monthly, so either keep the downloaded filename or rename it locally.

```bash
wget https://geo.mirror.pkgbuild.com/iso/latest/archlinux-x86_64.iso
```

Optional but recommended: verify the ISO checksum and signature using the current values from the Arch download page.

## Boot the installer

Use this BIOS-compatible command for the GRUB path:

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

Use OVMF/UEFI for the UKI path:

```bash
cp /usr/share/edk2/x64/OVMF_VARS.4m.fd ./OVMF_VARS_arch.fd

sudo qemu-system-x86_64 \
  -m 2048 \
  -enable-kvm \
  -cpu host \
  -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
  -drive if=pflash,format=raw,file=./OVMF_VARS_arch.fd \
  -cdrom archlinux-x86_64.iso \
  -boot d \
  -drive file=/dev/astra/vm-arch,format=raw,if=virtio \
  -nic user,model=virtio-net-pci
```

If the OVMF path differs on the hypervisor, locate it with:

```bash
find /usr/share -iname 'OVMF_CODE*.fd' -o -iname 'OVMF_VARS*.fd'
```

## Check live ISO networking

The Arch live ISO usually starts DHCP networking automatically.

```bash
ip -br link
ip -br addr
ip route
ping -c 3 1.1.1.1
ping -c 3 archlinux.org
```

If the interface has no address:

```bash
systemctl restart systemd-networkd
networkctl
```

## Choose the bootloader path

Pick exactly one:

- [[guides/Arch boot with UKI and systemd-boot|UKI + systemd-boot]] for UEFI/OVMF and no GRUB.
- [[guides/Arch boot with GRUB|GRUB]] for the older BIOS-oriented path.

Both paths end by booting into the installed system and then continue to [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]].
