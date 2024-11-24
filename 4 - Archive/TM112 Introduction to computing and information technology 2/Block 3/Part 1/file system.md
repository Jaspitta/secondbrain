A program, part of the [[operating system]], designated to writing, reading and organizing files in the physical hardware like an [[hard disk drive|HDD]].

Since the file system change with the [[operating system]] with need to prepare the hardware for the type of [[file system]] that we are going to use, this process is called [[formatting]].

The file system also dedicate a portion of the [[hard disk drive|HDD]] to a [[File Allocation Table]] which is an index of the different [[HDD clusters|HDD cluster]].
The standard is a [[FAT32]] which handle size of max 4GB, newer models like the [[New Technology File System]] from [[Microsoft]] uses a [[Master File Table]], than there is the [[Apple File System]] and the [[ext4]] for [[linux]] systems which do a very similar job.

When [[data]] is deleted, it actually remain there, the [[reference]] to is is simply removed from the [[File Allocation Table]] and therefore the [[cluster]] is seen as unused an can be overwritten if needed, this is called [[unallocated space]].

Since files are stored in [[HDD clusters|HDD cluster]] and a [[HDD clusters|HDD cluster]] has a fixed size, there is always some unused space in the last [[HDD clusters|HDD cluster]] that a file takes, this unused space is called [[slack space]]. Because of this, data in the [[slack space]] can survive if the new file is smaller than the previous one and remain there for a long time, this is called [[latent data]] or [[ambient data]].

As we saw, it is easy to have a vulnerability and leave available data that we think was deleted. There are however 3 ways of ensuring data is [[properly removed]] but they are not always easy:
- [[deletion by overwriting]]: all the [[disk]] or [[partition]] is filled with 0, 1 or a random one
- [[degaussing]]: hitting the disk with a powerful magnetic field will disrupt the magnetization of the components. However [[HDD]] are encased in a protective layer so the field needs to be very strong
- physical destruction: incineration, crushing or shredding