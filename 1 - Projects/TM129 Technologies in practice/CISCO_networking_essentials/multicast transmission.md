It is an [[IPV4 addressing]] that sends a packet to a group of devices that subscribed to a [[multicast group]]. 224.0.0.0 to 239.255.255.255 is reserved for such messages.

The receivers are called [[multicast client]]s, one common protocol is [[OSPF]] which uses 224.0.0.5 and in general the packets in a [[multicast transmission]] are actually [[broadcasted]], the difference is that only the [[multicast client]] will process the message, the others will discard it.

