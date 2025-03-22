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

It is importa to distinguish [[application program]]s and [[utility program]]s, the former are extra software that is added by the user or similar while the ladder are pieces of software that are included in the [[operating system]] even though they do not aid at the core functioning of it like TaskManager or Settings on [[Windows]].

Another important function of the [[operating system]] is [[multitasking]]. Different programs need to run at the same time, sharing the same [[hardware]] underneath, the [[operating system]] has to make sure that the resources are available to each program when needed and there is no interferences between them.
Ensuring such standards is possible because the [[operating system]] has access full access to the resources and manages them for the [[application program]]s that run on top of it, such power is given by the [[CPU]] itself, in fact regular program run in what is called [[user mode]] while the [[operating system]] run in [[kernel mode]] which gives it such powers. To be precise only some parts of the [[operating system]] needs such privileges and they are in fact called the [[kernel]].
![[Pasted image 20250321133903.png]]

