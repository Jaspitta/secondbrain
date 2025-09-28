On it's core, a [[switch]] forward based on the [[MAC address]], however there are actually two distinct methods they can do so:
- [[store and forward]]: receive the [[ethernet]] frame, calculate the [[CRC]] (number of 1s, if they do not match there is an error), if everything okay forward the frame to the right port. It is also possible to do [[frame classification]] for [[traffic prioritisation]].
- [[cut through]]: start forwarding even before the full frame is received, as soon as the destination MAC address is red, the forwarding begins. There are two of this type:
	- [[fast forward switch]]: bits are forwarded as soon as the destination [[MAC address]] is known, sometimes it creates errors but rarely, latency is measured from the first bit received to the first transmitted
	- [[fragment free switch]]: stores first 64 bytes because it is where errors are most likely to be, a middle ground between [[cut through]] and [[store and forward]]

It is also possible to configure each port to use [[cut through]] up until a threshold of errors, if too many [[ethernet frame]] are faulty, it switch to [[store and forward]], and if the error rate goes back down it switches back to [[cut through]].

Sometimes the [[switch]] wants to send an [[ethernet frame]] but the port is being used for a different one, switches can actually hold to packets in memory in different ways:
- [[port-based]]: queues are configured for each port, on frame that blocks a port can block all the frames wanting to go on that port
- [[shared memory]]: single common memory where each [[ethernet frame]] is linked dynamically to each port

