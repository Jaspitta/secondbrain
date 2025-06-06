# þÿTopic 5   Users and Security: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/287442995/RI-SabhbkhTGy1lNdMKlLRnbhSjqzO13KI2gn9AItdg-cove_82nP7JJ.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 5   Users and Security: View as Single Page | OU Online
- Category: #articles
- Summary: Linux systems manage user security through a permissions scheme that controls access to files based on user roles. There are three types of permissions: read, write, and execute, which are assigned to the file owner, group, and other users. Understanding these permissions is essential for managing user accounts and ensuring the security of files in a multi-user environment.
- URL: https://readwise.io/reader/document_raw_content/287442995

## Highlights
- Mainstream operating systems such as Windows, macOS and Linux are multi-user systems,
- For Linux, one reason is historical: Linux is modelled on Unix, and Unix was developed when computers were large and expensive and needed to be shared by many users
- Having a single product line reduces the software development effort to build both the OS
- Multi-user support is needed for larger systems such as servers (whether Linux, Windows or macOS), and is therefore present even when the OS is used as a personal computer
- it possible to design a more robust and secure system by giving different users different permissions
- A distinction that is common in operating systems is between administrator accounts (‘admins’) and normal users
- admins are responsible for configuring hardware and software for the entire system and must create, change and delete system files
- remain as a normal user, switching only to the more powerful role of admin when strictly necessary. That way you won’t accidentally delete a file
- On Linux systems, there is a one special admin user, the superuser called ‘root’.
- The root user has unlimited powers
- a Linux installation will always create one or more normal users with much more limited permissions.
- In some current Linux systems including Raspberry Pi Desktop, the root account has its login disabled so that no one can log in as root.
- Linux now has a mechanism to grant temporary elevated privileges
- the command sudo
- On Windows a broadly similar mechanism exists.
- ‘Run as administrator’
- User Account Control (UAC) protects users from unintended (or malicious) system changes.
- The effect is that Windows accounts (whether admin or normal) are normally run in a similar way to a sudoer account on Linux; that is using normal privileges for most tasks and being granted elevated privileges only when necessary.
- As a system administrator
- managing user accounts: adding, deleting and assigning appropriate permissions
- adduser and useradd. This is typical of Linux: there may be both a low-level binary command and also a higher-level scripted command.
- The low-level binary command is a direct interface to the underlying OS API
- The higher- level alternative is easier and safer to use interactively but may differ between distributions
- r, w and x respectively.
- The same permissions are used with other objects, for example directories
- Linux controls file permissions separately for different roles: the user (you, the owner of the file) the group that the file belongs to any other users.
- u, g and o respectively.
- The first character distinguishes normal files, shown as - (hyphen), from other file-like objects, by far the most common of which is d for directory.
- The subsequent nine characters are permissions,
- , the operating system will store these permissions internally in a binary format.
- 000 for no read, write or execute, and 111 to allow read, write and execute.
- 9 bits to encode permissions for a file.
- chmod [ugoa][-+=][rwx] <file>
- Permissions apply to directories and other objects as well as regular files, although the interpretation of read, write and execute may not be quite as obvious
- The ‘user’ in this context does need clarification, however. More precisely, it is the owner of the file, not the current user
- y the user who first created it a
- ownership can be changed using the command chown
- the /etc/passwd file contains an entry for each user in the system
- The third and fourth fields contain numbers which are the user ID (UID) and group ID (GID). It is these numbers which are used inside the operating system to identify users and groups.
- Commands such as ls must look up users and groups in the /etc/passwd or /etc/group files to find the human-readable name corresponding to a UID or GID.
- why the /etc/passwd and /etc/groups
- In the basic Linux system, although a user can belong to several groups, it isn’t possible to assign a single file to multiple groups.
- An alternative mechanism is the access-control list (ACL)
- This list can include any number of different users or groups, and a wider range of access types than the simple read/write/execute considered above.
- Sometimes traces of older ideas remain as systems designers try to keep backward compatibility. This is evident in the Linux password file, as can be seen in the discussion below.
- password file actually contains user account information which is needed by many programs,
- Traditionally passwords were stored directly in the /etc/passwd
- The operating system could store the password as plain text but hidden in a protected file
- You should backup an operating system, copying all the system files to an external disk drive or cloud storage (or historically to optical disc or tape). But once files are copied to a backup, they are no longer protected by the original operating system
- Modern approaches to security have moved towards encrypting data rather than attempting to hide it,
- Linux systems now use one of several supplementary schemes for additional security
- use stronger encryption and store the results in a ‘shadow’ password file /etc/shadow.
- only readable with root (or sudo) permission.
- the result stored in the shadow file is a hash of the user’s password
- A cryptographic hash function takes a string or long piece of text as input and produces a fixed-size string of bits (e.g. 128 or 256 bits) as a result
- It is a mathematical transformation
- a small change in input gives a large change in outp
- the output doesn’t depend on the length of the input
- the transformation is one-way.
- When checking a user’s password, the operating system takes what is typed in, hashes it and compares it with the stored hash; i
- Let’s say I set my password to ‘1234’ and find the hashed value stored in the shadow file. I can scan the whole shadow file looking for another user who has the same hash
- This can be developed into a dictionary attack: an attacker prepares a list in advance of possible passwords and computes the hashed value for each
- Requiring passwords to include numbers and punctuation symbols is not a complete protection: a rainbow attack generates all possible combinations of letters, digits and symbols up to some length
- The salt field is a deterrent to these dictionary attacks. When a user sets a new password, the operating system generates a random string of characters as the salt and stores it in the shadow file. The salt is added to the user’s password, effectively lengthening it with random characters, before the result is hashed.
- a dictionary attack is still possible: an attacker could combine the salt with each possible password before calculating the hash. However, the attacker would now have to build a new dictionary for every user because the salt value will be different each time.
