---
aliases: 
 - RA
---

It is sent to the [[IPV6 addressing]] [[multicast]] address $ff02::1$, source will be the [[link local]] address of the [[router]].

This message include the [[network prefix]], the [[domain name system|DNS]] address and the flags [[autoconfig]], [[other config]] or [[managed config]]. When flag [[autoconfig]] is enabled this will activate [[StateLess Address AutoConfiguration]].
The host will randomly create a [[host components]] for the address and add it to the [[network prefix]] so up to this point the server is completely [[stateless]].