`sudo adduser ali` to add a user named ali
`su ali` to login as ali
`deluser ali --remove-home` delete user ali and it's home directory
`sudo addgroup students` add students group in the /etc/group dir
`gpasswd -d ali students` add ali to students group
`sudo delgroup students` delete students group
`chmod [ugoa][-+=][rwx] file` change permission to file
`sudo chown ali:pi file` transfer ownership of file to user ali and group pi

symbol to file type:
- d: directory
- - regular file
- l symbolic link
- s socket, for interprocess communication
- p pipe, fir interprocess communication
- b block file, hardware communication
- c character file, hardware communication

for file types in linux permissions you have d for directory, l for link, c for character, b for block and - for file

linux main folders:
```
/home
/bin
/sbin
/boot
/tmp
/lib -> essential OS and kernel modules
/lib/modules -> load kernel modules
/usr -> user programs
/opt -> cross platform programs
/etc -> config
/var -> changing files
/dev -> device drivers
/proc -> interfaces for running processes
/mnt -> access to devices
```

```
fg %1 -> resume job 1 to foreground
bg %1 -> resume job 1 to background
command & -> start process in background
jobs -> visualize status of current jobs
pstree -> see all current running processes
systemctl status -> status of current runnign deamons
sudo systemctl enable
sudo systemctl stop
```

The POSIX signals for processes are: 
- SIGINT: interrupt from keyboard -> Ctrl C
- SIGQUIT -> Ctrl \
- SIGILL: terminate (not ignorable because OS managed)
- SIGTERM: terminate (ignorable)
- SIGSTP: pause or stop -> Ctrl Z
- SIGCONT: continue after SIGSTP

`ps -> see running processes`