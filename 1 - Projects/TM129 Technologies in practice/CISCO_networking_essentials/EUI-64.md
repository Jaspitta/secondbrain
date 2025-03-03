---
aliases:
- extended unique identifier 64
---

It is a process defined by the [[IEEE]], it uses the 48 bit [[MAC address]] split it in the middle between the [[OUI]] and [[device identifier]] and add $fffe$ in the middle.
This makes easy to identify the [[MAC address]] from the [[global unicast]], but this can also cause security concerns in some cases.

Because of this concerns many [[operating system]]s now generate the [[host portion]] randomly, to guarantee uniqueness there is a process called [[duplicate address]], if there is no reply to the address it means it is free
