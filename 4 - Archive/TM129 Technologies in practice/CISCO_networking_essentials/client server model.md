[[client]] and [[server]] are essentially just computers, what they differ is their role inside a network and usually the software installed in them.
[[server]] is tasked with providing information to many [[client]]s and has software to do so, the [[client]]s are required to read and display such information and have different software.

In general any [[computer]] that participate in a [[network]] is called a [[host]], it can be a [[client]], [[server]] or both.

If a [[network]] is comprised of [[computer]]s that do both the [[server]] and the [[client]], it is called a [[peer to peer]] [[network]]. A [[network]] of this type is easier to set up, cheaper as it has less components, easier to use and less complex, however it is less scalable, secure, prone to slow downs and there is not centralized administration.

You can also have a hybrid [[network]] where computers are both servers and clients but there is a central [[index server]] which store the records of which computer has which resource so the peers asks to it where to find them.

When an actual conversation between [[client]] and [[server]] occurs, the [[client]] tries to contact the [[server]], to do so it is not possible to use a URL like you are used to because communication happens via [[IP]], for this reason the client initiate a [[DNS lookup]] and asks a [[DNS server]] for the [[IP]] that matches a URL.
The [[client]] than establish a [[TCP/IP]] connection which will contain the [[ip address]] and [[source port]] of the client plus the same information for the [[server]] forming therefore the two [[socket]]s.

Other than web pages, [[File Transfer Protocol|FTP]], [[telnet]] and [[SSH]], also [[email]] is an example of a [[client server model]]. Servers stores and receive emails where a client has an inbox configured, clients finally can use [[SMTP]], [[POP3]] or [[IMAP4]] to access and read emails on the server.
- [[SMTP]]: uses port 25 for clients that wants to send an email to a server or when a server then has to forward the email to a different remote email server
- [[POP3]]: uses port 110, when a client send an email to a server and the message stays until a client read it and download it
- [[IMAP4]]: uses port 143, the server receive and store messages for the users but do not delete them unless the client specifically ask so