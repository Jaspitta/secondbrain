---
aliases:
- compression
- compressing
- archiving
---

[[archiving and compressing|archiving]] is the process of combining different [[file]]s and directories into one for easiness of storing and moving it, [[archiving and compressing|compressing]] compress the content into fewer bytes than the original

One big worry about [[archiving and compressing]] is that the content of the file can be somewhat obfuscated and extracting it would not be safe, there is no way to verify the content before first [[excrtacting]] it.
Most download sites provide a [[message digest]] with the file which can be used to verify the integrity, usually this is a [[SHA-256]] string produced with [[hashing]], the owner of the original file publishes such string so that who downloads the file can hash again the file and check if the strings match, if not the file has been corrupted accidentally or maliciously.
You can yourself use the `sha256sum <file>` command to calculate the [[message digest]] yourself and verify it matches.
When doing such verification it is recommended to acquire the [[message digest]] and the file from two separate sources, this is because if a [[hacker]] is trying to publish a malicious file through a fake website, likely he also published a different message digest so the verification would be useless.
The most common [[archiving and compressing|compression]] utilities also have some internal checks to verify if files are corrupt, in addition you are always recommended to check the content of an archive before extracting it.

The most common utility for [[archiving and compressing|archiving]] is [[tar]] which stands for [[tape archive]] and output a .tar file, it was designed for [[tape storage]] so it is made for [[block device]]s and it adds padding to each file to make sure it respect the block size. An archiving utility program in general has to make sure the identity of the content is respected, this means that not only the content of the files but also information about the file is maintained, this includes [[permission]]s, [[timestamp]], author and more. The problem with maintaining permissions of the files is that when a directory is archived, there is no guarantee that the same user will exist where it is extracted, therefore, unless the archiving user is a [[root user]] the ownership is transferred to the user [[extracting]] the file

The tar program, as stated, adds padding to files to make them a specific size, this not only does not decrease the size but actually increases it. For this reason archiving is commonly paired with [[archiving and compressing|compressing]] to save space, such algorithms have to be [[lossless]] meaning no information is lost, like [[run-length encoding]] for example.
The two most common [[compression algorithm]]s in [[linux]] are [[gzip]] and [[bzip2]], this result in a two step process that gives a file with a double extension like .tar.gz.
Because of how common it is to archive and compress together, [[tar]] now compresses the file for you if you want and can also decompress when unarchiving a file.

[[tar]] and [[gzip]] remain very widely used especially in the [[linux]] world, but another tool that took massive popularity among all the [[OS]]s is [[zip]], it is also use in special flavours for files that you know very well for example:
- .odt or .ods are [[xml]] [[file]]s compressed with [[zip]]
- .docx and .xslx also
- .jar are [[zip]] archives with special structure
Zip is a single tool that does both [[archiving and compressing|archiving]] and [[archiving and compressing|compression]] and is available in all [[OS]]s including linux with the command [[zip]] and [[unzip]] 