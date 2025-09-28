---
aliases:
  - DNS
---
It is the system dedicated to translating a [[domain name]] to an [[IP]].
A [[client]] will hold a [[DNS cache]] on it's system, but if a [[domain name]] that is not in the cache is requested, it has to send a query to the [[local DNS]] configured. This [[server]] as also a cache, if the [[domain name]] is in the cache it will send the [[IP]] back. If the [[local DNS]] (also called [[recursive DNS]]) does not have the [[domain name]] it has to ask a [[root level DNS]].
There are only 13 of them, operated by 12 organization with 750+ instances, these asks directly if necessary to a [[top level DNS]], there is one for each [[top level domain]] so .com, .net, .org etc...
The [[root level DNS]] then forward the [[IP]] of the [[top level DNS]] to the [[local DNS]], although usually it is already cached so this step is skipped. The [[local DNS]] now contact the [[top level DNS]], this will have the [[IP]] of the [[authoritative name server]], this is the final holder of the [[IP]] for the [[domain name]] the user need. Now the [[local DNS]] has the [[IP]] of the [[authoritative name server]], so it asks to it the [[domain name]] and cache the response just like the [[client]] does:
![[Pasted image 20250223162423.png]]


The [[DNS protocol]] actually uses only one type of message for all communications related to the protocol. This message is made of:
- question: the question for the [[domain name]]
- answer
- authority: [[record]] pointing to the [[authoritative name server]]
- additional: extra


A [[domain name system|DNS]] actually holds what are called [[record]]s and not just IPs, a record have a [[type]] which define what will the data represent:
- A: an [[IP]]
- NS: [[authoritative name server]]
- AAAA: [[IPV6]]
- MX: mail record


The [[domain name system|DNS]] is basically a special type of distributed [[database]], it is scalable because of the [[hierarchical structure]], the structure is given by the [[domain name]] itself with the ".", each [[server]] has to manage a small zone related to that portion therefore distributing the traffic.