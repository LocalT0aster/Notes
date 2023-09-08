# How to create a Virtual Machine (VM) in VirtualBox

## Step 1: Have [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed

## Step 2: Choose and download the distro image

I will be using [`lubuntu`](https://lubuntu.me) (Lightweight Ubuntu) for this purpose. But you can install any distro that you want (I will be using `apt` in the lab 1 preparation, so I reccomend you to use the Debian based ones)

Follow [this page](https://manual.lubuntu.me/stable/1/1.1/retrieving_the_image.html) if you are unsure of what version do you need.

## Step 3: Create the virtual machine

Launch the VirtualBox on your host machine, and follow:

![New VM](img/vminst0.jpg)
![Name, Folder, and Image config](img/vminst1.jpg)
![RAM & CPU cofig](img/vminst2.jpg)
![VHD config](img/vminst3.jpg)
![Checkout](img/vminst4.jpg)
Also, you can additionally increase the video memory and enable 3D acceleration for your VM:
![Additional Setting](img/vminst5.jpg)
![enable VMem & 3D acceleration](img/vminst6.jpg)

## Step 4: Launch the VM
Select the VM and press `Start` button

## Step 5: Installing the OS
Follow [this guide](https://manual.lubuntu.me/stable/1/1.3/installation.html) if you are installing `lubuntu`, and if you are using other distro, just search for `[your distro name] installation`.
### End of the guide
# [<- Return](Lab1Solution.md)