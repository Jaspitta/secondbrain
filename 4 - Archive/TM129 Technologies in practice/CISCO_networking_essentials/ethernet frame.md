- 7 bytes - preamble, helps the card to get in synch
- 1 byte - start frame delimiter
- 6 bytes - destination [[MAC address]] of the [[network interface card]]
- 6 bytes - source [[MAC address]]
- 2 bytes - length of data or type of data described via the upper layer protocol
- 46-1500 bytes - data ([[IPV4 packet]] or [[IPV6 packet]] usually)
- 4 bytes - check sequence for error checking

There are cases where the frame received is smaller than the minimum possible or bigger than the max, in most cases these are [[collision fragment]]s or [[jumbo frame]]s that are considered invalid, although some higher speed version of the [[ethernet standard]] support [[jumbo frame]]s.
