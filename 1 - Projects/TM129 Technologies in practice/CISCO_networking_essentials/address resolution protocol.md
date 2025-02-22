It is quite common for a host that wants to send a message to have the [[ip address]] of the destination but not the [[MAC address]].
Remember that the full packet will have the [[layer 2]] [[physical address]] that encapsulate the [[layer 3]] [[ip address]].

If the packet is destined for an external device, the [[MAC address]] will be simply the one of the [[default gateway]] if it is in the [[ARP table]], otherwise it will send an [[ARP request]] to recover the [[MAC address]]. To be precise, when the packet reaches the [[default gateway]], this device de-encapsulate the packet, read the [[ip address]] of destination, determines the best next device to reach, replace the [[layer 2]] information with the new information of the next device and so forth, until the packet gets to destination.

To know which [[MAC address]] should be replaced in the packet knowing the [[ip address]], there is the [[address resolution protocol]] for [[IPV4]] and the [[ICMPv6 neighbor discovery]] for [[IPV6 addressing]].

When a [[host]] wants to send a packet to a [[host]] but only has the [[IPV4]] address, the first thing it does it look into the local [[ARP table]] to see if there is a match for that address, if not it sends an [[ARP request]]. This is a [[broadcast transmission]] so all devices will receive the packet, in this special packet there is no [[ip header]] and there is a field called a [[type]] which identify the [[packet]] as an [[ARP request]], in this case it is [[0x806]].
If one of the hosts in the network has the [[IPV4]] address inside the [[broadcast transmission]] it will reply with a [[unicast transmission]] [[ARP reply]] containing the [[MAC address]], and again the [[type]] field set to [[0x806]], the requesting host will hold that information inside its local [[ARP table]], it knows it is a reply because of the [[type]] field.

This process is of course not exclusive to remote hosts, this very well happens for local hosts because the is still the need to be able to get the [[MAC address]] from the [[ip address]] when sending a [[packet]].

In general entries inside the [[ARP table]] have a [[time to live]], so if no packets are received or sent for a while the entry will be removed for windows we are talking about 15 to 45 seconds.

In [[IPV6]] there is a similar process called [[ICMPv6 neighbor discovery]].

One security risk of [[address resolution protocol]] is the possibility of bad actors to impersonate the [[default gateway]], someone can simply reply to an [[ARP request]] directed to it and insert it's [[MAC address]] to receive future [[packet]]s