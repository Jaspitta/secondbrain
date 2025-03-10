At the core there is the need to establish rules about the conversation, the method, the language and the confirmation strategy in particular. These rules make up what we call [[protocol]].

A [[protocol]] must define:
- [[message format]]
- [[message size]]
- [[timing]]
- [[encoding]]: data to bit/bit to data
- [[encapsulation]]: adding the right headers
- [[message pattern]]: acknowledgment before sending or streaming


Similar but different from a [[protocol]] is a [[standard]], it defines a set of rules for how things should be done, while a protocol define how devices should communicate in a [[network]], a standard define how something should be done like writing, sending and reading an email.
They allow for different devices to do things with each other, even if the device change, as long as the standard is respected.
An [[internet standard]] comes from long discussions, problems and testing, it start as a [[request for comments]](RFC) document by the [[internet engineering task force]](IETF).

Some example of [[internet protocol]]s that could all be in the same message:
- [[ethernet]]: [[network interface card]] to [[network interface card]] in same network
- [[IP]]: communication from source to destination through [[intermediate device]]
- [[TCP]]: proper ordering of messages
- [[http]]: transfer of [[HTML]]

Messages contains many protocols layers ([[layered model]]) usually in what is called a [[protocol stack]], for the [[TCP/IP]] model for example:
- application: [[http]] encode/decode and present data to the user
- transport:[[TCP]] support communication across different devices through the network
- internet: [[IP]] determine the best path for data through the network
- network access: [[ethernet protocol]] control hardware and media that makes up the network
This definition is what it is called a [[protocol model]] because it uses a protocol to define how something should be done at each layer. The alternative is a [[reference model]] which define the functions that should be completed at each layer but not how to. The most common [[reference model]] is the [[OSI model]](Open systems interconnection) by [[ISO]].:
- 7 application: process to process communication
- 6 presentation: representation of data for layer 7 services
- 5 session: manage and exchange data for layer 6
- 4 transport: segment, transfer and reassemble data for communication
- 3 network: exchange individual data pieces over network
- 2 data link: exchange data frame over a media
- 1 physical: mechanical, electrical and functional connection for exchanging a bit

In this model it is important to understand the [[encapsulation]] process in this mode, each layer add the [[header]] related to the [[protocol]] and pass the whole message to the next, the next will than take all the content including the headers, treat it as data and add it's own headers. This process continue for each layer, it start with the data produces by the user, [[application layer]] add it's headers, pass to [[presentation layer]], it takes the whole [[packet]], treat it as the payload, add it's headers, pass the whole [[packet]] forward and so forth.
At each layer, the combination of data and header create the [[protocol data unit]] or [[PDU]]
![[Pasted image 20250220100605.png]] 

The [[TCP/IP]] translated to [[OSI model]] would be:
- application: 7,6,5
- transport: 4
- internet: 3
- network: 2,1