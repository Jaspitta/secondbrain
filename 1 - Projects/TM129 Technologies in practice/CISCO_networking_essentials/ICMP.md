---
linklist:
  - "[[ICMPv6 neighbor discovery]]"
  - "[[Internet Control Message Protocol]]"
---


It is a [[protocol]] that works in conjunction with [[transmission control protocol|TCP]] to enrich the [[IP protocol]] and provide more reliability plus error management but it is not a default behaviour of [[IP protocol]] as it remains a [[best effort]].

This [[protocol]] comes as [[ICMPv6]] or [[ICMPv4]] based on which [[IP protocol]] version is being used, they are similar but the v6 has more functionalities, they have lots of messages but the most important are:
- [[ICMP Echo]]: designed to test the [[reachability]] of a host, it uses a [[Echo request]] and [[Echo reply]] message, it is the basis of the [[ping]] command
- [[Destination Unreachable]]: if a [[router]] or [[host]] receive a message that can not be delivered for some reason this message is sent back with an [[error code]] that should explain the reason why:
	- 0: net unreachable for v4 no route for v6
	- 1: host unreachable for v4 firewall block for v6
	- 2: protocol unreachable for v4 beyond scope for v6
	- 3: port unreachable for v4 address unreachable for v6
	- 4: nothing for v4 port unreachable for v6
- [[Time Exceeded]]:  sent when the [[time to live]] or [[hop limit]] fields are exceeded, used by the [[tracert]] utility. This utility actually sends sequential [[packet]]s, the first will have a [[time to live]] of 1, the second of 2 and so forth, this way it will stop at every [[hop]] and get a reply [[Time Exceeded]] from it 

[[ICMPv6 neighbour discovery]] is enriched with extra feature and message:
- [[Router Advertisement|RA]]: sent by enabled routers every 200 seconds, contains info that [[host]]s that use [[StateLess Address AutoConfiguration]] can use to setup their [[IPV6 configuration]]
- [[Router Solicitation|RS]]: request sent by hosts to get a [[Router Advertisement|RA]] message back
- [[Neighbor Advertisement|NA]]: response to a [[Neighbor Solicitaiton|NS]], the host reply with it's [[MAC address]] just like an [[ARP reply]]
- [[Neighbor Solicitaiton|NS]]: when a host does not know that [[MAC address]] but only the [[IPV6]] of another host, like [[ARP request]]