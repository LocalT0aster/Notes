---
title: "VM setup with LVM - branching guide"
topics:
  - "QEMU"
  - "LVM-backed virtual disks"
  - "Arch Linux"
  - "Alpine Linux"
  - "VM networking"
tags:
  - virtualization
  - virtual-machines
  - qemu
  - lvm
  - branching-guide
source: "2026-04-11 Compose profiles and VM intro.md"
---

# VM setup with LVM - branching guide

Use this as the entry point for manual VM setup notes. The host-side idea is always the same: create an LVM logical volume on the hypervisor and expose it to QEMU or libvirt as a raw disk.

```text
Host LVM logical volume
  -> QEMU/libvirt raw disk
  -> guest installer
  -> choose OS path
  -> choose bootloader path when needed
  -> networking setup
```

## Common host setup

Install QEMU tools on the hypervisor:

```bash
sudo apt install --no-install-recommends qemu-system-x86 qemu-utils
```

Use a raw LVM block device as the VM disk. Do not use `qcow2` for the drive format when the drive is an LV.

Arch example:

```bash
sudo lvcreate -L20G -n vm-arch astra
ls -l /dev/astra/vm-arch
```

Alpine example:

```bash
sudo lvcreate -L2G -n vm-alpine astra
ls -l /dev/astra/vm-alpine
```

## Choose the OS branch

- [[guides/Arch VM base install on LVM|Arch VM base install on LVM]]
- [[guides/Alpine VM with LVM and networking|Alpine VM with LVM and networking]]

## Arch bootloader branch

Arch needs an explicit bootloader decision before partitioning, because the disk layout changes.

- [[guides/Arch boot with UKI and systemd-boot|Arch boot with UKI and systemd-boot]] - UEFI/OVMF, ESP, UKI, no GRUB.
- [[guides/Arch boot with GRUB|Arch boot with GRUB]] - simple BIOS/GRUB path.

Prefer UKI + systemd-boot for a new UEFI VM. Keep GRUB as the compatibility path when the VM is already BIOS-oriented or when the course task explicitly asks for GRUB.

## Networking branch

After the guest boots, use the shared networking note:

- [[guides/VM networking with QEMU and libvirt|VM networking with QEMU and libvirt]]

That note covers the two normal connection modes:

- QEMU user-mode NAT with optional SSH port forwarding.
- virt-manager/libvirt bridge attachment to host `br0`.

## Existing guide shortcuts

- [[guides/Arch VM with LVM and networking|Arch VM with LVM and networking]] now points back to this branch map.
- [[guides/Alpine VM with LVM and networking|Alpine VM with LVM and networking]] remains the direct Alpine path and links back to shared networking.
