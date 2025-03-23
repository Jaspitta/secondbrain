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
