It is the [[layer 3]] of the [[OSI model]].

It's function is to allow devices to exchange data across different [[network]]s, the most common implementations are [[IPV4]], [[IPV6]], [[Open Shortest Path First]] or  [[Internet Control Message Protocol]].
This layer does [[addressing]], [[encapsulation]], [[routing]] and [[de-encapsulation]].
The [[encapsulation]] part is always performed by the [[source]] which adds the source and destination [[ip address]] as headers.

The [[router]]s operate at this layer, it choose the shortest path to get to the destination and each [[router]] that a [[packet]] crosses is called a [[hop]].

At this layer, there is no concern with the content of the [[packet]], all the service is dedicated to moving the packet around.

The [[IP protocol]] is the most used by far at this layers and mostly for the higher performance it delivers. It has drawbacks because it is [[connectionless]], [[best effort]] and [[media independent]] but this characteristics gives higher performance also.
The only dependence on the [[media type]] it has is the [[maximum transmission unit]], the [[data-link layer]] passes the [[maximum transmission unit]] to the [[network layer]], this way it knows the maximum size of each [[packet]] and in some cases a [[router]] is also tasked of splitting the packet in case it exceed the [[maximum transmission unit]], this is called [[fragmentation]].

The header of the [[IPV4 packet]] is actually more than just [[source]] and [[destination]], it is in total 20 bytes long:
- 1 byte: version (0100) + [[internet header length]]
- 1 byte: [[differentiated service]] or [[DS]], made of [[differentiated services code point]] (6 bit) and [[explicit congestion notification]] (2 bit), used for packet priority
- 2 byte: total length
- 2 byte: identification
- 2 byte: flag (4 bit) + [[fragment offset]] (12 bit)
- 1 byte: [[time to live]], sat by the source it is the max number of [[hop]]s a packet can take, if a [[router]] see it at 0 it discard the packet and send a [[Internet Control Message Protocol]] to the [[source]]
- 1 byte: number that identify the [[protocol]] of the data portion ([[UDP]] is 17 and [[TCP]] is 6)
- 2 byte: [[header checksum]], recalculated at every [[hop]] because the [[time to live]] change
- 4 byte: [[source address]]
- 4 byte: [[destination address]]

The header can actually have an additional 40 bytes dedicated to optional fields and padding if needed