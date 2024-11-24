It is know abroad as [[The Great Firewall of China]] and is is a complex surveillance system that monitor all internal and external traffic to apply proper censorship.
It is maintained by all chinese [[ISP]]s and require an estimated 30k to 50k employees.

It works by applying specific [[blocking technique]]s:
- [[IP address block]]: simple and effective way that block traffic from china directed to [[IP]]s in a specific [[block list]]. However traffic can be routed so it is not impenetrable
- [[DNS injection]]: most requests go through internal [[DNS server]]s subject to [[IP address block]], however the one that go to a foreign one are intercepted by [[golden shield]]. The [[firewall]] do a [[deep packet inspection]] on the request and check if the [[URL]] is in a blocked list, if it is it reply with a genuine looking response faster than the foreign [[DNS server]] and block you from the real page.
- [[resetting connection]]s: [[golden shield]] uses [[deep packet inspection]] to check if your message contains any of 15k words considered questionable by the government. If it finds any it sends some [[reset packet]]s with the [[ip address]] of the foreign server and close the connection, this is however not possible with encrypted messages
- [[prefix hijacking]]: to connect to the [[internet]] you need to go through [[edge router]]s which find the best path using [[routing table]]s in a process called [[Border Gateway Protocol]]. [[golden shield]] inserts false [[routing table]]s to redirect requests

It is worth mentioning that none of these practices are actually visible for users, all the blocks and redirection are hidden behind messages that the connection is unreliable or the site unavailable, never that it has been blocked.
With that being said, the chinese government does not deny such restrictions, instead they make public the fact that they heavily censor the internet and limit communications for the benefits of the citizens.



