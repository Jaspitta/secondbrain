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

There are tree types of addresses:
- [[unicast]]: one to one, a source can only be [[unicast]], there are many types:
	- [[global unicast]]: like a [[public IPV4 address]]
	- [[link local]]: obtained statically or dynamically, unique on the [[local network]] or [[link]], ignored by [[router]]s but mandatory for every interface, are in the range of $fe80::/10$. The [[link local]] of the [[router]] become the [[default gateway]] and in between [[router]]s they use their [[link local]] to exchange [[routing protocol]] info. Configured with `ipv6 address address link-local` or when generated dynamically using [[EUI-64]] or random
	- [[loopback]]: ::1/128
	- [[unspecified]]: '::'
	- [[unique local]]: from $fc00::/7$ to $fcff::/7$, not yet used, intended for devices that should be unreachable from outside
	- [[embedded]]
- [[multicast]]: one to many, prefix $ff00::/8$:
	- [[well-known multicast]]: assigned addresses to for pre defined groups, $ff02::1$ for [[all-nodes]] equivalent of [[IPV4]] [[broadcast]], $ff02::2$ for [[all-routers]] like a [[broadcast]] but only for [[router]]s on the same network, used for [[Router Solicitation]] messages
	- [[solicited-node multicast]]: special type of [[multicast]] [[all-nodes]] but can be filtered at [[layer 2]], so if the packet is not for you it does not get to [[network layer|layer 3]]
- [[anycast]]: one to many, the address can be given to many devices, only the first will receive it though

there is not actual [[broadcast]] address but there is a [[all-nodes]] address that gives the same functionality.

[[IPV6]] also has a [[network prefix]], it is only represented with [[slash notation]], can go from 0 to 128 and the recommended size is 64 so half the address.

To view info on you router [[IPV6 addressing]] you can use the command:
- [[show ipv6 interface brief]]
- [[show ipv6 route]]
- [[ping]]