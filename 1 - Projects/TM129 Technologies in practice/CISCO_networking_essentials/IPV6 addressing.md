It is the successor of [[IPV4 addressing]] with 128-bit of address space.
It has [[Internet Control Message Protocol]] that supports address resolution and auto-configuration unlike the equivalent 4.

The [[IPV4 addressing]] has three main problems:
- [[address depletion]]
- [[end to end connectivity]]: while [[Network Address Translation]] makes possible for hosts to share one [[public IPV4 address]], it means that the [[private IPV4 address]] remain invisible to the outside making [[end to end connectivity]] problematic
- complexity: while [[Network Address Translation]] extended the life of [[IPV4 addressing]], it added complexity making the protocol less efficient

[[IPV6 addressing]] solves this problems, [[address depletion]] is not realistic, [[Network Address Translation]] is not needed and the [[header]] fields are simplified, [[internet header length]], [[identification]], [[flags]], [[fragment offset]], [[header checksum]] and padding are removed plus others are moved or renamed. The final header is largely simplified with 40 bytes:
- 4 bytes: version (4 bit 0110) + [[traffic class]] (1 byte equivalent [[differentiated service]]) + [[flow label]] (20 bits type of handling by [[router]])
- 2 bytes: [[payload length]]
- 1 bytes: [[next header]] (8 bits) identify the [[protocol]] of the [[payload]] 
- 1 byte: [[hop limit]] (9 bits) equivalent of [[time to live]]. Because there is not [[header checksum]] it does not have to be recalculated, the check is done at [[transport layer]] and [[data-link layer]]
- 16 bytes: source ipv6
- 16 bytes: dest ipv6

There is the possibility to have additional [[extension header]] but the [[router]] does not do [[fragmentation]] with [[IPV6]]

Migrating to IPV6 is strongly advised but it does not have a deadline, the IETF developed tools to help the transition and the techniques are of three types:
- [[dual stack]]: devices run both [[IPV4 addressing]] and [[IPV6 addressing]] and the IPV6 is native
- [[tunneling]]: an [[IPV6 packet]] is [[encapsulation|encapsulated]] in an [[IPV4 packet]]
- [[translation]]: using a [[NAT64]] which transform packets between the two protocols

The format of this addresses is $x:x:x:x:x:x:x:x$ where each $x$ is made of 4 [[hexadecimal]] values so 16 bits, this is known as the [[preferred format]].
To shorten the length leading 0 are omitted, so a [[hextet]] at say $00aa$ can be written as $aa$, also if a [[hextet]] is made of only 0 it can be fully omitted, and if there is more than one in a row they all are replaced by $::$, however this last technique can be used only once for the address otherwise it would be ambiguous