# Block 3 Part 1 Data on Your Computer: A Private Investigation!

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/188736770/ihrmnlPqr6LLYsfPub7azoJj6ZNQ6k2E-c3oN6haGgg-cove_F4pgiFP.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 3 Part 1 Data on Your Computer: A Private Investigation!
- Category: #books
- Document Tags: [[favorite]] [[shortlist]] 
- Summary: The text explores how data is stored and managed on a computer's hard disk drive. It discusses file systems, data organization, and the implications for digital forensics. The process of creating a disk image and analyzing main memory (RAM) for potential data retrieval is also highlighted.

## Highlights
### Introduction
### 1.1 Hard disk drives
#### 1.1.1 The structure of a hard disk drive
- or HDD
- Even a particle of dust could cause it to crash
- three circular disks
- called platters
- rotate on that central spindle
- covered on both sides with a metal that can be magnetised
- Each platter has a head
- able to detect and change the magnetic areas
- 7200 revolutions
- a spot on the outside
- moves faster
### 1.1.2 Storing files on a hard drive
- the operating system runs something called a file system, which dictates how data is written to – and recovered from – a disk
##### Formatting a hard disk
- we can prepare
- any hard disk
- to work with any
- file system by
- formatting it
- at least one area of the disk must be loaded with
- file system
- These areas are called partitions
- reformatting a disk can also be a way of removing viruses from the computer, or fixing other errors
- hard disks are formed of a series of tracks
- called rings
- that can contain data
- A disk track is too large to manage the data effectively
- part of the formatting
- tracks are divided into several numbered, equal divisions known as sectors
- sectors are arc-shaped pieces of a track
- hold 512 bytes of data
- grouped together in clusters
- typically there are 4 or 8
- sectors in a cluster
- a file
- takes up a whole number of clusters
- platter
- tracks
- sectors
- same amount of data
- cluster
- one or more consecutive sectors
- FAT, which stands for File Allocation Table
- is the area of the hard disk that is used as an index of every cluster
- called FAT32
- It can only cope with a maximum file size of 4 GB
- New Technology File System (NTFS), where a table called a Master File Table (MFT) does a similar job
- The Apple File System
- Linux file system is called ext4
- when a new file is to be saved, the operating system can also use this table to determine which clusters are in use
- space that is available for files to be written to is referred to as unallocated space
#### 1.1.3 Deleting data from an HDD
- When a file is deleted
- data is still there
- but there is no reference to it in the file allocation table
- logical size of a file is a measure of the number of bytes
- physical size is almost always bigger than this because it has to be stored in a discrete number of clusters
- which means that there is a slack space
- data in the slack space might well come from files considerably older than the deleted file
- called latent data or ambient data
- can provide investigators with clues
##### How to permanently delete data from an HDD
- Overwriting
- fills every part of the disk with zeros or ones or a random mix of the two
- Degaussing
- a powerful magnetic field
- can erase an entire disk in a few minutes
#### 1.1.4 Fragmentation
- a hard disk drive gets slower the fuller it gets
- Physical destruction
- a file that cannot be stored in a single cluster, the file system breaks up the file in cluster-sized chunks and tries to save them in contiguous clusters
- Incineration
- if contiguous clusters are not available, the file is fragmented
- crushed
- shredded
- called fragmentation
- a larger cluster size
- reduces the potential for fragmentation
- reduces the amount of disk space needed to store information about the used and unused areas
- increase the likelihood of unused slack space
- defragment (or defrag)
- a software utility
- moves the chunks of files to try to arrange them in contiguous clusters
- Windows 10
- schedule a defragging utility
- once a week
- on a Mac
- OS X defrags files itself using Hotfile Adaptive Clustering (HFAC)
- files that are accessed frequently
- allocating them to a space on the outer track of the disk called the ‘hot zone’, which has faster access
- then, it is not necessary to defragment
- may become necessary
- when working with large files
### 1.2 Solid-state drives (SSDs)
#### 1.2.1 The growth of solid-state drives
- They use a technology called flash memory
- a solid-state chip that maintains stored data without any external power source
- file and operating systems still maintain the same system
#### 1.2.2 Comparing SSDs and HDDs
#### 1.2.3 How flash memory works
- the SSD device
- emulate the logical structure of a spinning hard drive
- when it comes down to how data is actually written to an SSD, they are quite different to hard disk drives
- made up of semiconducting materials
- a whole series of tiny electrically insulated boxes
- By applying a small electrical voltage at the top of one of these boxes, additional electrons can be attracted
- he electrons are trapped there
- In this state, the insulated box has a bit value of 1
- can be reset to 0 by forcing the additional electrons to flow out of the box by using an electrical voltage in the other direction
- continual reading and writing of the value of a box causes the insulation enclosing it to degrade over time
#### 1.2.4 Writing to and deleting data from an SSD
##### Writing data to an SSD
- software
- tries to prevent the same block in semiconductor memory from being used repeatedly
- every time a file is modified, it is written to different physical locations
- called wear levelling
- much more likely that a previously ‘deleted’ file will be partially overwritten
- a memory cell can only be written to when it is empty
- before a file is written
- that cluster are erased
- This slows down write operations
- manufacturers provide SSD control software, called TRIM, that uses any quiet time to ‘garbage collect’ any unreferenced file fragments
- just powering up an SSD
- can allow the garbage collection routines on the SSD to continue
- Deleting data from an SSD
- you can still physically destroy the drive
- degaussing does not work
- SSD manufacturers have a utility
- called ATA Secure Erase
- applying a spike of voltage to all of the memory cells simultaneously
### 1.3 Securing and analysing a hard drive
#### 1.3.1 Rupert and Gloria’s first case
#### 1.3.2 Securing the hard drive
##### Copying the hard drive and allocating a hash code
- forensically sound – that is that it is obtained in a rigorous way that is acceptable to the courts
- disk image of the hard drive – that is, we are going to copy it, bit for bit. This is a process called dead system imaging
- We are going to use a write blocker for that – it is a piece of software that makes the image disk read-only
- also run an algorithm that calculates a number, called a hash code, from all of the 0s and 1s on the original disk
- If the hash codes match, we can be certain (or virtually certain, anyway) that the disk image is a true bit-for-bit copy of the original
- binary representation of the name ‘TAM’. We could reduce this to a single number by adding up the ASCII codes for ‘T’, ‘A’ and ‘M’
- anagrams of ‘TAM’ will all have the same hash code
- ‘weight’ the ASCII codes
- 1 × 84 + 2 × 65 + 3 × 77 = 445.
- there will still be lots of other words that will have the same hash code as ‘TAM’
- when two sequences of bits have the same hash code we call it a collision
- very good hash code algorithms used in practice are designed to minimise collisions
- the hash code to be much smaller than the number of the original bits
- use the modulus operator
- he remainder when one integer is divided by another
- A smaller hash code is often obtained by finding the modulus with a prime number
- ‘TAM’ we can find its modulus with a prime number such as 23. So 
  445 % 23 = 8
- There are many different algorithms for calculating a hash code
- hash code (sometimes also called a checksum) for a submitted file
#### 1.3.3 Reading the hard drive
- image mounter
- a piece of software that enables the operating system to read and write data to a disk image
#### 1.3.4 Timestamps and other metadata
- Metadata is a set of data that describes and gives information about other data
- It also keeps timestamps, which tell you when a file was created, modified or deleted
- the ‘Accessed’ timestamp should be updated each time the file is accessed, but it is often disabled by default
- this frequent updating can affect the performance
- You do have to be a bit careful when looking at timestamps,” replied Gloria, ”because it is possible for someone to alter them by manipulating the computer clock
### 1.4 System files and deleted files
#### 1.4.1 System files
- system log,” said Gloria. “The operating system keeps a log file of events such as logins, logouts, device changes, system changes, etc.
- I can also see that a flash drive was plugged into the USB port at 19:38, then unplugged at 19:41. There was a logoff at 19:45
- .ost files. These are local copies of everything that is on the Microsoft Exchange Server, which is all of the email traffic to and from Zack’s Outlook email account. They are automatically stored so that they can be accessed and worked on when the computer is offline. When Outlook connects to the server again, they are synchronised
- Microsoft supplies a free reader for this format
#### 1.4.2 The Recycle Bin and soft deletes
- a soft delete. This is when a file is deleted, either by pressing the delete button or dragging it to the Recycle Bin (or the trash can
- the file stays exactly where it is
- the operating system renames the deleted file with a name that starts with $R and creates an associated file, the $I file, to contain metadata about the deleted file
- Well, the format of the $I file in Windows 10 is as follows:
  Offset
  Size (in bytes)
  Description
  0
  8
  Header
  8
  8
  File Size
  16
  8
  Deleted Timestamp
  24
  4
  File Name Length
  28
  Var
  Original File Name (including path)
- An offset is a position relative to another point
- the Header
- identifies it as a $I file
#### 1.4.3 Hard deletes
- keeps your soft deleted files until the garbage consumes about 5 per cent
- it is more efficient for the operating system to just delete the metadata. Deleting a file’s metadata and marking the location as being available again is an extremely fast operation
#### 1.4.4 File carving
- a series of bits in the header of the file (sometimes called a magic number) that indicates what kind of file it is
- hex editor is a piece of software that can be used to read and manipulate the fundamental binary data that constitutes a data file
- there is software available, called file carving or sometimes data carving software
- it does some further checks on the subsequent bytes to see if they are compatible with the kind of file identified
- the software then tries to find the end of the file
- if the header is missing, these basic data carving techniques won’t work
- but what if it is not stored in contiguous clusters? Then there will be lots of unrelated data in between the beginning and the end of the file, if the end is found at all
- so file carving doesn’t work on SSDs
### 1.5 Analysing main memory (RAM) and closing the case
#### 1.5.1 Live acquisition of main memory (RAM)
- I had hoped to make a RAM dump, so that we can take away a live system image of the RAM
- this software doesn’t need any installation on the machine, and it leaves a very small footprint because it interacts with the kernel – the very heart of the operating system. It is virtually undetectable
#### 1.5.2 RAM data recovery
- but RAM is also is the place where the operating system is loaded
- contains information about what processes and programs are running
- which networks the computer is connected
- passwords
- files that have been decrypted
- the keys
- there are registry hives
- The registry is an area of RAM that is used to store the lowest-level settings
- A hive is just a space within this registry
- Each time a new user logs onto a computer, a new hive is created
- there is some data that is only ever stored in RAM, particularly about web apps such as Gmail, or if private browsing has been enabled
- For example, you have probably heard of page files (pagefile.sys)? When there is data in RAM that is not being used very much, it is stored in a page file, which the operating system then saves to special locations on the hard disk. Another example is hibernation files (hiberfil.sys). If you hibernate your machine, the contents of the RAM are moved over to the hard drive, and when you ‘wake up’ your machine, they are copied back over into RAM.
- but when you print something in Windows, each page is processed into a picture which is stored as an Enhanced Metafile (EMF) within the printer spooler file
### 1.5.3 Wrapping up the case
### 1.5.4 The next case
