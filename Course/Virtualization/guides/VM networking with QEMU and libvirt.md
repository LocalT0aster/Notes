---
title: "VM networking with QEMU and libvirt"
topics:
  - "QEMU user networking"
  - "SSH port forwarding"
  - "libvirt bridge networking"
  - "systemd-networkd"
tags:
  - virtualization
  - virtual-machines
  - qemu
  - libvirt
  - networking
source:
  - "2026-04-11 Compose profiles and VM intro.md"
  - "2026-04-25 Debian image hardening and libvirt networking.md"
---

# VM networking with QEMU and libvirt

Use this note after the VM boots. The bootloader branch does not matter here: GRUB, UKI, Alpine, and Arch all end up with a guest network interface connected to some host-side backend.

## Branch 1: QEMU user-mode NAT

This is the simplest manual QEMU mode:

```bash
-nic user,model=virtio-net-pci
```

It gives the VM:

- outbound internet access through host NAT
- a virtual DHCP server
- no direct inbound access from the host or LAN

For SSH into the VM, forward a host port to guest port `22`:

```bash
-nic user,model=virtio-net-pci,hostfwd=tcp::2222-:22
```

Then connect from the host:

```bash
ssh -p 2222 preseed@127.0.0.1
```

## Branch 2: virt-manager bridge

Use this when the VM should appear directly on the class/LAN network.

On the hypervisor, the bridge already has to exist:

```bash
ip a show br0
bridge link
```

In virt-manager:

1. Shut down the VM.
2. Open the VM details view.
3. Select the NIC or add a new `Network` device.
4. Set source to `Bridge device`.
5. Set bridge name to `br0`.
6. Set model to `virtio`.
7. Apply and boot the VM.

Do not configure `br0` inside the guest. `br0` is the host-side bridge. The guest sees a normal virtual Ethernet interface such as `ens3`, `enp1s0`, or `eth0`.

Many students can attach VMs to the same host `br0`. They collide only if they reuse the same static IP, manually duplicate a MAC address, or fight over the same VM/libvirt object names.

Avoid `macvtap` for the course workflow unless explicitly required; it commonly prevents host-to-guest communication.

## Arch guest DHCP

For Arch, use `systemd-networkd`.

Create:

```bash
sudo nano /etc/systemd/network/20-wired.network
```

Prefer matching real Ethernet devices instead of guessing the interface name:

```ini
[Match]
Type=ether

[Network]
DHCP=yes
```

Enable DNS and networking:

```bash
sudo systemctl enable --now systemd-networkd
sudo systemctl enable --now systemd-resolved
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

Verify:

```bash
networkctl
ip -br addr
ip route
resolvectl status
ping -c 3 1.1.1.1
ping -c 3 archlinux.org
```

## Alpine guest DHCP

For Alpine, `/etc/network/interfaces` should contain:

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

Verify:

```bash
ip a show eth0
ip route
ping -c 3 1.1.1.1
ping -c 3 alpine.org
```

## Static IP on a bridge

An address such as `172.30.44.78/24` does not prove the setup is static. If the guest config uses DHCP, the DHCP server may simply be reusing the same lease.

Check current state:

```bash
networkctl status
ip route | grep default
resolvectl status
```

Only make an address static if it is assigned to you or outside the DHCP pool.

Arch static example:

```ini
[Match]
Type=ether

[Network]
Address=172.30.44.78/24
Gateway=172.30.44.1
DNS=172.30.44.1
DNS=8.8.8.8
```

Restart networkd:

```bash
sudo systemctl restart systemd-networkd
```

Do not guess the gateway. Use the gateway shown by the DHCP configuration before switching to static:

```bash
ip route | grep default
```

## SSH service in the guest

Arch:

```bash
sudo pacman -S openssh
sudo systemctl enable --now sshd
```

Alpine:

```bash
apk update
apk add openssh
rc-update add sshd default
rc-service sshd start
```

Create a normal user and prefer SSH keys for real use.
