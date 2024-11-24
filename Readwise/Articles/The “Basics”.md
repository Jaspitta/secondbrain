# The “Basics”

![rw-book-cover](https://cpu.land/banner.png)

## Metadata
- Author: [[Lexi]]
- Full Title: The “Basics”
- Category: #articles
- URL: https://cpu.land/the-basics

## Highlights
- The first mass-produced CPU was the [Intel 4004](http://www.intel4004.com/), designed in the late 60s by an Italian physicist and engineer named Federico Faggin ([View Highlight](https://read.readwise.io/read/01hc0sta8rpy0k2vs7s9jnemw4))
- instruction pointer ([View Highlight](https://read.readwise.io/read/01hc0tj684s1ne0m11th94v42e))
- fetch-execute cycle ([View Highlight](https://read.readwise.io/read/01hc0tj8w97e0y85xk6bxxdrdj))
- Some instructions can tell the instruction pointer to jump somewhere else instead ([View Highlight](https://read.readwise.io/read/01hc0tvta6xzvqrebq61a9kpaj))
- instruction pointer is stored in a [*register*](https://en.wikipedia.org/wiki/Processor_register). Registers are small storage buckets that are extremely fast for the CPU to read and write to ([View Highlight](https://read.readwise.io/read/01hc0tx551gs20xqhtmnn50fn6))
- machine code in a file somewhere. The operating system loads this into RAM ([View Highlight](https://read.readwise.io/read/01hc0v2kx26s8djr8nx33xyk44))
- CPUs have a super basic worldview; they only see the current instruction pointer and a bit of internal state. Processes are entirely operating system abstractions ([View Highlight](https://read.readwise.io/read/01hc0v3ydmyf5f2afrefhmp6wt))
- When you boot up your computer, the instruction pointer starts at a program somewhere. That program is the kernel ([View Highlight](https://read.readwise.io/read/01hc0vfb2abpeemat2wq391t4e))
- Linux is just a kernel ([View Highlight](https://read.readwise.io/read/01hc0vg204y7qfhkpgpyqmfh58))
- Processors start in kernel mode. Before executing a program, the kernel initiates the switch to user mode. ([View Highlight](https://read.readwise.io/read/01hc0vjx5y8kqsvt7ge99dp9gx))
- privilege level (CPL) can be read from a register called `cs` (code segment) ([View Highlight](https://read.readwise.io/read/01hc0vkgekems6mas8tf4dt4em))
- 0 is kernel mode and ring 3 is user mode ([View Highlight](https://read.readwise.io/read/01hc0vn7k82sh5qn7kfh14f5kt))
- software running in user mode has to ask the operating system kernel for help ([View Highlight](https://read.readwise.io/read/01hc0vr20be0b6s2xtfarvf3rm))
- A system call is a special procedure that lets a program start a transition from user space to kernel space, jumping from the program’s code into OS code. ([View Highlight](https://read.readwise.io/read/01hc0vqsb95smdtg3szbfmwthj))
- userland programs can use an instruction like [INT](https://www.felixcloutier.com/x86/intn:into:int3:int1) which tells the processor to look up the given interrupt number in the IVT ([View Highlight](https://read.readwise.io/read/01hc0w54agz1gmptwsbh0fxb19))
- When you call `exit(1)` from C running on a Unix-like system, that function is internally running machine code to trigger an interrupt, after placing the system call’s opcode and arguments in the right registers/stack/whatever. Computers are so cool! ([View Highlight](https://read.readwise.io/read/01hc0wbxjqd7t6eye7f1ws0e9y))
- Processors execute instructions in an infinite fetch-execute loop ([View Highlight](https://read.readwise.io/read/01hc0wm6d38avfg65q44zh5qs6))
- System calls are a standardized way for programs to switch from user mode to kernel mode and into OS code. ([View Highlight](https://read.readwise.io/read/01hc0wnc0g32h8rnczapp2w4rn))
    - Note: And trigger software interrupts underneath
- Programs typically use these syscalls by calling shared library functions ([View Highlight](https://read.readwise.io/read/01hc0wqa79bfd0y0gkrf0mqyb4))
