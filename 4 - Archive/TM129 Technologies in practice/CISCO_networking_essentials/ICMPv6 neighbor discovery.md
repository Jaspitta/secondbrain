It is similar to [[address resolution protocol]] but uses [[Neighbor Solicitaiton]] and [[Neighbor Advertisement]] messages.

Each [[host]] has a [[neighbor cache]], similar to an [[ARP table]] that maps [[IPV6 addressing]] with [[MAC address]] for hosts in the same network. If a host is about to send a message to another host on the same network (established looking at the [[ip address]]) but does not have the [[MAC address]] in it's [[neighbor cache]], the [[packet]] is put on hold.
The host creates a [[Neighbor Solicitaiton]] message, it has an [[ICMPv6 NS header]] which contains the target of the host we want to know the [[MAC address]] of, incapsulated in an [[IPV6 packet]] with a [[solicited-node multicast]] destination address (no router forwarding because the scope is [[link local]]), incapsulated in an [[ethernet frame]] with [[destination multicast]] destination.
All hosts receive the packet, since the [[ethernet frame]] has a [[destination multicast]] no host needs to go above [[layer 2]] to know if the packet is for them, once the right host receive the packet it will add the source [[MAC address]] and [[IPV6]] to it's [[neighbor cache]].
The target host now reply with a [[Neighbor Advertisement]] message, sent with [[global unicast]] to the source host, it will also add it's [[MAC address]] in the message of course.
Finally, the source host can update it's [[neighbor cache]], remove the initial [[packet]] from hold and send it with the correct destination [[MAC address]].

Note that if the host where to be on a remote network, the process would be the same, simply the final mapping would be that of the [[MAC address]] of the [[default gateway]], the messages are simply called [[Router Solicitation]] and [[Router Advertisement]] instead.

Counterintuitively, communication between two routers is with [[Neighbor Solicitaiton]] and [[Neighbor Advertisement]] messages, in essence if the devices are of the same time [[Neighbor Solicitaiton]] and [[Neighbor Advertisement]] are used, if they are of different type ([[host]] to [[router]]) for example, [[Router Solicitation]] and [[Router Advertisement]] messages are needed.



