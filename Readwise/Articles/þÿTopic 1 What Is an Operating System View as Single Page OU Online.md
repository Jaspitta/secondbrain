# þÿTopic 1   What Is an Operating System?: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/283869878/JuLW0bs8HHvp1odRE_pZKIyW1ssO2ZpEK2uYh3LqwTA-cove_5CuY8wr.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 1   What Is an Operating System?: View as Single Page | OU Online
- Category: #articles
- URL: https://readwise.io/reader/document_raw_content/283869878

## Highlights
- A computer operating system is the software needed to turn the collection of hardware that makes up a computer into a useful and useable system.
- l focus on personal computers – desktops and laptops – and on mainstream operating systems – Microsoft Windows, Apple macOS and Linux.
- all operating systems are built on similar principles, although they may look and feel different to their users.
- t it is not easy to draw a line around what is and what isn’t part of the operating system.
- I suggest that the major functions of an operating system (OS) are to do the following: provide a user interface to load and run programs manage the storage of data and programs support multitasking achieve device independence.
- To achieve device independence, the operating system must provide a consistent interface to hardware so that programs can use different hardware devices without having to be rewritten.
- The success of an operating system is a measure of how well it satisfies the needs of all these stakeholders.
- o transform the hardware components that make up a computer into a usable and useful system
- Mainstream operating systems can all present a desktop metaphor to the user:
- The normal interface offered by modern personal computers is known as a graphical user interface (GUI)
- the interface you investigated in the previous activity is known as a command-line interface (CLI) because the user types commands to interact with the computer
- ponent of an operating system interface that enable
- The component of an operating system interface that enables the user to start programs is sometimes referred to as the shell
- A particular component of a GUI is a file manager to provide facilities for manipulating files:
- essentially the same operations are carried out by all shells.
- f moving a file that I have just described can be represented in a diagram as shown in Figure 2 below. This diagram shows three layers
- (at the top) the shell, (in the middle) the core operating system functions, including those required to manipulate files on the disk, and (at the bottom) the hardware itself
- , it is not only the user who needs to carry out an operation like moving or saving a file. An application program such as a word processor will sometimes need to use the disk
- , the application programs are able to call on the core functions of the operating system
- The term application program is generally understood to mean a piece of software which is obtained separately from the operating system
- Windows includes the simple text editor Notepad, a program called Task Manager
- These programs are not really part of the operating system itself
- For the rest of this block I shall refer to them as simply utility programs
- If the details of the hardware are taken care of by the operating system, then application programs do not have to be adjusted to any particular hardware configuration
- Hardware independence or device independence allows application programs to run unaltered on a wide range of hardware devices
- The operating system for a personal computer allows the user to run more than one application program at the same time. This is called multitasking
- programs running at the same time must share access to the resources of the computer,
- The operating system must manage this sharing so that every program has access to what it requires yet does not interfere with the running of any other program.
- Processors and operating systems therefore need a means of ensuring that important aspects of layering are strictly enforced and that the operating system retains full control over the critical resources.
  This can be done because processors are designed to run in two modes, called user mode and kernel mode.
- it is also possible to install an OS into a virtual machine (VM), which opens up the possibility of having more than one OS available even on a single personal computer
- Since the VM is just a software emulation stored as files on your computer, it can be easily backed up, cloned and transferred
- Virtualisation in general means to create a virtual or emulated version of a computing device or other resource.
- A more radical version of virtualisation is needed to support an entire virtual machine (VM). Hardware virtualisation must give the illusion that each virtual machine has its own processor, memory, storage, network adapter, display, keyboard and mouse, while actually running on a single set of hardware.
- A general-purpose personal computer will have an operating system already installed; we’ll refer to this as the host operating system.
- Once a virtual machine is created, a new OS can be installed on the VM; this is called a guest operating system.
- A variant of full virtualisation is containerisation in which applications appear to run in isolated guest OSs but share a single kernel
