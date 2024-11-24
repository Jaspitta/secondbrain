---
aliases:
  - data carving
---
It is a process but also a software that can help you recover files that have been [[hard delete]] but have not been overwritten yet.
It has a set of [[file header]] of common [[file type]] (docx, png...), it looks for these headers in the disk and from there try to look for the end of the file, sometimes it is in the header itself, sometimes there is a footer, other times it looks for the next header and in the case of [[fragmentation]] it becomes exponentially difficult to be able to find the end.
For [[SSD]]s the high level of [[fragmentation]] makes impossible to recover data this way, but even worst the [[TRIM]] process erase the content of the file in the background.

Even though recovering the full file can be very difficult, it is still very possible to recover a portion of the file starting from the header up to the end of the [[HDD clusters|HDD cluster]].


