It is the successor of [[IPV4 addressing]] with 128-bit of address space.
It has [[Internet Control Message Protocol]] that supports address resolution and auto-configuration unlike the equivalent 4.

Migrating to IPV6 is strongly advised but it does not have a deadline, the IETF developed tools to help the transition and the techniques are of three types:
- [[dual stack]]: devices run both [[IPV4 addressing]] and [[IPV6 addressing]] and the IPV6 is native
- [[tunneling]]: an [[IPV6 packet]] is [[encapsulation|encapsulated]] in an [[IPV4 packet]]
- [[translation]]: using a [[NAT64]] which transform packets between the two protocols

The format of this addresses is $x:x:x:x:x:x:x:x$ where each $x$ is made of 4 [[hexadecimal]] values so 16 bits, this is known as the [[preferred format]].
To shorten the length leading 0 are omitted, so a [[hextet]] at say $00aa$ can be written as $aa$, also if a [[hextet]] is made of only 0 it can be fully omitted, and if there is more than one in a row they all are replaced by $::$, however this last technique can be used only once for the address otherwise it would be ambiguous