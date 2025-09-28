It is the [[standard]] for [[local area network|LAN]] cmmunication, even though there is no official documents stating so, it simply became that way for convenience.
The goal is to define how data is transmitted and formatted over the [[wired network]], it operates at [[layer 1]], so [[physical]] and [[layer 2]] so [[data link]] of the [[OSI model]].
The [[standard]] is maintained by the [[IEEE]] with committee [[802.3]], the max standard speed now is 100Gb/s.

Protocols in the 802 standard use two different sublayers of the [[data link]] to operate, one is the [[media access control]] or [[MAC]], the other is the [[logical link control]] or [[LLC]].
The [[MAC sublayer]] is implemented at hardware level, integrate with physical technology, provides the addressing at [[data link]] layer and does encapsulation.
The [[LLC sublayer]] 802.2 works as a middle man between the lower hardware part and the higher software parts, it add the protocol version to the [[ethernet frame]] facilitating for [[ip address]].
They both exist in the [[data link]] layer but the [[MAC]] works at lower level with [[ethernet]], [[Wireless LAN|WLAN]] and [[WPAN]].

