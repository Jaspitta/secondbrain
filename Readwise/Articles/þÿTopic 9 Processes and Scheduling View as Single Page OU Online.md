# þÿTopic 9   Processes and Scheduling: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/290508912/1hTadwP0KaC_87bj7V8jLGMgMrGQki0zX0OAymybrT4-cove_4lj6MeJ.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 9   Processes and Scheduling: View as Single Page | OU Online
- Category: #articles
- Summary: The text discusses how operating systems manage multiple processes and scheduling. It explains that an OS uses techniques like context switching and prioritization to allow different applications to run concurrently. Lastly, it highlights the importance of scheduling strategies to ensure smooth user experiences.
- URL: https://readwise.io/reader/document_raw_content/290508912

## Highlights
- One of these major functions is to support multitasking, and I will turn to look at multitasking in this and the next two topics.
- s allow the user to run more than one application program at once.
- operating systems are designed to support multitasking on a single processor
- current chips may only have two or four cores – fewer than the number of programs
- having multiple cores, while improving performance, doesn’t solve the problem of multitasking,
- o programs can be executed in the background at the same time as the program I am working with in the foreground.
- the apparent ability to run more than one program at a time is a grand illusion.
- multitasks by rapidly switching execution
- running hundreds of different processes on only a few processor cores (or even a single core). We should use the more technical term concurrent processes to describe these
- Processes are concurrent if their lifetimes overlap,
- with multiple cores, processes can be running at the same instant, and we could then use the technical term parallel.
- A program is a list of instructions.
- When a program is executed, the operating system loads the instructions into memory, allocates additional memory for data and grants access to other resources such as files and I/O devices.
- creates a process from the program. So a process is a program that is being executed, consisting of the instructions, memory for data and connections to other resources
- A task is an alternative term used for the same concept
- It is quite possible for an operating system to run two or more copies of a single program. To the operating system, each copy would become a separate process
- The operating system manages processes rather than programs
- A software developer can choose to develop a single software application as multiple processes that run concurrently.
- in this case it would be essential that both processes can access the same data:
- Most operating systems therefore provide an alternative to the process. This alternative is called a thread.
- a separate execution of a program, just as a process does, but threads share the memory and other resources allocated to a single process.
- because they share memory and other resources, the operating system can create them more quickly and switch between them more quickly.
- Some software libraries contain their own threading mechanisms, designed to avoid the overhead of using OS threads
- some processors have hardware threading
- effectively invisible to the operating system
- Clearly it’s important to protect one process from another in a multi-user system, but much the same considerations apply to processes in a single-user multitasking system.
- The ps command is the traditional Unix tool used to manage processes
- top and htop, that are similar to the GUI Task Manager in functionality but run from the CLI
- choosing which process to run next and for how long; this is known as scheduling.
- The OS will also impose regular switching to ensure smooth multitasking
- Each process is allowed to run only for a short time-slice, often referred to as a quantum, for example 10 ms.
- process that is replaced by another when its quantum expires is said to have been pre-empted
- Frequent switching is particularly needed for an OS described as a real-time operating system
- something particularly important when software controls equipment
- ‘real time’ should be specified precisely, for example that an event can be detected within 10 ms and handled within 50 ms.
- The scheduler is only concerned with what happens next, that is to make a good choice of which process to run nex
- (FIFO)
- keep a queue of processes.
- The first process in the queue is chosen to run and allowed to run until it completes. New processes join the end of the queue
- h requires a number of quanta to complete
- In a round-robin system, the first process to run is again taken from the queue of waiting processes.
- after a quantum the running process will be pre-empted and returned to the end of the queue.
- perhaps some processes should be treated as more important than others
- data may be lost if they are delayed in the ready queue for too long.
- , each process is given an equal slice of processor time.
- o give each process a priority level, usually expressed as a small number
- The queue of ready processes is now kept as a priority queue: the head of the queue always has the highest priority, and when a new high-priority process joins, it ‘queue jumps’ over lower-priority processes
- a low-priority process may never get a turn.
- A variant is to classify processes into a number of classes of priority and keep a queue for each class.
- The scheduler deals first with the highest-priority queue and then moves to the next highest-priority queue. Within a queue it can use round-robin scheduling to ensure all processes make some progress.
- change priorities dynamically
- I/O is always very much slower than processor speed. If such a process becomes unblocked, then it may be good to give it a priority boost because it is likely to quickly start another I/O operation and so get blocked again, which will allow another process to run. This will keep the I/O devices busy as well as the processor
- System designers have experimented with different scheduling algorithms over the years, and often come up with hybrid designs that combine several techniques from those considered above.
- The Linux scheduling system is based around priority and allows the programmer and user some control.
- lower numbers (higher priority).
- d ‘niceness’ which allows a process to change its own priority or that of another.
- the final process priority is the initial priority and niceness added together. A normal user can’t set a niceness of less than zero, but root (or using sudo) can set niceness to negative values down to −20 to achieve higher overall priority.
- Kernel threads can be given negative priorities
- referred to as real-time processes
- Most Linux versions have several schedulers: one that is used for most ‘normal’ processes, and specialised versions used for high-priority real-time processes.
- A real-time process can be scheduled using one of three different schedulers:
- FIFO
- Round-robin.
- Deadline
- book an amount of CPU time needed before a deadline
- handling audio and video in a buffer
- The current Linux ‘normal’ scheduler is called the Completely Fair Scheduler.
- honours the initial priority and niceness values but adjusts priority dynamically so that all processes get a ‘fair’ slice of CPU
- priorities are continually being adjusted,
- s priority will become higher the longer it is kept waiting.
- n two other specialised Linux schedulers. One is suited for batch processing,
- The other is specifically for an ‘idle’ process
- Ideally it should do no processing, halting the processor to reduce power consumption.
