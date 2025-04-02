# þÿTopic 3   Shells: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/285577403/6vMWgFyc_T778znX7rG0vmzXWKGyUnT-AlyhXkQGFUI-cove_ng6QoDm.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 3   Shells: View as Single Page | OU Online
- Category: #articles
- Summary: This topic explains the role of a shell in an operating system, which allows users to load and run programs through graphical user interfaces (GUIs) or command-line interfaces (CLIs). While GUIs are common, command lines offer unique benefits and are particularly useful in professional settings. The shell is essential for executing programs, and users will learn to navigate the Linux command line in this module.
- URL: https://readwise.io/reader/document_raw_content/285577403

## Highlights
- I will use the term ‘shell’ to talk about this interface to the operating system, whether it is a graphical user interface or a command-line interface
- a terminal was a keyboard and printer (a teleprinter or teletype, abbreviated tty) connected by a serial cable to a central computer.
- later versions that used a screen rather than a printer
- s console was a terminal directly connected to the mainframe computer that displayed system error messages;
- A shell allows users to start programs, and in a general sense encompasses both graphical user interfaces (GUIs) and command-line interfaces (CLIs).
- the command-line interpreter, which is the software that accepts typed commands and does something appropriate
- a shell encloses an environment in which programs run
- . In practice, that isn’t always possible since the shell may be very tightly integrated with the rest of the OS
- A graphical user interface is one that relies on clicking or tapping more than typing commands, and conveys output using more than just plain text.
- Applications provide their own interfaces and a developer could design any style they chose.
- Most OSs go further than this: they provide a widget set – icons, menus, buttons and other controls – to give a more uniform look
- Mainstream OSs usually provide a complete desktop environment to act as the shell.
- There are a number of Linux desktop environments, but the four in widest use are probably: GNOME KDE LXDE Xfce.
- Choosing among these is largely a matter of personal preference,
- uses the GTK widget toolkit. These widgets were originally developed for GIMP (GNU Image Manipulation Program)
- associated with the GNU Project and Red Hat Linux,
- GNOME 3 shell has moved away from the desktop metaphor
- designed to work well with touch
- based on the Qt widget toolkit
- positioned as a cross-platform project,
- Having rival desktop environments could make it harder for developers t
- The freedesktop.org project helps to bring developers together to work on interoperability and common approaches
- the first word is the command to be carried out spaces separate parts of the command line zero, one, or more arguments can be given to the command where more than one argument is given, the order is significant options can be given: options are flagged with a hyphen options are single letters several options can be combined they can be given in any order.
- Linux file systems are case sensitive and commands generally are implemented as executable files. By convention lower case is used for commands;
- The man page is the definitive documentation for each Linux command.
- Since most examples you will see in books and on the web use these single-letter options, I will do the same. However, when writing scripts I recommend using the long form to make your scripts self-documenting
- Programs are executable files and the shell will have identified which file is to be loaded and run.
- Many programs will be binary code files which contain machine instructions
- To run a code file, the OS must allocate main memory for it, then load the program into memory, create a process and start it executing.
- a script file contains OS commands written in plain text
- the command-line interpreter loads the file and then executes each command in turn
- the OS must hand control to the appropriate interpreter
- and allow it to execute the statements of the program.
