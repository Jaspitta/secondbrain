In a [[virtual machine]] we have a [[host operating]] system in which a software called [[hypervisor]] manage the virtual hardware on which the single [[guest operating systems]] run.

In a graph we would have:
hardware -> host OS -> hypervisor -> virtual hardware -> guest OS -> apps

One of the biggest advances in virtualisation in the advent of [[containerisation]], in this model instead of creating virtual hardware and a new OS every time, the host OS is divided in spaces (memory blocks) called containers in which applications can run.
The structure is:
hardware -> host OS -> (division) -> container manager -> virtual OS -> apps

This allows for much lighter environment to run applications with less overhead. The container manager divides the space into independent blocks and assign them to the virtual environments, plus it also works with a [[microkernell]] which manage the low level interactions with the hardware.
The main difference is that there is no need for the virtual hardware and most importantly for the guest OS, this significantly reduces memory, resources and boot times compared to virtual machines.
Another big advantage of container is [[portability]], every [[container]] has all it needs to run if there is a [[container manager]] underneath, therefore once you set up your environment in a container you can bring it to any machine and run it.
It is not all positives though, containers all share the [[microkernell]], so if one [[container]] has a security breach it can propagate also to the others and the main machine, virtual machines on the other hand are much more isolated and do present such risks.
Overall, considering the speed, agility and [[portability]] of containers, even wit the risks that they brings, it should be easy to see how they are such a good fit for [[cloud computing]] and [[DevOps]] even more.

The main player in the space is [[Docker]]