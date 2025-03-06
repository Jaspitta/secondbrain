Troubleshooting is mostly about [[process of elimination]], you segment what you are analysing and test each part to understand where the problem lies, from there you reduce the scope as much as possible until eventually you get to an answer.

When it comes to networks, if a PC has a problem the most common commands would be:
```
ipconfig /all
ping (usually you ping from the closest to the furthest device)
ipconfig /release
ipconfing /renew
traceroute
netstat
nslookup
```


Overall there are different approaches to troubleshooting:
- [[bottom up]]: starting from [[physical layer]] and going up testing, usually when you suspect the problem is at a lower layer
- [[top down]]: start from [[application layer]], when you suspect there is a software problem
- [[divide and conquer]]: use intuition to start from a layer, if that is ok you can assume all the once below also are
- [[follow the path]]: follow the traffic
- [[substitution]]: physically swap components with once you are sure are working, if the problem get's fixed you found the culprit
- [[comparison]]: compare config and devices with working once and try to spot the difference
- [[educated guess]]: built on experience, follow you hunch

Mostly what you want to do is to gather information, try to determine if the problem is software or hardware, choose between [[bottom up]] or [[top down]] accordingly, or if it is an already experienced problem use a [[divide and conquer]].

If you checked everything up to [[network layer|layer 3]], something might be blocking you on the upper layers, a common occurrence is a [[firewall]] blocking the port you are trying to access