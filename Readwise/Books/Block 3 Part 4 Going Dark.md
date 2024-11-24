# Block 3 Part 4 Going Dark

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/198194614/u5CQCWm-dYYT6qEL--sGlEoZVFVI0N-nNrEC1hGQKvE-cove_ZvXpxEc.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 3 Part 4 Going Dark
- Category: #books
- Summary: This text discusses the benefits and dangers of computer encryption, highlighting its role in both protecting privacy and enabling criminal activities. It explains how the Tor network uses strong encryption to secure data and discusses the challenges governments face in regulating encryption while ensuring public safety. The text also covers the legal framework in the UK that allows authorities to request access to encryption keys during serious investigations.

## Highlights
- This part concentrates on how encryption represents a huge opportunity for individuals and organisations but, simultaneously, a serious threat to our society.
- governments struggle not only to understand encryption, but to create workable legislation
### 4.1 Tor: an anonymous network
- Even though encrypted messages could not be read, the origin, destination, frequency and type of US intelligence messages *could* be determined by other intelligence agencies
- traffic analysis
- TOR
- a new network in which senders and recipients of data communicated through an ever-changing relay of other anonymous users
- TOR could not remain a secret. If TOR was *only* being used by intelligence agencies, traffic analysis would quickly identify
- Renamed as the Tor network
- now maintained by the non-profit The Tor Project Inc
#### 4.1.1 The Tor browser
- requires the Tor browser software,
- Many of the clever features and plug-ins we take for granted aren’t present
- behind the scenes, the Tor network is very different
- designed to hide the origin and destination of *all* data
#### 4.1.2 The Tor network
- During installation, Alice’s browser created a unique asymmetric key pair and stored the keys in a secure vault on her disk. Every Tor user has such a key pair
- the Tor network, which is constructed of thousands of individual nodes
- node is nothing more than a computer running Tor software
- find a route from Alice’s computer to Bob through this ever-changing network
#### 4.1.3 Building a circuit
- routed through the Tor network on a roundabout path called a circuit.
- start-up, Alice’s browser registered itself with a directory node responsible for keeping track of all nodes
- Alice’s browser creates a new Tor circuit by selecting several active nodes
- The first node in the circuit, Node 2, is called the guard node
- a series of relay nodes
- and finally to Node 22 (the exit node)
- From the exit, the data will travel to Bob over the conventional internet
- protected using a combination of asymmetric and symmetric encryption
#### 4.1.4 Encrypting data
- Alice and the nodes must exchange encryption keys. Alice’s Tor browser requests a copy of the public key from each node
- a node receives Alice’s request
- generates a unique session key
- duplicates this session key and makes a copy of its own public key
- The two keys are then encrypted together using Alice’s public key and sent to Alice
- The order in which this encryption is applied is crucial
- first encrypted with the public key from the most distant node
- Tor repeatedly encrypts the data using every public key provided by nodes
- The second round of encryption has two inputs:
  1. the ciphertext from the first round of encryption
  2. Node 22’s Tor network address.
- no fewer than five layers
#### 4.1.5 Sending data
- Alice’s browser has encrypted the request, it transmits
- Node 2 receives the ciphertext, it stores the address that sent it the ciphertext. Node 2 has no way of knowing if this is where the ciphertext originated
- Node 2 then removes the outermost layer of encryption using its private key, revealing another layer of ciphertext as well as the address of the next node
- Node 5 repeats the process
- every node only knows the address of the node immediately before it in the circuit as well as the address of the next node
- Node 22, the final layer of encryption is removed, revealing the request to contact Bob’s computer
- Node 22 makes a connection to Bob’s website over the conventional internet
- is called onion routing
- The repeatedly encrypted ciphertext is referred to as an onion
#### 4.1.6 Bob’s reply
- Data from Bob returns to Alice through the Tor network
- the reply is protected by symmetric rather than asymmetric encryption. Remember the session keys
- The reply re-enters the Tor network through Node 22,
- uses its session key to encrypt the data
- Node 17 then re-encrypts the ciphertext using its own session key and forwards the ciphertext
- Alice’s Tor browser decrypts the ciphertext using its copies of the chain’s session keys
#### 4.1.7 Rebuilding circuits
- Tor would ideally create a new circuit for every exchange
- create a very large computational load
- Unless interrupted, Tor maintains circuits for about 10 minutes
### 4.2 The Darknet
- billions of web pages indexed by internet search engines are not the entirety of the internet; in fact, this surface web constitutes only a fraction
- deep web probably contains several hundred times as much data as the surface web
- following links from indexed pages in the surface web
- sites that cannot be visited by web browsers
- the Darknet, and it relies on Tor
#### 4.2.1 Hidden services
- he most influential parts of the Darknet are hidden services (or onion services) accessed using apparently nonsensical .onion addresses
- onion addresses represent another use for hashes.
- onion address is generated by hashing the public key of the server
- cannot be resolved to an IP number by a DNS server
- data exchanged between Alice and the hidden service does not leave the Tor network
- The process
- is identical, but there is no exit node
- The most infamous hidden services are the Darknet’s marketplaces
- Marketplaces anonymise sellers and customers using a pair of technologies we have already introduced
- Bitcoin
- Tor
- Silk Road
#### 4.2.2 Silk Road
- sent by Ross Ulbricht using the handle "altoid", a talented Texan physics and engineering graduate interested in libertarianism
- By early 2011, Silk Road had more than 300 product listings – almost all for illegal drugs.
- Although much of Silk Road’s business *was* illegal, it *felt* safe.
- Ulbricht taking a commission worth some $20,000 per day
- *Gawker* published a profile of Silk Road (Chen, 2011) that did much to raise its profile – not just with potential customers, but also with the FBI
#### 4.2.3 Policing the Darknet
- The identity of Tor users and the locations of Tor hidden services *can* be revealed, albeit only with large expenditures of time and effort.
##### Identifying Tor users and services
- a process known as deanonymisation.
- using traffic analysis
- but *cannot* decrypt the data being exchanged.
- AI program searched for patterns in data passing through the guard, identifying the addresses of computers hosting hidden services with 88% accuracy.
- a PowerPoint presentation (Figure 4.12) summed up the inability of the world’s foremost intelligence agency to comprehensively surveil the Tor network
- Tor receives regular updates to fix security weaknesses
#### Tracking Bitcoins
- Bitcoin transactions are not – and never have been – entirely untraceable.
- the entire history of every Bitcoin can be recreated
- Bitcoin does not require new users to provide any form of official identification
- Bitcoin clients have their own network addresses which are broadcast to other Bitcoin users as people connect to and disconnect from the Bitcoin network
- Over time, they obtained IP numbers for approximately 60% of Bitcoin users who had logged into the network during the study.
- attack is limited by it causing a noticeable slowdown on the Bitcoin network as increasing numbers of connections are monitored
- methods for counteracting their type of deanonymisation
### 4.3 The rights and wrongs of encryption
- Most people’s feelings about encryption fall somewhere between two absolute statements:
  1. ‘Encryption should be banned since it allows criminals to escape justice.’
  2. ‘Encryption should be used as widely as possible because it protects personal privacy in a world of widespread surveillance and insecure network
#### 4.3.1 Arguments
- what is an argument?
- At the heart of any argument sits a main claim:
- this main claim needs to be accompanied by at least one supporting claim or reason.
- an academic argument is *not* an argument in the sense of a verbal fight
##### Assumptions
- Whether a claim supports another claim usually relies on unspoken assumptions that are shared by the claim maker and their audience
##### Supporting claims
- Determining whether a speaker or author means one claim to support another can be difficult
- looking out for connecting phrases or words such as *‘for example’*, *‘because’*, ‘*therefore’*, *‘so’*, etc.
- In terms of the conversation, the supporting claim is the answer to the *‘Why?’* question.
#### 4.3.2 Argument maps
- Arguments can also be presented graphically in argument maps.
- The main claim has been placed in an oval, to set it apart from other claims on the map
##### Opposing claims
- The opposing claim provides a reason for not (wholeheartedly) accepting the claim it opposes
- this is different from simply contradicting a claim
#### 4.3.3 Evaluating arguments
- the author of the slide has considered both supporting and opposing claims. In other words, their argument is balanced. This can make the argument more credible to a critical audience
- A critical audience won’t of course be persuaded merely by the fact that an argument is balanced. The supporting claims will have to outweigh the opposing ones.
#### 4.3.4 Argumentation versus persuasion
- e know from many psychological studies that every one of us is subject to many tendencies and biases
- according to the mere exposure effect, the more often we hear a claim, the more inclined we will be to believe it
- confirmation bias ensures that claims that fit in well with what we already believe are more likely to be accepted
### 4.4 Controlling encryption
- Practical enforcement of any such a ban is almost certainly impossible since:
- a ban is little deterrent to criminals hiding their activities using strong encryption
#### 4.4.1 Banning strong encryption
- some governments have proposed allowing citizens to use encryption, but to limit the length of the keys they can use
- This amounted to a de facto ban on US companies exporting strong encryption to the rest of the world.
- This ban gradually disintegrated during the 1990s.
- the US government ordered US software companies to provide two versions of encryption software:
- ‘domestic’ version with 56-bit DES
- ‘international’ version using 40-bit DES
- The weaker international standard exposed users to brute-force attacks.
- Further concessions on the export of strong encryption were made in 1996, until they were removed entirely by 1999 for almost all export markets
#### 4.4.2 Key escrow
- In 1996, the US government announced that US companies would be permitted to export long encryption keys, provided that duplicates were retained in the United States where they could be ‘recovered’ as needed by law enforcement and intelligence agencies
- in March 1997, the British government outlined plans requiring British companies offering encryption products to deposit duplicate keys with a central government repository. This process is known as key escrow
- Escrow is a legal concept in which buyers do not pay sellers directly; instead, funds are transferred through a so-called trusted third party
- these bodies can request that the trusted third party releases the key into their care – a process known as key recovery.
#### 4.4.3 The Clipper Chip
- a second attempt to implement key escrow
- Encryption and decryption would be performed using the new Skipjack symmetric algorithm running on a dedicated microprocessor called the Clipper Chip
- potential risks posed by theft of keys or their misuse by governments or individuals are much harder to resolve
- British key escrow proposal was dropped following a change of government in 1997 and the US key escrow was abandoned in 1999
- in the event of suspected criminal activities, Clipper would allow government agencies to decrypt encrypted messages.
- undermined by a lack of trust in the ability of governments to safeguard keys
- Clipper devices would contain two separate keys:
  1. an 80-bit unit key unique to each Clipper Chip
  2. a family key common to all Clipper Chips.
- The escrowed unit key would be split in two: one half retained by the US Treasury, the other by the National Institute of Science and Technology
##### How Clipper worked
- encrypted session key is then combined with some additional information including a hash and re-encrypted with the family key
- Clipper Chips fitted to Alice and Bob’s devices negotiate a shared symmetric 80-bit session key.
- computer encrypts her message using the session key
- Clipper Chip encrypts the session key using its unique unit key
- produce a piece of ciphertext known as the Law Enforcement Access Field (LEAF).
- r transmits the encrypted message and the LEAF to Bob.
- Bob’s computer discards the LEAF and uses his copy of the session key to decrypt Alice’s message.
- The LEAF is protected by two layers of encryption. The outer layer can be decrypted using the Clipper family key shared by all Clipper Chips
- a copy of Alice’s unit key is held in escrow by the Treasury and NIST
##### Clipper’s first flaw
- concerned that government agencies would abuse trust and eavesdrop on innocent parties
- Security experts around the world devoted time to investigating Clipper’s workings,
- Each LEAF was authenticated by a 16-bit hash which has 216 = 65,536 possible values
- Rather than a single unique hash for every possible LEAF, every Clipper LEAF hash corresponded to 2128/216 = 2112 keys!
- Blaze explained how a malicious user could use LEAF hash collisions to circumvent law enforcement.
##### Scenario 3
- Chuck’s computer then repeatedly generates and tests fake session keys to find one whose hash collides with that of the genuine session key.
- The US government chose to quietly cancel Clipper entirely.
##### Clipper’s second flaw
- Skipjack was declassified by the NSA in 1998, *after* Clipper had been abandoned. Researchers discovered a partial attack on Skipjack just one *day* after the algorithm had been published
- the best security technologies are those that have been scrutinised by as many people as possible
- The demise of Clipper appeared to mark the end of the crypto wars between privacy and security activists and governments
#### 4.4.4 End-to-end encryption
- Revelations that British and US intelligence agencies had been surveilling large parts of the world’s communications network saw millions of people switch
- applications such as Signal employ end-to-end encryption,
- messages are encrypted for the entirety of their journey
- they all use the same approach as TLS/SSL
- using symmetric session keys
- using asymmetric encryption.
- end-to-end encryption overcomes a long-standing problem that relatively few people use encryption even when it is offered to them
- applications using end-to-end encryption automatically generate and apply encryption and decryption keys without user intervention, whilst the keys themselves are secured
#### 4.4.5 Backdoors and golden keys
- There has been political pressure from both the US and UK governments for manufacturers to include a backdoor or golden key into encryption products.
- Cryptographers have identified serious problems with any backdoored encryption system
### 4.5 Legislating for encryption
- how encryption is controlled in the United Kingdom through *legislation*.
#### 4.5.1 The Regulation of Investigatory Powers Act 2000
- ensure police forces can access plaintext data as part of an investigation
- abbreviated to RIPA
- At more than 50,000 words, RIPA is an enormous, wide-ranging piece of legislation
- examining RIPA Part III, which legislates for key disclosure
- lays out circumstances under which certain governmental bodies can demand individuals or companies to disclose the content of encrypted data
- also details the penalties
##### Section 49: Notices requiring disclosure
- Section 49 details circumstances under which a person may be forced to disclose their encryption keys when they are presented with a so-called Section 49 Notice.
##### Subsection (1)
- lists circumstances under which Section 49 can be used
- also lists the government agencies who can demand encryption keys:
##### Subsection (2)
- permits one of these agencies to require a key to be disclosed only if they believe a suspect has the key and there is no reasonable alternative course of action
##### Subsection (3)
- Possible reasons for demanding the disclosure of keys
##### Subsection (4)
- lays out the formalities of serving a notice to disclose encryption keys
##### Section 53: Failure to comply with a notice
- sets out a series of penalties
- Subsections (1) and (2) explain the conditions under which someone has committed an offence of not disclosing
- requires that they were in possession of the key before receiving the notice.
- Subsection (2) has proved to be especially controversial.
- authorities must demonstrate to a court that the person once had access to an encryption key
- They are then *presumed* to still have the key.
- The accused person can *rebut* this claim.
- they would be expected to produce some evidence to support their claim.
- the prosecution could attempt to disprove this claim, but would need to demonstrate ‘beyond reasonable doubt’ that the user still had access
- two further subsections:
- (5A) listing the maximum prison terms
- allowing a higher penalty to be imposed on offenders under certain circumstances.
- raised concerns that forcing people to disclose keys may breach fundamental rights
##### Section 54: Tipping off
- recipients of a Section 49 Notice may be forbidden from informing other people or organisations
- Reasons for secrecy and the penalties for violating a demand for secrecy are explained in Section 54.
- s serious penalties (listed in Subsection (4))
##### Implementation of Part III
- implementation of Part III was delayed allowing for consultation with industry and the public.
#### 4.5.2 Prosecutions under RIPA Part III
- It is unclear why relatively few failures to comply with a Section 49 Notice are prosecuted under Section 53
