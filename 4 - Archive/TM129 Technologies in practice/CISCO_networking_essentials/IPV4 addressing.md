
One particularity of [[IPV4 addressing]] is that each address will have a [[network component]] and a [[host components]].
Devices in the same network share the same [[network component]] portion but will have a different [[host components]]. What identify the network is therefore the [[network component]] and that part for the whole network is called the [[subnet mask]].

Not all address can be used for everything, depending on the transmission some addresses are reserved. A [[public IPV4 address]] is globally routed between [[ISP]]s while [[private IPV4 address]]es are reserved for internal use in organization. When talking to the [[internet]] there is at some point the need to translate between public and private IP4 addresses, this is done by a [[Network Address Translation]] inside a [[router]].

The [[RFC 1918]] establishes the ranges for private addresses as:
- 10.0.0.0/8-10.255.255.255/8
- 172.16.0.0/12-172.16.255.255/12
- 192.168.0.0/16-192.168.255.255

[[public IPV4 address]]es are managed by [[Internet Assigned Numbers Authority]] which manages and allocates IPs on [[Regional Internet Registries]] of which there are 5 and which allocate address to [[ISP]]s for use.

##### configuration

Configuring an [[IPV4]] can be done manually or automatically, when done manually the administrator need to set, [[IPV4 address]], [[subnet mask]] and [[default gateway]].
Manual configuration can be error prone and time consuming but it still might make sense for a [[device]] that does not move and needs to simply be called like a printer for example.

For devices that moves or change like laptops we use [[Dynamic Host Configuration Protocol server]] which assign info automatically, this also allows for address to be reused as they are only leased for the time the device stays connected to the network, after that they are reclaimed by the server.
Many home and office [[router]]s are both client and DHCP servers, they provide IPs for the local network but also asks for them to the [[ISP]] [[Dynamic Host Configuration Protocol server]].

The [[client]] sends out a [[broadcast transmission]] called [[DHCP discover]] with the [[MAC address]] of the sender, the [[Dynamic Host Configuration Protocol server]] respond with a [[DHCP offer]] which the [[client]] can use to configure it's [[IPV4 address]]. The offer message contains the [[IPV4 address]], [[subnet mask]] and [[default gateway]]. The [[client]] finally send a [[broadcast transmission]] [[DHCP request]] and request the IP that was offered in the previous message and the [[server]] sends a [[DHCP acknowledge]].

Remember that the [[ip address]] that you see configured on the router is usually what the other devices will se as [[default gateway]]