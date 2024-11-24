The invention of [[encryption]] and [[asymmetric encryption]] made much more possible to have secret conversations also for military purposes. However, when you send an [[encrypted]] message, expecially if you send many over time, you might reveal patterns related to locations and more about yourself.
This brought the invention of the [[tor network]], a [[network]] designated to send messages through an always changing chain of relays and other anonymous computers to maintain secrecy. Because of the way this network works it can not be kept secret, it needs other endpoints to participate in the network.

#### [[tor browser]]

The tor network has many special requirements compared to a regular [[network]] and for many of these it requires a special [[browser]], for this reason if you want to use this network you need to first download the [[tor browser]] to do so.
The first thing that is done by this [[tor browser]] during installation is the creation of a personal unique [[asymmetric key]] pair stored in a [[local secure vault]].

For messages to go from source to destinations they have to travel via one of the core building blocks of the [[tor network]] which are the [[tor node]]. At heart they are nothing more than someone else pc connected also to the tor network.
Therefore to get to a destination you need to pass a series of [[tor node]]s which form a so called [[tor circuit]]. Such nodes are gathered in a [[directory node]] when they start and connect to the network.
From the source the data goes to what is called the [[guard node]], than a series of [[tor relays]] and finally the [[exit node]] from which it travels to destination using the conventional [[internet]].

#### tor encryption

The [[encryption]] process has many steps, first the source ask to all the nodes their [[public key]]. Each node generate a session key, pair it with their public key, encrypt it with the source's public key and reply to the source.
At this point the source encrypt the message with all the keys of all the nodes, starting from the most distant one like a matrioska with a minimum of 5 layers (this is where it differs from the conventional internet). Not only this, apart from the [[exit node]], every time the message is encrypted, it also gets added the address of the next node (when source encrypt the message with key of node n, if it is not the exit node it first add the address of node n+1 and than encrypt with node n public key).
![[tor message encryption]]
When a [[tor node]] receive a message it uses its private key to unpack it. This reveal more [[ciphertext]] and the address of the next node, in this way each node only knows the address of the previous and next node but never knows if one of these is the [[source node]], [[destination node]] or just a relay.
All this process is called [[onion routing]] due to the multitude of layers and the message [[encrypted]] is called a [[tor onion]].
The response message follow the same logic but uses [[symmetric encryption]]with the [[session key]] that was generated in the beginning, each node encrypt the message with its [[session key]] and forwards it to the next, the source will have to decrypt using all the session keys in revers order.

Ideally [[onion routing]] and [[tor onion]]s should change at every message with a new [[tor circuit]] being established each time, however, due to the high computation cost, the circuit might be held for up to 10 minutes before being destroyed.