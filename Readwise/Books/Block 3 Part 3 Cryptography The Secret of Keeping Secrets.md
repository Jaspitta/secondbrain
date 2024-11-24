# Block 3 Part 3 Cryptography: The Secret of Keeping Secrets

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/196166839/gfhfquKn5bOA63tNYnKkgyDvMY9Mowe7LJqKg-4EoxA-cove_V0iB7ll.jpg)

## Metadata
- Author: [[The Open University]]
- Full Title: Block 3 Part 3 Cryptography: The Secret of Keeping Secrets
- Category: #books
- Summary: Hashes and encryption keys play a crucial role in keeping data secure. Public-key cryptography allows secure data exchange without sharing sensitive information. Digital signatures help verify the authenticity of data and prevent tampering.

## Highlights
### Introduction
- This part complements Block 2 Part 7
- We will explore hashing further and show how hashing alone cannot protect user data
- introduce two forms of computer encryption
- they can also hide criminals from law enforcement
- we place increased emphasis on the conflict between what is technologically possible and what is socially acceptable
### 3.1 Hashing
- Hashing is useful because of two related characteristics
- It is a ‘one-way’ operation
- A variation of a single bit of data between two otherwise identical files will result in vastly different hash values
- hashes are described in terms of the number of bits making up the hash
- they are usually stored and displayed as hexadecimal values
#### 3.1.1 Authenticating data
- used to show the authenticity of files published on the internet
- Authors of documents can generate the hashes and publish them alongside the file itself
- if the two hashes match, the file is identica
- if the hashes differ, there is a problem
#### 3.1.2 Collisions
- widely used in so-called digital certificates
- to authenticate the origins of software
- a hashing algorithm *should* produce a unique hash for every different piece of data
- hashing algorithms *can* produce identical hashes for different pieces of data – known as a collision
- Collisions are extremely rare – the first MD5 collision was only found after hashing 250 different pieces of data
- it is impossible to *completely* guarantee the integrity of data hashed using MD5
- Flame is an especially sophisticated malware package that was first reported in 2012
- tool for spying
- used a fake digital certificate
- hash collided with one issued by Microsoft.
- developed jointly by the NSA, CIA and the Israeli military
- the US government advised transitioning away from SHA-1 in favour of SHA-2
- discovery of the first SHA-1 collision by Dutch researchers in 2016, who used a novel technique more than 100,000 times faster than brute force to test a colossal 263.1 hashes to discover a duplicate
#### 3.1.3 Protecting hashed passwords
- hashes can obscure computer passwords, but cannot guarantee their safety
- to further strengthen defences
- Salting is a process in which a computer adds a small amount of additional data to a password before it is hashed
- generates a random number, called the salt
- joined together, creating a new password
- The new value is hashed.
- When the user next logs in
- the computer recovers their salt, recombines it with the password and generates a hash
##### Why salt works
- Salt greatly increases the number of possible hashes any attacker must test in a dictionary attack
##### Misusing salt
- A new random salt *must* be generated every time a user creates a new account
#### 3.1.4 Even more password protection
##### Key stretching
- Key stretching increases the amount of time required
- o create a hash
- Key stretching may be problematic for online shopping sites or social media services where very large numbers of users are constantly logging in and out
##### Encrypting hashes
- We can further protect the password file using encryption
- In the most secure systems, passwords are stored, encrypted and decrypted by hardware security modules (HSM)
- designed in such a manner that there is no way to export keys from the HSM in a usable format. In fact, the only way to steal the keys is to steal the HSM itself
#### 3.1.5 The benefits and limitations of hashing
- Hashing cannot:
  • confirm that data has never been changed
  • guarantee the confidentiality of data
  • authenticate the creator or sender of data.
### 3.2 Ciphers and keys: an introduction to encryption
- Encryption is a field of mathematics concerned with obscuring information
- encryption was time-consuming
- the computer
- spurred the development of yet more complex means of encryption
- Computer encryption algorithms work on binary data
- encryption makes much of the modern world possible
- banking and payments
- conversations
- networks
- authenticating
- files stored
- electronic voting
- preventing piracy
#### 3.2.1 Some terminology
- Plaintext
- information that can be directly read
- Ciphertext is the encrypted data.
- key
- data that determines the value of the ciphertext
- cipher
- algorithm
- for turning plaintext into ciphertext
- Encryption
- the process of converting plaintext to ciphertext.
- Decryption
- the process of reverting ciphertext to plaintext
#### 3.2.2 Encryption keys
- Different keys allow a single encryption algorithm to produce an almost limitless number of different outputs
##### Computer encryption keys
- key is a string of bits
- For a key length of *n*, there are 2*n* possible keys
##### The problem with short keys
- Short keys are vulnerable to brute-force attacks
- Testing a million keys per second may sound fast, but this can easily be achieved by a modest PC
- Encryption that is resistant to brute-force attacks and whose algorithm has no known weaknesses is known as strong encryption
#### 3.2.3 Safeguarding keys
- The key is the most important piece of information in any practical form of encryption
- any encrypted messages are safe *so long as the value of the key is not known to the attackers*
##### Storing keys
- in a file called the key chain
- in a computer’s hardware
- in hardware security modules
- generated by a computer as and when they are needed
##### Session keys
- New keys are generated for each exchange of data
- Keys are deleted at the end of a session
### 3.3 Symmetric encryption
- Since the process of encryption and decryption are performed using the same key, ROT13 is an example of symmetric encryption.
#### 3.3.1 The Data Encryption Standard (DES)
- The NBS chose IBM’s ominously named ‘Lucifer’ algorithm and passed it to the US government’s National Security Agency (NSA) for review
- the NSA mandated reducing the key length of the final Data Encryption Standard from the 64 bits proposed by IBM to 56 bits
- An early IBM proposal would have seen DES use 128-bit keys
##### How DES works
- breaks plaintext into 64-bit blocks
- each of which is divided into two halves
- One half is scrambled using
- the F-function
- The two halves are recombined
- swapped
- This is repeated sixteen times
- Decryption of DES ciphertext is performed by reversing the proces
- One of the controversies regarding the role of the NSA
- the agency may have weakened the substitution algorithm
- messages could be decrypted
- became a US standard in 1976
- the NSA have demonstrated these worries were unfounded
- the NSA’s changes strengthened DES
- became a worldwide de facto standard
##### The adoption of DES
- also because it was capable of encrypting and decrypting large volumes of data at great speed
- specially designed microchips
##### The end of DES
- increasing computing performance meant more and more people
- had sufficient processing power to break DES
- 1997. A competition
- in 96 days by a collection of 14,000 internet-connected
- following year, Deep Crack, a $250,000 computer
- brute-forced DES in less than three days
##### The stopgap: Triple DES
- 1999
- government recommended users of DES moved to so-called Triple DES
- uses a key-bundle usually containing two – occasionally three – DES keys
- Most implementations of 3DES use two keys to perform three passes of encryption
- first pass uses the first key
- second pass re-encrypts
- using the second key
- third pass re-encrypts
- reusing the first key.
- Less frequently, a third key is used for the third pass
- quickly became a global standard and is still found in applications
- will remain secure against brute force until 2030
#### 3.3.2 The replacement: the Advanced Encryption Standard (AES)
- 1997
- work alongside the government in developing a new encryption standard
### 3.4 Turning the world upside down: asymmetric cryptography
- symmetric encryption was thought to be the only way of encrypting data. Before encrypted data could be exchanged, a shared symmetric key had to be generated and shared
- Alice and Bob could meet, generate the key and each leave with a copy
- might be inconvenient
- one copy of the key could be lost
- known as the
- key distribution problem
- thousands of people were employed in
- distributing
- encryption keys
- United Kingdom’s Government Communications Headquarters (GCHQ) in 1973
- now called asymmetric cryptography or public-key cryptography
- a cryptographic scheme that avoided the key distribution problem
- emained secret until December 1997
#### 3.4.1 How asymmetric cryptography works
- each user create *two* keys
- private key that the key owner must keep safe
- public key which can be sent to *anyone*
- the keys are known as a key pair
- private key is the *only* key that can decrypt files encrypted with the corresponding public key
- public key is the *only* key that can decrypt ciphertext encrypted using the corresponding private key
- Anyone wanting to send an encrypted message to Alice uses a copy of her public key to secure the message
##### Exchanging secrets using asymmetric cryptography
- The mathematics
- complex
- but using
- is relatively simple
- she can request a copy of Bob’s public key from a public key chain server located on the internet.
- Alice encrypts the plaintext using
- Bob’s public key
- he uses his private key
- to decrypt the ciphertext
##### Private keys must remain private!
- the private key *must* be kept secure.
##### Revoking keys
- often, users forget the password needed to use their keys;
- Public-key encryption software offers revocation facilities, by which a user can mark a key as no longer trusted. Revocation effectively adds a comment to a key informing users that it can no longer be trusted.
- Key chain servers can manage this process, warning users that the old key is no longer secure and distributing replacement keys.
##### Asymmetric key strength
- asymmetric keys are typically very large – usually 1024, 2048 or 4096 bits long.
- it is much harder to judge its security relative to symmetric keys.
- Symmetric encryption is fast.
- It uses small keys.
- It is well-suited to encrypting any amount of data.
- The rediscovery of asymmetric cryptography
- Three years after GCHQ’s discovery, asymmetric cryptography was independently rediscovered by two groups of US cryptographers.
- Rivest, Shamir and Adleman’s algorithm, RSA, founded the multi-billion-dollar company RSA Security
- RSA Security is now part of Dell Technologies Inc., and continues to develop public-key encryption technologies
#### 3.4.2 Using asymmetric cryptography to authenticate data
- it can also be used to uniquely identify the author of a piece of data. Asymmetric cryptography allows creators to ‘sign’ their data
- A public key can only decrypt ciphertext encrypted with the corresponding private key
- because asymmetric cryptography is computationally expensive
- normal to encrypt the relatively small hash of a document, rather than the document itself. The encrypted hash is called a digital signature.
##### A simple digital signature
##### Faking a digital signature
- There is nothing to stop Eve creating a new asymmetric key pair in Bob’s name.
- we need a way of verifying the identity of key holders. Fortunately, there is precisely the tool we need – a digital certificate.
#### 3.4.3 Digital certificates (public-key certificates)
- Eve’s scheme would fail if genuine keys were authenticated by a trusted third party
- a digital certificate authenticates public keys *and* digital signatures.
- consists of
- version
- serial number
- Issuer information
- Public key information
- Acceptable uses
- Digital signature information
- A hash of the certificate’s contents known as the thumbprint (sometimes called a fingerprint).
- digital certificates are issued by one of a relatively small number of certificate authorities (CAs)
- If the certificate authority is satisfied of the holder’s identity, they create a new certificate
##### Using digital certificates
- now use digital certificates containing public keys to perform encryption, decryption and to authenticate data.
- she now needs to persuade a certificate authority that she is Bob – which, as you can imagine, is extremely difficult!
- obtaining keys from certificates is highly automated.
- If a private key is compromised, the holder simply revokes all associated certificates.
##### Can we trust the certificate authorities?
- Trust in certificates is largely maintained by large software vendors
- Where a CA is found to be at fault, companies can issue updates to software to block certificates, or indeed entire certificate authorities
- Symantec is one of the world’s largest computer security companies
- By 2017, Symantec controlled 14%
- confirmed that Symantec had failed to ensure the integrity of its certificates.
- Chrome browser, and would block all existing Symantec certificates from October 2018 onwards.
- Symantec sold its CA to a smaller rival, DigiCert, for $950 million (Figure 3.7). At a stroke, DigiCert became one of the largest CAs in the world
### 3.5 Everyday encryption
#### 3.5.1 Secure web connections
- Web traffic is not encrypted by default;
- In 1995, Netscape released the Secure Socket Layer (SSL) as a standard for other companies to include in their software.
- was largely replaced by the more secure Transport Layer Security (TLS),
- a web browser connects to a server
- The handshake
- a ‘hello’ message from the browser
- the time
- a few bytes of random data.
- browser then sends
- a list of types of cryptography that it supports
- server responds
- server sends its time and a further chunk of random data to the browser.
- server chooses one asymmetric cipher, one symmetric cipher and a hashing algorithm
- server concludes the handshake by delivering its digital certificate
- Verification
- browser verifies the server by examining its certificate.
- browser hashes the certificate and compares it to the hash stored in the certificate’s thumbprint.
- The pre-master secret
- browser uses the time values and random data it created in Step 1 to create a pre-master secret
- extracts the server’s public key from the certificate and uses it to encrypt the pre-master secret.
- sent to the server, which extracts it with its private key.
- Generating a symmetric key
- Both machines simultaneously turn the pre-master secret into a **master secret** using the time and random data produced
- When the browser has finished creating its key, it tells the server it is ready
- Every piece of data is checked for tampering or error using the hashing algorithm agreed during the handshake.
#### 3.5.2 Security through publicity
- The most trusted forms of encryption are those that have been most intensely scrutinised.
- public knowledge of how encryption is implemented improves security.
- allows experts to determine
- weaknesses
- security through obscurity can mislead honest people into placing undue trust
