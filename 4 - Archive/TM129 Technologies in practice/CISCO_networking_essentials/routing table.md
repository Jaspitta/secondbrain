It is the table cached in a [[router]] to associate the [[ip address]] of a network with one of it's [[network interface card]].
It can be populated dynamically with information provided by another [[router]] or manually.

You can use the command [[netstat -r]] or [[route print]] to view the [[routing table]]

Entries in a [[routing table]] can be added in two ways:
- [[static routing]]: the route is added by hand and if the [[logical topology]] changes it needs to be updated by hand, the [[default route]] is always entered with [[static routing]]
- [[dynamic routing]]: routers shares and learn routes with a specific [[routing protocol]], no human intervention needed except for enabling the protocol, the protocol can be [[ospf]] or [[eigrp]]. It is important that also the connected [[router]]s use [[dynamic routing]] otherwise it will be useless