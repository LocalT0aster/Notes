---
title: "Arch VM with LVM and networking"
topics:
  - "Arch Linux"
  - "QEMU"
  - "LVM-backed virtual disks"
  - "bootloader branches"
  - "networking"
tags:
  - virtualization
  - virtual-machines
  - arch-linux
  - qemu
  - lvm
  - branching-guide
source:
  - "2026-04-11 Compose profiles and VM intro.md"
  - "https://wiki.archlinux.org/title/Installation_guide"
  - "https://archlinux.org/download/"
---

# Arch VM with LVM and networking

This note is now a short branch index. Use it when you specifically want Arch; use [[guides/VM setup with LVM - branching guide|VM setup with LVM - branching guide]] for the full VM setup map.

## Flow

1. Start with [[guides/Arch VM base install on LVM|Arch VM base install on LVM]].
2. Choose one bootloader branch:
   - [[guides/Arch boot with UKI and systemd-boot|UKI + systemd-boot]] for a new UEFI VM without GRUB.
   - [[guides/Arch boot with GRUB|GRUB]] for the older BIOS/GRUB path.
3. Finish with [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]].

## Defaults

- Host VG: `astra`
- Host LV: `vm-arch`
- QEMU drive: `-drive file=/dev/astra/vm-arch,format=raw,if=virtio`
- Preferred new boot path: [[guides/Arch boot with UKI and systemd-boot|UKI + systemd-boot]]
- Preferred class networking path after install: [[guides/VM networking with QEMU and libvirt#Branch 2 virt-manager bridge|virt-manager bridge]]
