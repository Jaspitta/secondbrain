---
aliases:
  - Solid State Drive
  - Solid State Drives
---
A type of drive that uses [[flash memory]] which is a particular solid state chip which maintain date without a power source.

Since the [[file system]] and [[operating system]] use abstractions they do not need to know the physical properties of the drive, therefore we have the same structure of [[sectors]] and [[HDD clusters|HDD cluster]]. This is also possible because the [[SSD]] has internal software that emulates the structure of an [[HDD]]

Since there are no moving parts, [[HDD fragmentation]] happens but it is not really a problem for an [[SSD]].

Internally, an [[SSD]] is made of [[semiconductor]] boxes, you can add electrons into them by applying a voltage (gain a negative charge and take the value 1) and remove them with a voltage in the other direction. Since we are talking about a [[semiconductor]] the charge can be maintained also when the power is switched off.
These properties also means that a box can be written only when it is empty, therefore before writing a cluster it has to be erased which can slow down write operations by a lot. To alleviate this problem the software in [[SSD]] has a background process called [[TRIM]] that uses rest times to erase unreferenced [[HDD clusters]] to prepare them for write.

In a similar fashion to erase the content there is a software called [[ATA Secure Erase]] which apply a voltage to the whole [[SSD]] instead just one cluster like [[TRIM]] and flush the whole memory. You can always physically destroy your [[SSD]] but remember that [[degaussing]] does not work.

One drawback is that compared to [[HDD]] the memory part of the device actually wear down faster, after max a few hundreds of thousand of read/write the [[semiconductor]] material loose part of its properties and become unreliable unlike [[HDD]] which can support millions of operations.
To alleviate this problem the software that manages the [[SSD]] uses [[wear leveling]] where files are intentionally split around the [[SSD]] and changed of location every time they are modified to avoid using always the same [[HDD clusters|HDD cluster]].



