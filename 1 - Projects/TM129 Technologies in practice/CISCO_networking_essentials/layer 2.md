---
aliases:
  - data link layer
---

Since it prepares network data for the [[physical layer]], it has to know the [[topology]] of the network, we distinguish two of these:
- [[physical topology]]: usually [[point to point communication]], [[hub and spoke]] and [[star|mash]] for [[WAN]] and , [[star]] or [[star|mash]], [[extended star]], [[ring]] and [[bus]] for [[LAN]],  describe the physical connection and location
- [[logical topology]]: describe the way a network transfer data from node to node, usually include addressing informations of the single devices but can also include much more


[[duplex communication]] describe the direction of data between two devices, with [[half-duplex]] data can travel both ways but only one at the time while [[full duplex]] means that data can travel both ways at the same time. Two communicating [[network interface card]]s must use the same type of [[duplex communication]] otherwise inefficiencies will rise.

[[LAN]]s and [[WAN]]s are [[multiaccess network]]s so two devices could be attempting to access the network simultaneously, today almost all use a [[full duplex]] so there is no problem, however, when that was not so common there where two ways to control access to the [[media]]:
- [[contention-base access]]: there is a process managing access to the [[half-duplex]]:
	- [[CSMA/CD]]: for [[WLAN]]s and legacy [[bus]], the [[network interface card]] detect amplitudes outside the norm and declare the message invalid so it has to be resent
	- [[CSMA/CA]]: devices broadcast the time needed for sending a message before actually sending it so other know for how long the medium will be taken, the receiver will also send an acknowledgment at the end.
- [[controlled access]]: time based access, devices need to wait their turn to communicate, used in the legacy [[ring]] and [[arcnet]]

