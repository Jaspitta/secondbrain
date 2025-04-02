# þÿTopic 4   the Command-Line Interface: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/286222342/qoF940j-74ynb4HH3waD4w9EAmRxzFNJ2GA7RtYvFy8-cove_Q3MaXCS.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 4   the Command-Line Interface: View as Single Page | OU Online
- Category: #articles
- Summary: This text explains how to archive and compress files using command-line tools in Unix/Linux, focusing on the `tar`, `gzip`, and `bzip2` commands. It highlights the difference between archiving (combining files) and compressing (reducing file size) and emphasizes the usefulness of scripting to automate these tasks. The text also mentions the wide compatibility of zip files but notes their limitations compared to Linux tools.
- URL: https://readwise.io/reader/document_raw_content/286222342

## Highlights
- A further level of checking is provided by many download sites
- a ‘message digest’ accompanies the file and can be used to check the integrity of the download.
- The message digest is produced by a cryptographic hash function which takes the content of the file and reduces it to a string of bits. Here the SHA-256 hash function has produced 256 bits
- any change to the content results in a different hash value.
- The creator of the file produces and publishes the hash
- you recompute the hash value and check that the result is the same
- difference indicates that what was downloaded is not what was intended
- The standard program used to create an archive is tar (tape archive)
- The output of tar is an archive file, conventionally given the extension .tar
- The key function of tar is to write out the contents of files and record enough information so that the structure of directories can be recreated when the archive is later read. tar must also faithfully record information about a file
- tar was designed to write information direct to a magnetic tape drive. Tape drives are ‘block devices’ (block and character devices are covered in another topic), so padding is inserted between files to ensure that each file starts at a block boundary and make it possible to extract a single file
- As noted above, the base operation of tar does not compress files and includes additional padding between files
- , the technique of ‘run-length encoding’ would work well with the padding you saw in a tarball
- Any compression algorithms used for archiving must be lossless
- The two-step process of tar and gzip produces the double extension .tar.gz
- tar has been extended to run the compression step itself.
- , tar can also deal with decompression as a further convenience.
- tar should preserve the owner, permissions and timestamp for a file
- When tar is run as the root user, it behaves in exactly this way.
- when used to transfer files between different systems, it would not be possible to preserve ownership since the users on different systems may not be the same.
- For a normal user, tar will by default transfer ownership of files to the user performing the extraction
- The zip format is supported by all mainstream OSs and has become a de facto standard for file transfer
- OpenDocument office files (.odt, .ods and others) are zip-compressed XML files Microsoft Office files (.docx, .xslx and others) are also zip-compressed XML files JAR files are used in the Java code ecosystem; they are zip archives with a particular structure.
- Zip archives have the advantage over tar/gzip that they offer straightforward compatibility across operating systems
- A solution is to record the commands you use in a file so that they can be repeated later, and this is the start of developing CLI scripts
- command-line interpreters go beyond just replaying commands
- When combined with the many utility programs provided with an OS like Linux, the result can be very powerful.
