# Installing Arch Linux with LUKS, Btrfs, UKI and rEFInd

## 1. What we are building

The final storage and boot structure will be:

```text
UEFI firmware
└── rEFInd boot manager
    └── arch-linux.efi unified kernel image
        └── unlocks the LUKS2 container
            └── mounts the Btrfs @ subvolume as /
```

The disk itself will look like this:

```text
Disk
├── Partition 1: FAT32 EFI System Partition, mounted at /efi
│   ├── EFI/refind/...
│   └── EFI/Linux/arch-linux.efi
│
└── Partition 2: LUKS2 encrypted container
    └── Btrfs filesystem
        ├── @           → /
        ├── @home       → /home
        ├── @snapshots  → /.snapshots
        ├── @var_log    → /var/log
        └── @pkg        → /var/cache/pacman/pkg
```

### What each component does

| Component  | Its job                                                                          |
| ---------- | -------------------------------------------------------------------------------- |
| **UEFI**   | The computer firmware that starts EFI programs                                   |
| **ESP**    | A small, unencrypted FAT32 partition readable by UEFI                            |
| **rEFInd** | Displays the boot menu and launches the Arch UKI                                 |
| **UKI**    | One EFI file containing the kernel, initramfs, microcode and kernel command line |
| **LUKS2**  | Encrypts the Linux partition at the block-device level                           |
| **Btrfs**  | Stores files and provides subvolumes, compression and snapshots                  |

A UKI is an EFI executable containing the components normally stored as separate kernel, initramfs and command-line files. rEFInd is a **boot manager**: it discovers or is configured to launch EFI executables. It does not need to understand the encrypted Btrfs filesystem because the completed UKI is stored on the FAT32 ESP.

## 2. Why Btrfs instead of LVM

The referenced LVM-on-LUKS arrangement normally looks like this:

```text
LUKS
└── LVM volume group
    ├── root logical volume
    ├── home logical volume
    └── swap logical volume
```

This guide instead uses:

```text
LUKS
└── Btrfs
    ├── root subvolume
    ├── home subvolume
    └── other subvolumes
```

Both solve some of the same storage-management problems, but at different levels:

* LVM creates resizable virtual block devices called logical volumes.
* Btrfs subvolumes are filesystem-level divisions that share the same pool of free space.
* Btrfs also supplies copy-on-write snapshots and transparent compression.
* Subvolumes do not need fixed sizes in advance.

Putting LVM between LUKS and Btrfs can be useful in specialized systems, but it is usually unnecessary for a desktop installation because Btrfs already provides flexible storage management through subvolumes and snapshots. A more useful comparison is:

```text
LUKS
├── LVM
│   ├── ext4 logical volume → /
│   └── ext4 logical volume → /home
│
└── Btrfs filesystem
    ├── @        → /
    ├── @home    → /home
    └── snapshots, etc.
```

LVM with ext4 is a traditional and very stable approach:

* LVM provides flexible partition resizing and separate logical volumes.
* ext4 is a mature, simple filesystem with predictable behavior.
* Snapshots require additional tools such as LVM snapshots, which are block-level and less space-efficient for frequent desktop snapshots.

Btrfs provides many of the same management features at the filesystem level:

* Subvolumes replace many use cases for separate partitions or logical volumes.
* Copy-on-write snapshots are fast and space-efficient.
* Compression and filesystem-level features are built in.

Mixing LVM and Btrfs is not inherently impossible, but it combines two layers that solve overlapping problems:

```text
LUKS
└── LVM
    └── Btrfs
        └── subvolumes
```

This adds complexity when troubleshooting, recovering, resizing, or explaining the storage layout. It can also make it harder to understand which layer is responsible for a problem. For most Arch desktop installations, choose one storage-management approach:

* LUKS → LVM → ext4 if you prefer traditional block-device management.
* LUKS → Btrfs if you want subvolumes, compression and snapshots.

This guide therefore uses Btrfs directly inside LUKS and does not install or add the `lvm2` initramfs hook. The LVM guide is only conceptual background.

## 3. Scope and assumptions

This guide assumes:

* An x86-64 computer booted in UEFI mode.
* The entire selected disk may be erased.
* Secure Boot is disabled for the initial installation.
* Arch will use the whole disk.
* The example disk is `/dev/nvme0n1`.
* The timezone is `Europe/Amsterdam`.
* The initial system is a command-line installation.
* No swap or hibernation is configured yet.

Btrfs swap files require special no-copy-on-write handling, and a subvolume containing an active swap file cannot be snapshotted normally. It is safer to add swap or hibernation after the base system boots successfully.

> **Destructive-operation warning:** the partitioning commands below erase the selected disk. Verify the disk name by its size and model. Do not blindly assume that your disk is `/dev/nvme0n1`.

> **Command convention:** the examples use direct device paths rather than shell variables. This is more repetitive, but it makes each destructive command easier to read and verify. Replace `/dev/nvme0n1`, `/dev/nvme0n1p1` and `/dev/nvme0n1p2` when your disk uses different names.

## 4. Boot the Arch installation medium

In the firmware settings:

1. Boot the Arch USB entry marked **UEFI**.
2. Temporarily disable Secure Boot.
3. Do not select a legacy or CSM boot option.

Check whether the live environment was started in UEFI mode:

```bash
ls /sys/firmware/efi
```

If the command displays files and directories, the system was booted in UEFI mode. If it reports that the directory does not exist, reboot and choose the UEFI entry for the installation USB. UKIs and rEFInd require UEFI.

Set the console keyboard layout when necessary:

```bash
loadkeys us
```

Replace `us` with the appropriate keymap when using another keyboard layout. You can list available layouts with:

```bash
localectl list-keymaps
```

Enable network time synchronization:

```bash
timedatectl set-ntp true
timedatectl status
```

For wired networking, DHCP should normally work automatically. Test the connection:

```bash
ping -c 3 archlinux.org
```

For Wi-Fi, start the interactive iwd client:

```bash
iwctl
```

Inside `iwctl`, enter:

```text
device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect YOUR_NETWORK_NAME
exit
```

Replace `wlan0` with the wireless device shown by `device list`. You will be prompted for the Wi-Fi password when required.

## 5. Identify the correct disk

Display the available disks and partitions:

```bash
lsblk
```

Use the sizes in the output to identify the disk that will contain Arch Linux. Common names are:

```text
NVMe disk: /dev/nvme0n1
Its partitions: /dev/nvme0n1p1, /dev/nvme0n1p2, ...

SATA or USB disk: /dev/sda
Its partitions: /dev/sda1, /dev/sda2, ...
```

This guide uses `/dev/nvme0n1` as the example installation disk. Every command below therefore uses:

```text
EFI System Partition: /dev/nvme0n1p1
Encrypted partition:  /dev/nvme0n1p2
```

When your disk is named differently, replace these paths carefully in every command. For example, a SATA installation might use `/dev/sda`, `/dev/sda1` and `/dev/sda2`.

> Run `lsblk` again immediately before partitioning. Confirm the disk by its size. Selecting the wrong disk will destroy data on that disk.

## 6. Partition the disk

We will create:

- A 1 GiB EFI System Partition.
- One Linux LUKS partition using the remaining space.

Open the interactive partition editor for the example disk:

```bash
cfdisk /dev/nvme0n1
```

If `cfdisk` asks for a partition-table type, choose **gpt**.

Use the arrow keys and the options shown at the bottom of the screen:

1. Select each existing partition and choose **Delete** until only free space remains.
2. Select the free space and choose **New**.
3. Enter `1G` as the size.
4. Select the new 1 GiB partition, choose **Type**, and select **EFI System**.
5. Select the remaining free space and choose **New**. Accept the suggested size so it uses the rest of the disk.
6. Select the second partition, choose **Type**, and select **Linux LUKS**.
7. Choose **Write**, type `yes`, and press Enter.
8. Choose **Quit**.

The **Write** step is the point at which the partition table is actually changed.

Check the result:

```bash
lsblk
```

For the example NVMe disk, you should now see `/dev/nvme0n1p1` and `/dev/nvme0n1p2`. The partition type describes the intended use; encryption itself is created in the next section.

## 7. Format the ESP and create the LUKS container

Format the first partition as FAT32 for use as the EFI System Partition:

```bash
mkfs.fat -F 32 -n EFI /dev/nvme0n1p1
```

Create a LUKS2 container on the second partition:

```bash
cryptsetup luksFormat --type luks2 /dev/nvme0n1p2
```

Type the uppercase confirmation requested by `cryptsetup`, then choose a strong encryption passphrase.

Use a passphrase that you can enter reliably with the keyboard layout available during early boot. Losing every valid LUKS passphrase means losing access to the encrypted data.

Open the encrypted container and name the unlocked mapping `cryptroot`:

```bash
cryptsetup open /dev/nvme0n1p2 cryptroot
```

Enter the LUKS passphrase. The unlocked storage is now available at:

```text
/dev/mapper/cryptroot
```

Check it with:

```bash
lsblk
```

You should see `cryptroot` beneath the second partition.

## 8. Create Btrfs and its subvolumes

Create the filesystem:

```bash
mkfs.btrfs -L archroot /dev/mapper/cryptroot
```

Temporarily mount its top level:

```bash
mount /dev/mapper/cryptroot /mnt
```

Create the subvolumes:

```bash
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@snapshots
btrfs subvolume create /mnt/@var_log
btrfs subvolume create /mnt/@pkg
```

Inspect them:

```bash
btrfs subvolume list /mnt
```

Unmount the top level:

```bash
umount /mnt
```

### Why use separate subvolumes?

A snapshot of `@` will represent the root system but will not recursively include nested subvolumes such as `@home`, `@var_log` or `@pkg`.

That is useful because:

* User files can be managed separately from system snapshots.
* Logs keep recording events after a root rollback.
* The package cache does not bloat every root snapshot.
* Snapshots themselves are not nested inside snapshots of `/`.

Creating `@snapshots` does **not** automatically create snapshots. It only prepares a suitable location for a later tool such as Snapper or for manual Btrfs snapshots. Btrfs subvolumes share the filesystem’s free space and can be snapshotted independently.

## 9. Mount the installation filesystem

Mount the root subvolume with Btrfs compression enabled:

```bash
mount -o noatime,compress=zstd:3,subvol=@ /dev/mapper/cryptroot /mnt
```

Create the directories that will become mount points:

```bash
mkdir -p /mnt/home
mkdir -p /mnt/.snapshots
mkdir -p /mnt/var/log
mkdir -p /mnt/var/cache/pacman/pkg
mkdir -p /mnt/efi
```

Mount each remaining subvolume:

```bash
mount -o noatime,compress=zstd:3,subvol=@home /dev/mapper/cryptroot /mnt/home
mount -o noatime,compress=zstd:3,subvol=@snapshots /dev/mapper/cryptroot /mnt/.snapshots
mount -o noatime,compress=zstd:3,subvol=@var_log /dev/mapper/cryptroot /mnt/var/log
mount -o noatime,compress=zstd:3,subvol=@pkg /dev/mapper/cryptroot /mnt/var/cache/pacman/pkg
```

Mount the EFI System Partition:

```bash
mount /dev/nvme0n1p1 /mnt/efi
```

Verify the complete layout:

```bash
findmnt -R /mnt
```

Check that `/mnt`, `/mnt/home`, `/mnt/.snapshots`, `/mnt/var/log`, `/mnt/var/cache/pacman/pkg` and `/mnt/efi` are all present.

`compress=zstd:3` enables transparent Zstandard compression at a moderate level. `noatime` avoids updating a file-access timestamp on ordinary reads. Using the same options for each Btrfs subvolume makes the layout easier to understand.

This guide does not explicitly enable discard passthrough through LUKS. TRIM can be useful on SSDs, but it should be considered separately because it has both hardware and privacy implications.

## 10. Install the base system

Install Arch, the storage and boot tools, networking, documentation and the `nano` editor:

```bash
pacstrap -K /mnt base linux linux-firmware btrfs-progs cryptsetup mkinitcpio systemd-ukify refind efibootmgr networkmanager sudo nano man-db man-pages texinfo tealdeer wikiman arch-wiki-docs
```

`systemd-ukify` provides a UKI-building backend. The offline documentation packages will be useful later when no browser or video guide is available.

Generate the filesystem table:

```bash
genfstab -U /mnt > /mnt/etc/fstab
```

Open it for inspection:

```bash
nano /mnt/etc/fstab
```

In `nano`:

- Use the arrow keys to move.
- Press `Ctrl+O`, then Enter, to save.
- Press `Ctrl+X` to exit.
- When only inspecting a file, press `Ctrl+X` and choose not to save.

The file should contain mount entries for:

```text
/
/home
/.snapshots
/var/log
/var/cache/pacman/pkg
/efi
```

Do not edit the generated UUIDs unless you know they are wrong.

Enter the installed system:

```bash
arch-chroot /mnt
```

Commands from this point run inside the new Arch installation.

## 11. Install CPU microcode

Display CPU information:

```bash
lscpu
```

Look at the **Vendor ID** line:

- `GenuineIntel` means Intel.
- `AuthenticAMD` means AMD.

For an Intel CPU, install:

```bash
pacman -S intel-ucode
```

For an AMD CPU, install:

```bash
pacman -S amd-ucode
```

Install only the package that matches the computer's CPU. The `microcode` mkinitcpio hook used later will include it in the boot image.

## 12. Configure timezone, locale and hostname

Set the timezone and hardware clock:

```bash
ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
hwclock --systohc
```

Open the locale list:

```bash
nano /etc/locale.gen
```

Find this line and remove the `#` from its beginning:

```text
en_US.UTF-8 UTF-8
```

Save with `Ctrl+O`, press Enter, and exit with `Ctrl+X`. Then generate the selected locale:

```bash
locale-gen
```

Create the locale configuration:

```bash
nano /etc/locale.conf
```

Enter:

```text
LANG=en_US.UTF-8
```

Save and exit.

Configure the keyboard layout used during early boot:

```bash
nano /etc/vconsole.conf
```

For a US keyboard, enter:

```text
KEYMAP=us
```

Save and exit. Use the same keymap that you tested in the live environment.

Choose a hostname for the computer. This guide uses `archbox`:

```bash
nano /etc/hostname
```

Enter only:

```text
archbox
```

Save and exit. You may choose another simple hostname without spaces.

Configure local hostname resolution:

```bash
nano /etc/hosts
```

Enter:

```text
127.0.0.1 localhost
::1       localhost
127.0.1.1 archbox.localdomain archbox
```

When you chose another hostname, replace both occurrences of `archbox`. Save and exit.

Set the root password:

```bash
passwd
```

## 13. Create a normal user

Replace `alice` with the username you want to use:

```bash
useradd -m -G wheel -s /bin/bash alice
passwd alice
```

The first command creates the home directory and adds the user to the administrative `wheel` group. The second command sets that user's password.

Open the sudo configuration safely with `visudo`, using `nano` as the editor:

```bash
EDITOR=nano visudo
```

Find this line:

```text
# %wheel ALL=(ALL:ALL) ALL
```

Remove the leading `#` so it becomes:

```text
%wheel ALL=(ALL:ALL) ALL
```

Save and exit. `visudo` checks the syntax before accepting the file, which is safer than editing `/etc/sudoers` directly.

Enable networking and time synchronization at boot:

```bash
systemctl enable NetworkManager
systemctl enable systemd-timesyncd
```

## 14. Configure the encrypted initramfs

Open the mkinitcpio configuration:

```bash
nano /etc/mkinitcpio.conf
```

Find the line beginning with `HOOKS=` and replace it with:

```bash
HOOKS=(base systemd autodetect microcode modconf kms keyboard sd-vconsole block sd-encrypt filesystems fsck)
```

Important details:

* `systemd` selects the systemd-based initramfs.
* `sd-encrypt` unlocks LUKS devices in that environment.
* `keyboard` and `sd-vconsole` make the keyboard layout available before root is unlocked.
* `microcode` embeds the installed Intel or AMD microcode.
* There is deliberately **no `lvm2` hook**.
* Do not combine the `systemd`/`sd-encrypt` arrangement with the alternative `udev`/`encrypt` arrangement.

The Arch dm-crypt documentation uses `sd-encrypt` for systemd-based encrypted-root setups. Its LVM-on-LUKS example contains an additional `lvm2` hook; removing that hook is the essential change for our direct Btrfs-on-LUKS design.

## 15. Create the embedded kernel command line

The UKI needs to know:

1. Which LUKS container to unlock.
2. What name to give the unlocked device.
3. Which device contains `/`.
4. Which Btrfs subvolume is `/`.

Display the **LUKS container UUID**:

```bash
cryptsetup luksUUID /dev/nvme0n1p2
```

Write the UUID down or keep it visible. It will look similar to:

```text
11111111-2222-3333-4444-555555555555
```

Open the kernel command-line file:

```bash
nano /etc/kernel/cmdline
```

Enter the following as **one line**, replacing the example UUID with the value printed by `cryptsetup`:

```text
rd.luks.name=11111111-2222-3333-4444-555555555555=cryptroot root=/dev/mapper/cryptroot rootflags=subvol=@ rw
```

Save and exit.

Use the UUID reported by `cryptsetup luksUUID`. Do not use:

- The Btrfs filesystem UUID.
- The FAT32 EFI partition UUID.
- A filesystem label.

`rd.luks.name=<LUKS UUID>=cryptroot` tells the systemd-based initramfs to unlock that LUKS container and expose it as `/dev/mapper/cryptroot`. `rootflags=subvol=@` selects the Btrfs root subvolume.

## 16. Configure mkinitcpio to produce a UKI

Create the standard directory for Linux UKIs on the EFI System Partition:

```bash
mkdir -p /efi/EFI/Linux
```

Open the preset created by the kernel package:

```bash
nano /etc/mkinitcpio.d/linux.preset
```

Preset formats can change. Keep the existing `ALL_kver` value and existing preset names, and modify only the output settings described below.

### Typical default-only preset

A default-only configuration should contain the equivalent of:

```bash
ALL_kver="/boot/vmlinuz-linux"

PRESETS=('default')

default_uki="/efi/EFI/Linux/arch-linux.efi"
```

Comment out the old separate-initramfs output by placing `#` at the beginning of its line:

```bash
#default_image="/boot/initramfs-linux.img"
```

### When the generated file contains a fallback preset

Keep the fallback preset and configure both UKI outputs:

```bash
ALL_kver="/boot/vmlinuz-linux"

PRESETS=('default' 'fallback')

default_uki="/efi/EFI/Linux/arch-linux.efi"

fallback_uki="/efi/EFI/Linux/arch-linux-fallback.efi"
fallback_options="-S autodetect"
```

Comment out both old image outputs:

```bash
#default_image="/boot/initramfs-linux.img"
#fallback_image="/boot/initramfs-linux-fallback.img"
```

Do not add a fallback preset when the original file does not contain one. A single default UKI is sufficient for the first boot.

Save the preset and exit `nano`. Then build the UKI:

```bash
mkinitcpio -p linux
```

Read the output carefully. Resolve any reported error before rebooting.

Check that the UKI exists:

```bash
ls -lh /efi/EFI/Linux
```

Identify it:

```bash
bootctl kernel-identify /efi/EFI/Linux/arch-linux.efi
```

It should be recognized as a unified kernel image. The UKI now contains the kernel, initramfs, microcode and the command line from `/etc/kernel/cmdline`.

## 17. Install rEFInd

Install rEFInd to the mounted EFI System Partition:

```bash
refind-install --nodrivers
```

`refind-install` normally copies rEFInd below `/efi/EFI/refind` and creates a UEFI boot entry. The `--nodrivers` option skips extra filesystem drivers because both rEFInd and the UKI are stored on the FAT32 EFI partition. rEFInd does not need to read the encrypted Btrfs filesystem.

Inspect the EFI directory:

```bash
ls -R /efi/EFI
```

Inspect the firmware boot entries:

```bash
efibootmgr
```

You should see an entry for rEFInd.

### Optional Arch icon

Copy rEFInd's Arch icon beside the UKI:

```bash
cp /usr/share/refind/icons/os_arch.png /efi/EFI/Linux/arch-linux.png
```

The icon and UKI now have matching names:

```text
arch-linux.efi
arch-linux.png
```

rEFInd can use the matching image for the discovered Arch entry.

### Manual menu entry only when automatic detection fails

rEFInd should normally discover an EFI executable stored in `EFI/Linux`. Do not add a manual entry unless Arch is missing from the menu.

When a manual entry is necessary, open:

```bash
nano /efi/EFI/refind/refind.conf
```

Add this block near the end of the file:

```text
menuentry "Arch Linux" {
    icon /EFI/Linux/arch-linux.png
    loader /EFI/Linux/arch-linux.efi
}
```

Save and exit. Do not add an `initrd` line or repeat the kernel options: both are already embedded in the UKI.

## 18. Final checks before rebooting

Confirm that the EFI System Partition is mounted at `/efi`:

```bash
findmnt /efi
```

Open the embedded command line and check the UUID, mapper name and Btrfs subvolume:

```bash
nano /etc/kernel/cmdline
```

Exit without saving when it is correct.

Open the mkinitcpio configuration and confirm that the `HOOKS=` line contains `systemd` and `sd-encrypt`, but not `lvm2`:

```bash
nano /etc/mkinitcpio.conf
```

Confirm that the UKI exists and is recognized:

```bash
ls -lh /efi/EFI/Linux/arch-linux.efi
bootctl kernel-identify /efi/EFI/Linux/arch-linux.efi
```

Confirm that rEFInd is installed and has a firmware entry:

```bash
ls /efi/EFI/refind
efibootmgr
```

Review the filesystem table one last time:

```bash
nano /etc/fstab
```

A common mistake is generating the UKI while `/efi` is not mounted. The UKI must exist on the actual FAT32 EFI System Partition, not in an ordinary empty `/efi` directory on the encrypted root filesystem.

Exit the chroot:

```bash
exit
```

Unmount the installed system:

```bash
umount -R /mnt
```

Close the encrypted mapping:

```bash
cryptsetup close cryptroot
```

Reboot:

```bash
reboot
```

Remove the installation USB when the firmware starts again.

## 19. First boot

The expected sequence is:

1. Firmware starts rEFInd.
2. rEFInd shows an Arch Linux entry.
3. rEFInd launches `arch-linux.efi`.
4. The UKI initializes the early userspace.
5. You are asked for the LUKS passphrase.
6. `/dev/mapper/cryptroot` is created.
7. Btrfs subvolume `@` becomes `/`.
8. Arch reaches the login prompt.

Log in as the normal user, not as root.

For Wi-Fi, use:

```bash
nmtui
```

Or list available networks with:

```bash
nmcli device wifi list
```

## 20. Offline help: tealdeer, wikiman and ArchWiki docs

Video guides are convenient, but they are poor recovery tools when the computer has no working browser or internet connection. Local documentation remains available from a terminal.

### tealdeer

`tealdeer` provides the `tldr` command: short, example-oriented summaries of common commands.

While the new installation has internet access, log in as the normal user and download the page cache:

```bash
tldr --update
```

You can then read cached examples offline:

```bash
tldr cryptsetup
tldr mount
tldr btrfs
tldr mkinitcpio
tldr efibootmgr
```

Run `tldr --update` once for each user who needs a local cache. Updating requires internet access; reading already cached pages does not.

### wikiman and arch-wiki-docs

`arch-wiki-docs` installs a local HTML copy of ArchWiki articles. `wikiman` provides a terminal interface for searching installed manual pages and documentation sources.

Start the interactive interface with:

```bash
wikiman
```

You can also request a topic directly:

```bash
wikiman btrfs
wikiman dm-crypt
wikiman mkinitcpio
wikiman refind
```

The offline ArchWiki HTML files are stored below:

```text
/usr/share/doc/arch-wiki/html/en/
```

List that directory when you need to inspect the files directly:

```bash
ls /usr/share/doc/arch-wiki/html/en
```

Traditional manual pages are also available offline:

```bash
man cryptsetup
man crypttab
man btrfs
man btrfs-subvolume
man mkinitcpio
man refind-install
man efibootmgr
```

Use `tldr` for quick examples, `man` for exact command documentation, and `wikiman` with `arch-wiki-docs` for longer Arch-specific explanations.

## 21. Recovery from the Arch USB

Keep an Arch installation USB available. It is both an installer and a recovery environment.

Boot it in UEFI mode and unlock the root partition:

```bash
cryptsetup open /dev/nvme0n1p2 cryptroot
```

Mount the root subvolume:

```bash
mount -o subvol=@ /dev/mapper/cryptroot /mnt
```

Mount the ESP:

```bash
mount /dev/nvme0n1p1 /mnt/efi
```

Enter the installation:

```bash
arch-chroot /mnt
```

Rebuild the UKI:

```bash
findmnt /efi
mkinitcpio -p linux
```

Reinstall rEFInd when necessary:

```bash
refind-install --nodrivers
```

Exit and cleanly unmount:

```bash
exit
umount -R /mnt
cryptsetup close cryptroot
reboot
```

## 22. Common problems

### No rEFInd menu

Check in the firmware setup whether an rEFInd entry exists. From the live environment, mount and enter the installation, then run:

```bash
refind-install --nodrivers
efibootmgr
```

Some firmware implementations forget or ignore NVRAM entries. That is a firmware-specific problem rather than a Btrfs or LUKS problem.

### rEFInd appears, but Arch does not

Verify:

```bash
ls -lh /efi/EFI/Linux/
```

The following file must exist on the mounted ESP:

```text
/efi/EFI/Linux/arch-linux.efi
```

Rebuild it:

```bash
mkinitcpio -p linux
```

Use the manual rEFInd stanza only after confirming the UKI itself exists and is valid.

### No passphrase prompt

Open the mkinitcpio configuration:

```bash
nano /etc/mkinitcpio.conf
```

Check the `HOOKS=` line. It must include `systemd`, `keyboard`, `sd-vconsole`, `block` and `sd-encrypt`. It must not include `lvm2` for this layout.

Save only when you make a correction, then rebuild the UKI:

```bash
mkinitcpio -p linux
```

### Passphrase is accepted, but root cannot be mounted

Open the command-line file:

```bash
nano /etc/kernel/cmdline
```

Exit without saving unless you need to correct it.

Frequent errors include:

* Using the Btrfs UUID instead of the LUKS UUID.
* A mapper name other than `cryptroot`.
* Missing `rootflags=subvol=@`.
* Typing the partition UUID incorrectly.

Display the correct LUKS UUID again:

```bash
cryptsetup luksUUID /dev/nvme0n1p2
```

Open the command-line file:

```bash
nano /etc/kernel/cmdline
```

Correct the UUID while keeping the complete command line on one line:

```text
rd.luks.name=YOUR-LUKS-UUID=cryptroot root=/dev/mapper/cryptroot rootflags=subvol=@ rw
```

Save, exit and rebuild the UKI:

```bash
mkinitcpio -p linux
```

### The UKI works until a kernel update

Check whether the ESP is mounted:

```bash
findmnt /efi
```

Then rebuild:

```bash
sudo mkinitcpio -p linux
```

Once the preset is configured correctly, normal kernel package hooks should regenerate the UKI. The ESP must be mounted at `/efi` when this happens.

### A Btrfs snapshot does not contain `/home`

That is intentional. `@home` is a separate nested subvolume and is not included recursively in a snapshot of `@`. Snapshot it separately when home-directory snapshots are desired.

## 23. Security limitations

This setup encrypts the Btrfs filesystem at rest, including `/boot`, user data, logs and the package cache.

The ESP remains unencrypted because the firmware must read it before LUKS can be opened. It contains:

* rEFInd.
* The UKI.
* The embedded kernel command line.
* Optionally an icon.

LUKS protects confidentiality of the encrypted partition. By itself, it does not prove that the unencrypted rEFInd or UKI files have not been modified.

Secure Boot can add boot-chain verification, but doing it correctly requires signing and trusting both rEFInd and every regenerated UKI. That should be configured as a separate step after the unsigned installation boots reliably.

## 24. Back up the LUKS header

A damaged LUKS header can make otherwise intact encrypted data inaccessible. Create a header backup:

```bash
sudo cryptsetup luksHeaderBackup /dev/nvme0n1p2 --header-backup-file luks-header.img
```

Move `luks-header.img` to secure storage on another physical device. Do not leave the only backup on the encrypted disk it is supposed to protect.

Treat the backup as security-sensitive. An old header backup may preserve older keyslots, so removing or changing a passphrase on the live header does not necessarily invalidate copies of an earlier header.

## 25. Mental model to remember

When troubleshooting, work through the layers in order:

```text
Can the firmware start rEFInd?
        ↓
Can rEFInd find and launch the UKI?
        ↓
Does the UKI contain the right kernel command line?
        ↓
Does sd-encrypt unlock the correct LUKS UUID?
        ↓
Does /dev/mapper/cryptroot appear?
        ↓
Can Btrfs mount subvolume @ as /?
        ↓
Can systemd start the installed system?
```

Do not randomly reformat or reinstall when one layer fails. Determine the first layer that does not work and repair only that layer.
