# OS Lab 1 Solution Script
## Preparing for the lab
If you do not have linux, you can read [How to Create a VM](HowToCreateAVM.md).

If you are using git for the first time on your machine, you should set your name and email for commits.
```bash
git config --global user.name "Your Name"
git config --global user.email youremail@example.com
```
Also it is required to have gcc installed to complete this lab. On Ubuntu/Debian distros you can do this by installing `build-essential` using `apt`:
```bash
sudo apt update && sudo apt install -y build-essential
```
If you use VSCode and Virtual Machine (VM) it's better to launch it on host and connect to vscode server, using `code tunnel` command. [[More info]](https://code.visualstudio.com/docs/remote/vscode-server)

## Useful commands and shortcuts
Copy and Paste in Linux Terminal is performed using `[Ctrl + Shift + C]` & `[Ctrl + Shift + V]`

You can navigate using:
* `cd` to change directories
* `ls` to show files in current folder
* `pwd` to show current folder path

## Git init

Create repo folder and init the git:

Copy & paste in the terminal. Also you might want to create separate folder for repos, before you create the repo.
```bash
mkdir OSLabs
cd OSLabs
git init
```

# Exercises:

## Exercise 1:
Copy & paste in the terminal (`Ctrl + Shift + V`)
```bash
echo "mkdir week01
cd week01 >> week01/ex1.sh
ls /usr/bin | grep gcc | sort -r | head -n 5 > ex1.txt" > week01/ex1.sh
cd week01 || true
chmod +x ex1.sh
.ex1.sh
```

## Exercise 2:
Next exercise depends on creativity. You need to do this on your own. I have followed [this tutorial](https://itsfoss.com/cowsay/) and played with the commands.

To hide/backup your previous bash history, you can type:
```bash
cd ~
cp .bash_history history_backup
history -cw
```

After playing with commands, you should put them to `ex2.txt` (you need to navigate to folder `week01` using `cd` before you do so):
```bash
history > ex2.txt
cat ex2.txt | cut -c 8- > ex2.sh
```

And don't forget to return your history back!
```bash
cd ~
rm .bash_history
mv history_backup .bash_history
history -r
```

## Exercise 3:
Navigate to `week01` folder using `cd`, and create `ex3.sh` file.
```bash
nano ex3.sh && chmod +x ex3.sh
```
Paste the following code `[Ctrl + Shift + V]`
```bash
#!/bin/bash
mkdir -p root
date & sleep 3
ls -latr / > root/root.txt
date & sleep 3
mkdir -p home
date & sleep 3
ls -latr "/home/${USER}" > home/home.txt
```
Then exit nano (`[Ctrl + X] -> [Y] -> [Enter]`) and run the script:
```bash
bash ex3.sh
```
You can remove files from folders using this script:
```bash
mv root/root.txt root.txt
mv home/home.txt home.txt
rm -rf root
rm -rf home
```

## Exercise 4:
Navigate to the `week01` and paste this code `[Ctrl + Shift + V]`
```bash
echo "#include<stdio.h>
int main()
{
    printf(”Hello World!”);
}" > main.c
gcc main.c -O3 -o ex4
chmod +x ex4
```
Now you can execute your freshly compiled `ex4` executable:
```bash
./ex4
```
## Summarizing and submitting
After writing sown all the exercises, you can stage and commit your files to a local repository:
```bash
git add .
git commit -m "Lab1"
```
You can use `gh` tool to publish your repo to GitHub.

Install `gh` on Ubuntu/Debian:
```bash
sudo apt update && sudo apt install -y gh
```
Login to GitHub:
```bash
gh auth login
```
Publish to a private repo:
```bash
gh repo create
```
### End of the Lab