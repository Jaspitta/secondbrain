What we normally call ports are a [[layer 4]], so [[transport]], identifiers that are used from [[server]] and [[client]]s to communicate using either [[TCP-UDP]].

[[transport layer port]]s below 1024 are usually dedicated to known services, they are called [[well known port]]s like 80 for [[web server]]s and 25 for mails.
This is the case for [[server]]s, hosts on the other end do not use the same port when receiving a response, in fact they use a random port above 1024, they include source port and destination port in the packet  so the web server knows to which port to send the packet and to which port respond.
One of the main advantages of using different ports is so that a host or server can run multiple services at the same time with no confusion.

Ports are managed by the [[Corporation for Assigned Names and Numbers]]

- [[well known port]]s: from 1 to 1023 for common web usage
- [[registered port]]s: 1024 to 49151 for both source or destination usually for organization
- [[private port]]s: 49152 to 65535 usually reserved for source ports by any application

