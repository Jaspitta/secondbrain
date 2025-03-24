# þÿTopic 2   Structure of an Operating System: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/284907081/jFdHCdpoNccwcve75wW_lcT4Ly-8-lB9v6WJuK2-STI-cove_EdvqQ80.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 2   Structure of an Operating System: View as Single Page | OU Online
- Category: #articles
- Summary: This topic discusses how operating systems, like Linux, are structured with layers and modules to separate application programs from hardware. It explains the roles of user mode and kernel mode in managing system functions and hardware access. The flexibility of Linux allows users to modify the graphical user interface, enhancing their interaction with the OS.
- URL: https://readwise.io/reader/document_raw_content/284907081

## Highlights
- application programs do not interact directly with the hardware of the computer, but instead call on services of the operating system. This gives the operating system the opportunity to control and manage access to the critical hardware resources.
- OSs use the fact that the processor will run in one of two modes, called user mode and kernel mode.
- these are referred to as rings
- such as input and output, are ‘privileged’ instructions and can only be used in kernel mode.
- A bit in the processor’s status register records the current mode
- Instead, when an application program wishes to use core operating system functions, it makes a system call using the syscall machine instruction.
- , a return instruction restores the previous processor state
- The same switch from user mode to kernel mode is needed to service interrupts. An interrupt is a hardware signal triggered by an I/O device or other hardware to ask the processor for attention
- When an interrupt occurs, the processor stops its current execution, switches to kernel mode, and starts to run a special interrupt service routine
- e operating system routines that operate in kernel mode and are called via syscall or interrupts are known as the kernel of the operating system
- For current mainstream OSs
- the OS provides
- a large library of subroutines
- The library routines use syscalls only when necessary
- Software can also be organised into modules, each of which is a collection of software routines and data structures that is designed to deal with some area of functionality.
- . A hardware interface focuses on a standardised method of communication between components.
- A software interface is an analogous concept but applied to software.
- Viewed in this way, we can see the OS as being made up of a number of different modules,
- Process management. This module is responsible for switching between processes
- Memory management. This module manages the sharing of physical memory
- I/O module. This handles low-level access to devices,
- File system. This manages files and directories
- each major subsystem in the figure above may itself be composed of layers and modules.
- An OS module typically has both a user mode and a kernel mode component;
- Library routines are provided for different computer languages and provide an easier- to-use interface than direct access to the OS.
- The figure also highlights three interfaces between the major layers. At the top, the API represents the access for developers of application programs to the user interface and other system libraries. The interface between user mode and kernel mode consists of system calls to the operating system kernel.
  Finally, the kernel communicates with the hardware through hardware interfaces.
- None of these modules can be completely self-contained and there will be links among them – any module may need more memory or need to create processes
## New highlights added March 24, 2025 at 10:28 AM
- Linux has a monolithic kernel, which means that any routine inside the kernel can call on any other. Other operating systems have tried to achieve greater reliability and security by enforcing greater modularity. One approach has been to design a microkernel, which contains only the minimum essential elements
- t and a special interprocess communication (IPC)
- microkernels are inefficient
- . Both macOS and Windows can be considered hybrid microkernels: they aim for similar design principles of strong modularisation and support low-level IPC, but much of the OS runs in kernel mode for efficiency.
- A virtual file system (VFS) module now deals with as much of the common functionality as possible,
- As far as possible, most operating system designers try to ensure that their OS will run on a wide variety of platforms or architectures
- One way to make support for several architectures easier is to introduce another layer into the OS design immediately above the hardware. This is called a hardware abstraction layer or ‘architectural dependent code’
- Only this part needs changing
- makes virtualisation easier.
- A related problem faced by OS designers is how to deal with the variety of hardware devices and peripherals that might be part of a computing system
- For a more open system, it is necessary to add modules and device drivers dynamically to the kernel
- Windows uses DLLs (dynamic-link libraries) to add kernel-mode drivers. Linux uses loadable modules with the extension .ko located in subdirectories of /lib/modules.
- Linux commands that can be used to manage loadable kernel modules
- lsmod (list modules) command lists all the currently loaded kernel modules. The modprobe (module probe) command can be used to load and unload modules,
- On Linux, the GUI and windowing system is less tightly linked to the underlying OS than is the case with Windows and macOS, and there is considerable flexibility in the look and feel of the resulting GUI.
- A Linux desktop environment depends on several underlying components, for example a window manager and a widget toolkit
- g window system is responsible for keeping applications visually separate
- The widget toolkit provides the buttons and controls that allow application developers to produce applications with a unified look and feel
- The desktop environment itself enhances that by providing additional features such as a clipboard that works across applications.
- Underlying most Linux desktop environments is usually the same basic display system, X11,
- e X Window System, also known as X11
- Overall it manages the communication between an application and the display and input devices.
- Although X11 could be a complete GUI, its lack of features makes it most useful now as an underlying display protocol.
- A project has been running for some years to develop an alternative to X11 called Wayland,
- A multi-user system like Linux could run X11 for more than one user, but a typical configuration for a personal computer would be to boot directly (or via an initial log in prompt) to a single X11 session.
- A session manager handles starting new applications for that user.
- X11 handles the task of making sure that output from different applications is kept separate, but this can be done in several different ways and is the responsibility of another component, the window manager.
- can be stacked over each other, and most window managers show overlapping stacked windows
- tile the windows so that the display is divided up into non-overlapping windows.
- A variant on a stacking window manager is a compositing window manager. Compositing relies on the ability of graphics hardware to merge images and produces a desktop where windows show transparency, drop shadows and other effects
- X11 now delegates these operations direct to hardware
- hat there are several places in which an individual user or a distro builder can customise the look
- window manager
- widget set
- choices of colour, icons and fonts through themes.
- The range of possible graphical interfaces on Linux is very large,
- The default Raspberry Pi Desktop window manager is a customised version of LXDE, and the only session manager provided is Openbox
- Experience has shown software designers that layering and modularisation are important techniques in designing and implementing robust and portable software, especially in complex cases such as operating systems.
