---
aliases:
  - layer 4
---

The role of this layer is to guide the exchange of data produced by [[application layer]] programs at different hosts, usually a [[client]] and a [[server]]. It is already detached from any type of concern about the physical characteristics or limitations of the [[network]], it is the intermediate between higher layer concerned with user data and lower layers concerned with the network itself.

The responsibility of this layer are:
- [[tracking conversation]]s: a [[conversation]] here is considered a set of flowing data between source and destination application, this layer has to manage and separate the different [[conversation]]s
- [[segmentation]]: divide data into [[segment]]s or [[datagram]]s for [[network layer]] and reassemble them
- add [[header]]s
- [[identify conversation]]: since more [[conversation]]s can be on the same host it has to separate the data using [[transport layer port]]s
- [[multiplexing]]: uses [[segmentation]] to allow communication multiplexing avoiding congestion from a single [[conversation]]

It includes two protocols [[TCP]] and [[UDP]], these protocols are concerned with how to transfer data between hosts in the sense of [[reliability]] and [[conversation]]s unlike [[network layer]] concerned simply with the routing.

##### [[transmission control protocol]]

This [[transport layer]] [[protocol]] is considered a [[reliable]] and [[full-feature]] protocol because it uses additional [[header]]s to guarantee the delivery at the cost of additional processing. It divides data into [[segment]]s and support the following operations:
- [[number]]: track [[segment]] and match to specific host and application
- [[acknowledge]]
- [[retransmission]]: if no [[acknowledge]] is received it retransmit the [[segment]]
- [[sequence data]]: [[segment]]s might arrive in wrong order
- [[regulate rate]]: send [[segment]] at a rate acceptable for the receiver
To allow for this feature there has to be a connection established between sender and receiver, therefore [[transmission control protocol|TCP]] is considered a [[connection-oriented protocol]].
To achieve all this feature the [[transmission control protocol|TCP]] protocol keeps track of the [[conversation]] with a state where it record what has been sent and what has been acknowledged, the session start with an [[establishment]] and end with [[termination]].
It total it adds 20 bytes:
- 2 byte: source [[port]]
- 2 byte: destination [[port]]
- 4 byte: [[sequence number]] for reassembly
- 4 byte: [[acknowledgment number]] state if data has been received and the next byte
- 4 bit: [[header length]]
- 6 bit: [[reserved]]
- 6 bit: [[control bits]]
- 2 byte: [[window size]], number of bytes that can be accepted at once ([[flow control]])
- 2 byte: [[checksum]]
- 2 byte: [[urgency]]
##### [[three way handshake]] and [[session termination]]

The simplest process is the [[session termination]], one of the hosts set the [[finish control flag]] in the [[header]] and send the [[FIN segment]], the other sends the [[acknowledge]] and [[SYN]] back, than he sends the [[FIN segment]] and the first host finally send his [[acknowledge]], overall two fin and acknowledge exchanges for a total of four messages.

The [[three way handshake]] has the goal of establishing the other device is available, it has an active service and also inform the device that someone is trying to open an connection. The main actor is the [[control bits]] header, each of the 6 bits represent a state:
- [[URG]]: urgent message
- [[ACK]]
- [[PSH]]: push notification
- [[RST]]: reset connection
- [[SYN]]: synch number for connection establishment
- [[FIN]]: [[session termination]]
In a [[three way handshake]] the first message has the [[control bits]] set to [[SYN]], the receiver sends back the [[control bits]] with both [[SYN]] and [[ACK]], and finally the first sends the [[ACK]]

##### ordering and [[guarantee of deliver]]

In order to ensure all segments arrive at upper layers in order the [[transmission control protocol|TCP]] uses the [[sequence number]]. This number is picked randomly and increased at every message by the amount of bytes in the message, it start with the [[initial sequence number]] and progresses with each [[segment]], if something arrives out of order it is held into a [[buffer]] by the receiver while waiting for the right [[segment]] to arrive.
On the other hand, the receiver sends back an [[ACK]] for each [[segment]] with the number of the next byte that it is expecting in the [[sequence number]] ([[expectational acknowledgment]]), so also the sender knows if something needs to be resent. There is a limit to the amount of bytes the sender can send before having to wait for an [[ACK]] and that is the [[window size]], sometimes up to 1Gb, established during the [[three way handshake]], and there is also a limit to the size of every single segment, called the [[maximum segment size]] obtained by taking the [[maximum transmission unit]] and subtracting the headers.
In case one [[segment]] in the middle of a message is lost, the receiver will send in the [[ACK]] the number of the byte starting that segment, this can cause the [[sender]] to have to send all the [[segment]]s starting from that one, some [[operating system]]s will support [[selective acknowledgment]] which prevent this from happening, the receiver will send the [[ACK]] with the missing packet and the [[selective acknowledgment]] for all the packets following that have been received.
All this is combined with timers to set a maximum waiting time for the [[ACK]], after witch the [[segment]] is re-sent
##### [[user datagram protocol]]

It is much simpler, does not have [[guarantee of deliver]] ([[best effort]]) nor [[flow control]], very little [[data checking]], it is not a [[connection-oriented protocol]] and has the minimum informations required to deliver the right [[datagram]] to the right [[conversation]].
All this downsides comes with the possibility of much faster [[conversation]]s also thanks to simpler headers of 8 bytes:
- 2 byte: source [[port]]
- 2 byte: destination [[port]]
- 2 byte: [[header length]]
- 2 byte: [[checksum]]
##### [[transport layer port]]

What we normally call ports are a layer 4, so [[transport]], identifiers that are used from [[server]] and [[client]]s to communicate using either [[transmission control protocol|TCP]] or [[user datagram protocol|UDP]] and create what are called as [[socket]] when combined with the [[IP]].
[[transport layer]]s below 1024 are usually dedicated to known services, they are called [[well known port]]s like 80 for [[web server]]s and 25 for mails.
This is the case for [[server]]s, hosts on the other end do not use the same port when receiving a response, in fact they use a random port above 1024, they include source port and destination port in the packet  so the web server knows to which port to send the packet and to which port respond.
One of the main advantages of using different ports is so that a host or server can run multiple services at the same time with no confusion.

Ports are managed by the [[Corporation for Assigned Names and Numbers]]

- [[well known port]]s: from 1 to 1023 for common web usage
- [[registered port]]s: 1024 to 49151 for both source or destination usually for organization
- [[private port]]s: 49152 to 65535 usually reserved for source ports by any application


