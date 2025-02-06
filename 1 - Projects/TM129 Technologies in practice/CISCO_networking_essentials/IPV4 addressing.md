
One particularity of [[IPV4 addressing]] is that each address will have a [[network component]] and a [[host components]].
Devices in the same network share the same [[network component]] portion but will have a different [[host components]]. What identify the network is therefore the [[network component]] and that part for the whole network is called the [[subnet mask]].

Not all address can be used for everything, depending on the transmission some addresses are reserved. A [[public IPV4 address]] is globally routed between [[ISP]]s while [[private IPV4 address]]es are reserved for internal use in organization. When talking to the [[internet]] there is at some point the need to translate between public and private IP4 addresses, this is done by a [[Network Address Translation]] inside a [[router]].

The [[RFC 1918]] establishes the ranges for private addresses as:
- 10.0.0.0/8-10.255.255.255/8
- 172.16.0.0/12-172.16.255.255/12
- 192.168.0.0/16-192.168.255.255

[[public IPV4 address]]es are managed by [[Internet Assigned Numbers Authority]] which manages and allocates IPs on [[Regional Internet Registries]] of which there are 5 and which allocate address to [[ISP]]s for use.