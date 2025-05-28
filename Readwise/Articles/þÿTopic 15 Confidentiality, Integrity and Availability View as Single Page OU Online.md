# þÿTopic 15   Confidentiality, Integrity and Availability: View as Single Page | OU Online

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/295739769/eoW0fIEeW-s0JsfiEi6iLFhn2xJqWGgGMMTRytorZHk-cove_XARafoR.png)

## Metadata
- Author: [[readwise.io]]
- Full Title: þÿTopic 15   Confidentiality, Integrity and Availability: View as Single Page | OU Online
- Category: #articles
- Summary: The CIA triad in cybersecurity stands for Confidentiality, Integrity, and Availability, which are essential for system security. Techniques like encryption and redundancy help protect data and ensure users can access it without interruption. Understanding and applying these concepts is crucial for mitigating security threats.

## Highlights
- m ‘CIA triad’
- Confidentiality:
- who or what is to be granted access to the data or the system;
- Integrity:
- unchanged from its intended form.
- Availability
- data should be readily available to authorised users
- the requirement to keep our data hidden from unauthorised access
- we can do by encrypting the data
- This type of communication interception is sometimes referred to as a man-in-the-middle attack, or eavesdropping attack
- can also be considered as a passive attack
- Imagine a scenario where a threat actor can gain access to and alter a patient’s medical records:
- Organisations are bound by law to handle carefully personal information they hold on individuals or other organisations.
- Maintaining OS integrity can be as simple as automatically updating security patches or timely service pack installations
- Access control systems
- The threat actor now has several malicious options available; these are sometimes referred to as attack vectors.
- Imagine that the threat actor now has access to the system, and particularly the unsecured router in the previous scenario. From there, it would be possible for the threat actor to add their own username and password and assign administrator privilege
- it would also be possible to easily move from a passive attack to an active attack
- , this would bring about an operational disruption to the system, which can be referred to as a denial-of-service (DoS) attack
- The term mitigation is used to describe how we intend to reduce the risk of events occurring that could harmfully impact our systems o
- removing the risk entirely is impossible,
- we can configure the router to encrypt the username and the password,
- MD5 does, however, have an important use as an integrity checker. MD5 will generate a fixed-length hash value from plain text,
- To add an extra layer of integrity, the process of salting is used
- Redundancy to retain availability
- redundant devices that will take over in the event a device becomes unresponsive.
- Cisco uses the Hot Standby Router Protocol (HSRP), which creates a standby router to act as an alternative
- the standby router automatically takes over.
- Switches can be set up to have multiple redundant links to the same destination
- Ethernet frames and IP packets have no time to live (TTL)
- redundant paths can lead to loops in a switch network
- STP (Spanning Tree Protocol) was developed, whereby all redundant links in a switched network are forced into a back-up state
- It’s also possible to create redundant servers to take over should the primary server fail, or to work alongside the primary server to share the load.
- Another form of redundancy can be implemented to protect the operating system, for example in the event of a hard disk failure.
- s disk mirroring.
- should a disk drive become exploited, corrupted, or damaged, then access to an exact copy of the data or even the entire OS will be available
- no data will be lost
- RAID is a technology
- multiple hard disk drives to act as a single logical drive
- various levels of RAID
- The most basic level of RAID is known as RAID 0 and provides only the most basic form of data protection. This achieved by ‘striping’ data across an array of disk drives
- no fault tolerance
- RAID 1, disk mirroring is implemented
- g allows for identical data to be written across an array of hard disk
- here are increased hardware costs
- there may also be some performance loss.
