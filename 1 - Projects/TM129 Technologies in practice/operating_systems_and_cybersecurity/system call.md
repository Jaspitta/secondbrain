---
aliases:
- syscall
---

It is a special [[machine instruction]] performed by a program running in [[user mode]] when it needs to do some operations in [[kernel mode]].
The program asks the [[operating system]] to perform such instructions, this operation switches the operating system to [[kernel mode]], perform the necessary task and finally restore the state with the [[return instruction]].
During the execution, control is passed to the operating system, the program has to wait for those instructions to be carried out before getting control back