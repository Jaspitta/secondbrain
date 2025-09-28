It is an [[IPV4 addressing]] that sends a packet to a group of devices that subscribed to a [[multicast group]]. 224.0.0.0 to 239.255.255.255 is reserved for such messages.

The receivers are called [[multicast client]]s, one common protocol is [[OSPF]] which uses 224.0.0.5 and in general the packets in a [[multicast transmission]] are actually [[broadcasted]], the difference is that only the [[multicast client]] will process the message, the others will discard it.

Just like [[broadcast transmission]] and [[unicast transmission]], [[multicast transmission]] can also be referred to [[MAC address]]. While in the other two cases there are no differences, for [[multicast transmission]] the destination address is 01-00-5E when the encapsulated packet is [[IPV4]] and 33-33 when it is [[IPV6]]. 

