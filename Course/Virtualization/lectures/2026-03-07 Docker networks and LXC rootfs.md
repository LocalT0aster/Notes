---
title: "Mar 7 - Docker networks and LXC rootfs"
date: 2026-03-07
topics:
  - "Docker networks"
  - "LXC containers"
  - "root filesystem"
  - "LVM containers"
tags:
  - virtualization
  - containers
  - docker
  - lxc
  - lvm
source: "r.2ea786f27b6b7f389b7fafc70c47bcec.html"
---

# Mar 7 - Docker networks and LXC rootfs

## Homework (networks in Docker)

I would like to see the way of managing networks in pure Docker (without docker-compose)

```bash
docker network ls
docker network create project1
```

creates new network

53: br-efe6ea47b14d: `<NO-CARRIER,BROADCAST,MULTICAST,UP>` mtu 1500 qdisc noqueue state DOWN group default

link/ether 02:42:18:e1:b2:46 brd ff:ff:ff:ff:ff:ff

inet 172.23.0.1/16 brd 172.23.255.255 scope global br-efe6ea47b14d

valid_lft forever preferred_lft forever

we can see the bridge

```bash
docker inspect project1
```

more details about network

by default Docker uses 172.16.0.0/12

Docker allocates /16 per network, not a very good way

```bash
docker run --rm --net project1 -ti ubuntu:24.04
apt update
apt install iproute2
```

to have ip command

```bash
cat /etc/resolv.conf
```

nameserver 127.0.0.11

options ndots:0

all DNS requests, even without a dot, send to nameserver

I would like to manage IP addresses of containers

```bash
docker run --rm --name ubuntu --hostname ubuntu --net project1 --ip 172.23.0.15 -ti ubuntu:24.04
```

no luck - our network was created without subnet assignment, and we have to specify it

```bash
docker network rm project1
```

destroy the network

```bash
docker network create --subnet 192.168.10.0/24 project2
docker run --rm --name ubuntu --hostname ubuntu --net project2 --ip 192.168.10.11 -ti ubuntu:24.04
```

can we create one more network and run a container, attached to two networks?

```bash
docker network create --subnet 192.168.20.0/24 project3
docker network ls
docker create --name app --hostname app --net project2 --ip 192.168.10.21 --rm -ti alpine:3.23
```

we only create container, we don't run it yet

```bash
docker network connect --ip 192.168.20.21 project3 app
```

I do connect container to second network

```bash
docker inspect app
```

I can see two networks in the end of the output

```bash
docker start app
docker exec -ti app sh
ip a
```

shows me two network interfaces

```bash
ip r
```

we have both networks as routes (as expected)

default gateway will be from the first connected network

one more note about network connectivity

default docker configuration prohibits routing between docker networks. why? security matter

Chain FORWARD (policy DROP 0 packets, 0 bytes)

```c
if you would like two networks to be able to communicate with each other, you have to make a rule with it
```

most of the time you have to be a little bit tricky to manage your own set of rules along with Docker

Best advise: put your rules to DOCKER-USER chain to allow communication

Always use IP subnets for allowing traffic

sudo iptables -I FORWARD 1 -s 192.168.10.0/24 -d 192.168.20.0/24 -j ACCEPT

sudo iptables -I FORWARD 1 -s 192.168.20.0/24 -d 192.168.10.0/24 -j ACCEPT

right now I do insert them right to the FORWARD chain, but you can replace FORWARD with DOCKER-USER and have the same effect

Same task with Docker Compose is a lot easier:

```bash
cd
mkdir multinet
```

create a new file in Kate

```yaml
services:
```

one:

```yaml
image: alpine:3.23
```

restart: unless-stopped

command: sleep 3600

```yaml
networks:
```

first:

ipv4_address: 10.100.11.11

two:

```yaml
image: alpine:3.23
```

restart: unless-stopped

command: sleep 3600

```yaml
networks:
```

first:

ipv4_address: 10.100.11.12

second:

ipv4_address: 10.100.12.12

three:

```yaml
image: alpine:3.23
```

restart: unless-stopped

command: sleep 3600

```yaml
networks:
```

second:

ipv4_address: 10.100.12.13

```yaml
networks:
```

first:

driver: bridge

ipam:

config:

- subnet: 10.100.11.0/24

second:

driver: bridge

ipam:

config:

- subnet: 10.100.12.0/24

save the file to multinet directory with name docker-compose.yml

```bash
cd multinet
sudo docker-compose up -d
docker-compose exec two sh
ip a
ip r
```

## LXC

```bash
sudo apt install lxc lxc-astra
```

Let's take a look at the configuration (file layout)

Some parts of LXC are configured with environment variables, usually in Debian you have them in /etc/default

/etc/default/lxc - we have default settings here (generic, like autostart)

/etc/default/lxc-net - default configuration of the networking

Some settings are in

/etc/lxc/default.conf - these are defaults for a newly created container

LXC sets some kernel parameters

/etc/sysctl.d/30-lxc-inotify.conf

```c
if you would like to run a lot of containers, you have to do more tweaks here
```

LXC has some services at startup, but they are fire and forget. They start, do what they need and go away.

```bash
sudo systemctl status lxc-net
```

you can see dnsmasq running, as a result of the service

when you need logs of dnsmasq (or some detail about network init)

sudo journalctl -u lxc-net

lxc-net service ensures the default bridge is created (if you need it), assigns IP address, runs dnsmasq and then goes away.

```bash
sudo systemctl status lxc
```

Two more locations of interest:

/var/cache/lxc - all the downloaded files will be there

/var/lib/lxc - container files (configuration and rootfs) goes here

We have installed two packages: lxc and lxc-astra, why do we need second one?

dpkg -L lxc-astra

/usr/share/lxc/templates/lxc-astralinux-ce

/usr/share/lxc/templates/lxc-astralinux-se

this package brings templates for you to create LXC-container with Astra Linux inside

We do have dnsmasq running right now, but it is running only on lxcbr0 bridge.

dnsmasq does two things:

DNS resolver for containers

DHCP server

```bash
sudo systemctl cat lxc-net
```

it runs /usr/libexec/lxc/lxc-net with different parameters, it's just a script

it has all the defaults hardcoded

never ever edit /usr/libexec/lxc/lxc-net file, but put desired option to /etc/default/lxc-net

LXC does not have any Docker Hub or any Hub at all. Why?

Usually lifecycle of the LXC container is like this: you ask LXC to create a new container, it runs scripts from a template file and creates it.

```bash
sudo lxc-create -t ubuntu -n ubuntu1
```

this creates a new container

```bash
sudo lxc-ls -f
```

```bash
sudo -i
```

become root

```bash
cd /var/lib/lxc
ls -l
```

for each container we will have a dedicated directory here

```bash
cd ubuntu1
ls -l
```

we have a config file named config

rootfs directory - root filesystem of a container

we didn't ask for anything when we were creating a container, so LXC uses file mechanism by default

```bash
exit
sudo lxc-start -n ubuntu1
```

start the container

in the older times when you run lxc-start, you've been attached to it's output

oldfags would start it a litlle bit different

```bash
sudo lxc-start -n ubuntu1 -d
sudo lxc-ls -f
```

I see my container running, but no IP address yet

how can I jump in?

```bash
sudo lxc-attach -n ubuntu1
exit
```

let's go back

let's take a look at the namespaces

```bash
sudo lsns
```

let's try to fix DHCP

```bash
sudo lxc-attach -n ubuntu1
```

dhclient

run DHCP-client by hands and it works

```bash
exit
```

as soon as I have an IP-address, its routable, so I can do SSH

```bash
ssh -l ubuntu 10.0.3.X
```

no luck, no SSH server

```bash
sudo lxc-attach -n ubuntu1
sudo lxc-stop -n ubuntu1
```

it is not working

```bash
sudo lxc-stop -k -W -n ubuntu1
```

this will work and kill it fast

We do have some troubles with ubuntu, so let's switch to Astra and take a look at it

let's create Astra Linux container with LVM - let's have a logical volume for astra

to use LVM all we have to do is to provide LXC with the names of the volume group to create lv in

```bash
sudo vgs
```

we have a volume group called astra

```bash
sudo lxc-create -t astralinux-se --bdev lvm --vgname astra -n astra --fssize 4G
```

scripts in Astra templates usually use the /etc/apt/sources.list from the host, beware

```bash
sudo lvresize -L20G astra/root --resizefs
```

increase size of rootfs of our virtual machine

```bash
sudo lxc-ls -f
```

list the containers

```bash
sudo lxc-start -n astra
```

in a couple of seconds you can see astra having an IP-address assigned

```bash
ssh -l admin 10.0.3.X
```

password is astralinux

let's take a look

```bash
df -h
```

we can see 4GB filesystem

Docker: each container (if you leave it's rootfs as writeable) can do whatever it wants, and it's last writable layer will be stored in /var/lib/docker directory on the host. In most cases you do not have a separate mount there. So, any container is using rootfs of the host. You can easily run out of storage. overlayfs is a tricky debug beast.

LXC: when used with LVM backend, container cannot use more space that you've just allocated. if we need to increase the size of the rootfs of the container, we just resize the lv. LVM can perfectly do that.

one more thing to notice: LVM has a snapshot feature. it means, you can create a snapshot of a container at any moment. mind, that LVM uses copy-on-write method, so if you do a snapshot, then you slow the performance of the device. do not overuse that. create, copy, then delete.

I would like to install apache2 for example

```bash
sudo apt update
sudo apt install apache2
```

no luck here, because default configuration of the Docker sets FORWARD chain to drop

sudo iptables -P FORWARD ACCEPT

let's take a look at the config of the container

```bash
sudo -i
```

```bash
cd /var/lib/lxc
cd astra
cat config
# Template used to create this container: /usr/share/lxc/templates/lxc-astralinux-se
# Parameters passed to the template:
# For additional config options, please look at lxc.container.conf(5)

# Uncomment the following line to support nesting containers:
#lxc.include = /usr/share/lxc/config/nesting.conf
# (Be aware this has security implications)

lxc.net.0.type = veth
lxc.net.0.hwaddr = 00:16:3e:cb:b6:55
lxc.net.0.link = lxcbr0
lxc.net.0.flags = up
lxc.apparmor.profile = generated
lxc.apparmor.allow_nesting = 1
lxc.rootfs.path = lvm:/dev/astra/astra

# Common configuration
lxc.include = /usr/share/lxc/config/debian.common.conf

# Container specific configuration
lxc.tty.max = 1
lxc.pty.max = 1024
lxc.uts.name = astra
lxc.arch = amd64

lxc.mount.entry = /parsecfs parsecfs none bind 0 0
```

So, what can we say about network configuration?

1. we have veth adapter, as Docker and Podman do
2. we have a clean option - which bridge to use

LXC does not create anything but default bridge for you. you want another bridge? create it by youself.

3. we don't see here any configuration of the IP-address, but it is possible. we can assign IP-address to a container from the config

```bash
lxc.net.0.ipv4.address = X.X.X.X/24
lxc.net.0.ipv4.gateway = X.X.X.X
```

the trick is, that inside the container you may have any other network management (NM with any additional config) and it will override what you put into config

This line in config

```bash
lxc.mount.entry = /parsecfs parsecfs none bind 0 0
```

means "mount /parsecfs directory from the host to container /parsecfs"

Let's see all the options:

- let's assign an IP-address manually
- let's make a bind directory

```bash
mkdir /tmp/bindtest
```

create a directory

let's edit container config

```bash
sudo nano /var/lib/lxc/astra/config
```

after lxc.net.0.flags line, please add

```bash
lxc.net.0.ipv4.address = 10.0.3.11/24
lxc.mount.entry = /tmp/bindtest tmp/bindtest none bind,create=dir 0 0
```

I've added the create=dir option to create a target directory in a container

Ctrl+S, Ctrl+X

container is running right now, let's restart it

```bash
ping 10.0.3.11
ssh -l admin 10.0.3.X
df -h
```

host:

sudo chown 1000:1000 /tmp/bindtest

you should know who runs the container and which UID it uses

```c
if you have need to run a bunch of a similar containers, you can use LVM and thing called thinpool to create thin snapshots. thin snapshot holds only the difference from the origin.
```

Homework (if you would like to practice)

Try to create a copy of a container we've just created
