---
aliases:
- command line interface
---

This is another type of [[shell]] that can be used to communicate with the [[operating system]], it is text based both in input and output and it has a steeper learning curve but with some noticeable advantages.

commands list:
```
date # print current date
cal # print current month calendar
whoami
history
cal 1999 # calendar full year 1999
cal jan 2000
ls
ls /var
ls -l /var
ls -l -t /var # -t order by time
ls -lt /var
ls -tl /var
man ls # open the manual for ls
whatis ls
cd
tar --list --file=file.tar.gz # show the contents of a compressed archive
tar --extract --verbose --file=file.tar.gz # extract the content of a compressed archive
tree dir # show the tree of the directory
sha256sum file # hash the file with sha-256 function
tar --create --verbose --file=file.tar dir/ # create an archive from the dir/ directory
diff -r ~/work/life ~/extract/life # check for differences in files content and directories
gzip file # compress a file with gzip
gunzip2
bzip2 file # compress a file with bzip2
bunzip2 file
tar --create --verbose --gzip --file=file.tgz dir # archive and compress a directory
tar --create --verbose --bzip2 --file=file.tbz dir # archive and compress a directory
tar --extract --verbose --file=file # decompress and extract a file
```

command syntax:
- [[command]]: case sensitive because a command is simply a script in a [[file]] so as files are case sensitive the command which is simply the name of the file is too
- [[argument]]s: 0 to n, order sensitive
- [[option]]s: 0 to n, order insensitive, case sensitive, preceded by a '-'

As anticipated, a [[command]] is simply a collection of [[instruction]]s to be executed located in a file. There are two possible type of files to be executed:
- [[binaries]]: also called [[code file]]s files containing [[machine instruction]]s ready to be executed, the [[operating system|OS]] allocates memory for it, load the program into memory, create a [[process]] and start it, once it ends the memory is freed by the [[operating system]]
- [[script]]s: the file contains instructions as simple text, usually calling other [[binaries]] inside. The [[command line interpreter]] reads the file and execute each command in it, if necessary the OS hands control to other [[interpreter]]s like [[Python]].