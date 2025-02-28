---
aliases:
  - layer 1
---
The primary role is to convert what is given by the [[layer 2]] [[data-link layer]], so an [[ethernet frame]] and convert it into a signal.

The [[physical layer]] is considered a bit separate from the other [[OSI model]] layers, because it is much more concerned with electronics than software and therefore governed by separate associations and [[standard]]s. The main organizations involved into standards for the [[physical layer]] are [[ISO]], [[TIA]], [[ANSI]], [[ITU]], [[IEEE]], [[FCC]], [[ETSI]] but there are also local organizations that develops standards at national or regional level.

This layer main concerns is divided into three areas:
- [[physical components]]: all the physical elements, including [[network interface card]] and the [[media]]
- [[encoding]]: method for representing digital information, [[Manchester encoding]] represent 1 as high voltage and 0 as low voltage but different [[standard]]s have different [[encoding]]s also based on the [[media]]
- [[signaling]]: the way bits are transmitted or signaled physically, for example a short light pulse for a 0 and a long light pulse for a 1, while [[encoding]] provide a way of representing 1 and 0 physically, [[signaling]] provide a way of transmitting the signal that could be voltage, light, radio or more

While choosing the [[encoding]] would be like choosing which alphabet to use, choosing the signaling would be like choosing how to communicate in the sense of writing, speaking etc..

The speed of the medium or the speed at which we can transmit data in general is called [[bandwidth]], that is the amount of bits per second we can transmit. Remember you can change up to a certain point how many bits per second you send but you can not change the speed at which those travel thought the [[media]]. Common terms to measure quality of the [[bandwidth]] are:
- [[latency]]: time for data to go from one point to another
- [[throughput]]: amount of bits transferred in a given time
- [[goodput]]: amount of usable data transferred in a given time


As we said, different media can be used to transmit data, the most common is [[copper cable]] because it is cheap and easy to install, however it is limited in distance and [[interference]] from [[EMI]] and [[RFI]] or [[crosstalk]]. The fading of the signal due to distance travel is called [[attenuation]]. Not all [[copper cable]] is equal, there are three main type of [[copper cable]]:
- [[unshielded twisted-pair]]: most common, terminate with [[RJ-45 connector]], four colour-coded wires twisted together in a plastic tube. The twisting is for reducing [[interference]], also different colours are twisted differently. All the characteristics are defined in the standard [[ANSI/TIA-568]]. Even with the same connector, the color to pin match can different based on the usage, with the [[ethernet straight-through]] being used for most networking and [[ethernet crossover]] for connecting similar devices 
- [[shielded twisted-pair]]: same connector, more expensive because wrapped in a shield
- [[coaxial cable]]: copper core, plastic shell, copper mesh as second wire and shield and rubber shell, not very used anymore

While [[copper cable]] is the cheapest and most common, it is definitely not the most performant, that is the [[fiber-optic cable]].
Commonly used for interconnecting network devices it is immune to [[interference]] and can transmit over longer distances.
It exists into two variations:
- [[SMF]]: a single laser is shine straight through a 9 micrometer glass core at very long distances
- [[MMF]]: multiple LEDs at different angle are shine through a 50 to 62 micrometer glass core up to 550 meters

The main usages are [[enterprise network]]s, [[fiber to home]], [[long-haul networks]] for connecting cities and [[submarine cable]].
Of course it also has different connectors:
- [[straight-tip connector]]: oldest
- [[subscriber connector]]: very used for [[LAN]] and [[WAN]], also called [[squared connector]]
- [[lucent connector simplex]]: smaller version of [[subscriber connector]]
- [[duplex multimode connector]]: like a [[lucent connector simplex]] but support duplex
One cable can have different connectors at the different ends to interconnect different [[network]]s for example, these are called [[patch cords]]


