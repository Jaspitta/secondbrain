They operate on [[ethernet frame]] and therefore they work at layer 2, [[data link]], of the [[OSI model]].

This device uses a [[mac address table]] where it stores the [[MAC address]] of devices connected to it's ports. When an [[ethernet frame]] is sent, the destination contains the [[MAC address]] of the device and the [[ethernet switch]] can look up which port has the device with that [[MAC address]].

The [[mac address table]] in an [[ethernet switch]] is not pre populated but built by the device itself, when a message is sent to the [[ethernet switch]], the [[ethernet frame]] contains also the source [[MAC address]], the switch check if it has a record of such [[MAC address]] on it's table, if it does not it adds the [[MAC address]] just received on the port that it has been received on. If the destination address is also unknown to the [[ethernet switch]], it simply broadcast the [[ethernet frame]] on all the ports and the receivers check if the message was meant for them.

An [[ethernet switch]], whenever it forward a packet, it always ignores the content, the addressing is done solely based on the source and destination