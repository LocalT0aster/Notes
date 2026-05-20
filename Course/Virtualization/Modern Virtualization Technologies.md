---
title: "Modern Virtualization Technologies"
tags:
  - virtualization
  - course-notes
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Modern Virtualization Technologies

Split and cleaned from the original Etherpad HTML dump. Each lecture note keeps the source wording where possible and normalizes formatting for Obsidian/GFM Markdown.

## Lectures

- [[lectures/2026-02-07 Namespaces and chroot|2026-02-07 - Namespaces and chroot]] - Linux namespaces, debootstrap, chroot
- [[lectures/2026-02-14 Network namespaces and Docker basics|2026-02-14 - Network namespaces and Docker basics]] - mount namespace recap, network namespaces, veth
- [[lectures/2026-02-21 Docker ports, processes, and images|2026-02-21 - Docker ports, processes, and images]] - Docker port forwarding, docker-proxy, GUI applications in containers
- [[lectures/2026-02-28 Docker Compose and LXC intro|2026-02-28 - Docker Compose and LXC intro]] - Docker cleanup, Docker Compose, container networking
- [[lectures/2026-03-07 Docker networks and LXC rootfs|2026-03-07 - Docker networks and LXC rootfs]] - Docker networks, LXC containers, root filesystem
- [[lectures/2026-03-14 LXC snapshots and LVM|2026-03-14 - LXC snapshots and LVM]] - lxc-copy, LXC configuration, LVM snapshots
- [[lectures/2026-03-21 Resources, cgroups, LXD and Incus|2026-03-21 - Resources, cgroups, LXD and Incus]] - resource limits, cgroups, LXD
- [[lectures/2026-03-28 Docker images and Flask app|2026-03-28 - Docker images and Flask app]] - container image lifecycle, Dockerfile basics, static site image
- [[lectures/2026-04-04 Dockerfile, users, compose, postgres|2026-04-04 - Dockerfile, users, compose, postgres]] - base images, non-root container users, Docker builders
- [[lectures/2026-04-11 Compose profiles and VM intro|2026-04-11 - Compose profiles and VM intro]] - Compose variables, Compose profiles, virtual machines
- [[lectures/2026-04-18 Virt-manager, LVM images, virsh|2026-04-18 - Virt-manager, LVM images, virsh]] - virt-manager, Astra VM installation, LVM-backed images
- [[lectures/2026-04-25 Debian image hardening and libvirt networking|2026-04-25 - Debian image hardening and libvirt networking]] - Debian image hardening, systemd-networkd, systemd-resolved

## Guides

- [[guides/Alpine VM with LVM and networking|Alpine VM with LVM and networking]] - QEMU setup with an LVM-backed disk and user-mode DHCP/NAT networking
- [[guides/Arch VM with LVM and networking|Arch VM with LVM and networking]] - QEMU setup with an LVM-backed disk, GRUB, and persistent DHCP networking

## Source

- `r.2ea786f27b6b7f389b7fafc70c47bcec.html`
