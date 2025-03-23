there is no black and white definition for an [[operating system]], in some sense we can say that it makes the [[hardware]] of a computer a usable system, we can however start with defining the main functions:
- provide a [[user interface]] to load and run programs, sometimes a [[CLI]] or a [[GUI]]
- manage storage
- support multitasking
- achieve [[device independence]]

When a regular user boots an [[operating system]] the result is usually the view of the [[desktop]] which is a great metaphor to help regular users understand the system. This however is not the full view of it but simply one possible view organised with one specific purpose.

One of the main characteristics of an [[operating system]] is that it is structured into layers. The component that is used to start programs is referred to as a [[shell]], there are many types but regardless of the one being used the underlying operations are performed by the [[operating system]] so they remain the same.
Regardless of the method, the key concept is that there are different layers communicating with each other:
![[Pasted image 20250320175143.png]]
data flows between these layers in both directions, operations can be initiated by a user so using a [[shell]] but also by an application program, regardless there is no direct communication with the [[hardware]] and this is the key concept of [[device independence]], all [[hardware]] should work with all [[application program]] as long as the [[operating system]] mediates.
Notice that a [[shell]] can be interpreted as simply another application program and in fact it is one, it gets loaded at the end of the [[boot process]] but it can be replaced by a different one if needed and it is no concern for other programs.

It is important to distinguish [[application program]]s and [[utility program]]s, the former are extra software that is added by the user or similar while the ladder are pieces of software that are included in the [[operating system]] even though they do not aid at the core functioning of it like TaskManager or Settings on [[Windows]].

Another important function of the [[operating system]] is [[multitasking]] in part also possible thanks to [[device independence]]. Different programs need to run at the same time, sharing the same [[hardware]] underneath, the [[operating system]] has to make sure that the resources are available to each program when needed and there is no interferences between them.
Ensuring such standards is possible because the [[operating system]] has access full access to the resources and manages them for the [[application program]]s that run on top of it, such power is given by the [[CPU]] itself, in fact regular program run in what is called [[user mode]] while the [[operating system]] run in [[kernel mode]] which gives it such powers. When specific operations are performed, the application program has to pass the torch to the operating system since they are not possible in [[user mode]], the most common example is [[I/O operations]]. To be precise only some parts of the [[operating system]] needs such privileges and they are in fact called the [[kernel]].
![[Pasted image 20250321133903.png]]

The state of the [[execution mode]] is set in a specific [[bit]] of a [[register]] in the [[CPU]], application programs can not change this bit, they have to ask permission to the [[operating system]] with a [[system call]] which will change the state, perform the operation and restore it with the [[return instruction]].
A similar occurrence happens when an [[interrupt]] is triggered.
The [[routine]]s triggered by a [[system call|syscall]] or an [[interrupt]] are the only instructions that gives access to critical resources and those set of instructions are called the [[kernel]] of the [[operating system]].
These [[routine]]s where very few previously, modern operating systems offer a library full of [[API]]s for developers and the library perform [[system call|syscall]]s only when necessary.

We have introduced the use of [[API]]s or [[interface]]s in general, wether it is for hardware or software, which provide a defined way to interact with devices or functionalities. In this sense, interfaces can also be called [[module]]s, especially when talking about [[software]], so we can define the operating system into modules:
![[Screenshot 2025-03-22 at 16.13.59.png]]

This layering can be more or less pronounced, in [[linux]] for example there is a [[monolithic kernel]], each module can talk directly to each other. Some operating systems use a [[microkernel]], it has only the bare minimum and a [[special interprocess communication]] for modules to talk, this is potentially more secure and reliable but require more context switching and is therefore slower. [[Windows]] and [[macOS]] use a combination of those two models.

Back to the topic of [[device independence]], we said that as long as the [[operating system]] mediates every [[application program]] can talk to every [[hardware]], however the [[operating system]] has to support such hardware as well. This is achieved adding another layer on top of the hardware called [[hardware abstraction layer]] which change based on the hardware, it also makes [[virtualization]] easier, however not all operating systems care much about such feature.
On some devices, the hardware installed can even change so the kernel modules necessary must be loaded dynamically, windows uses [[DLL]] files while linux uses [[.ko]] files which are [[loadable modules]] in /lib/modules that can be loaded with `modprobe` or viewed with `lsmod`