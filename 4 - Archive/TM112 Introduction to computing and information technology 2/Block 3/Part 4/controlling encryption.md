For the first years of strong [[encryption]] existence, governments grew skeptical of it's uses since, other than protecting the privacy of citizens it also gave a new tools to criminals to communicate in a way that was basically impossible for the governments to track.
Some governments tried to ban strong encryption but that is such a poor deterrent for criminals that the only people to suffer from it where the citizens.

Another attempt was to limit the size of encryption keys to be used, the idea is to have keys that are almost impossible to brute force for citizens or a small criminal organization but still possible for a government albeit with great efforts. In the 90s the USA limited the size of [[DES]] keys to 56 bits for domestic use and 40 for international use, with time this made companies too vulnerable to attacks and in 1999 all similar restrictions where removed.

A different approach was tested and that is the concept of [[key escrow]]. The concept was that it was possible for companies to use strong [[encryption]] both domestically and internationally but [[encryption key]]s had to be duplicated and stored safely by the government in the case of criminal charges with a process called [[key recovery]]. This approach was followed by the UK also, but the concern for possible corruption or improper keeping of such [[encryption key]]s grew so much that in the end also this approach was abandoned.


A further attempt was made by the USA government through the development of the [[clipper chip]]. All [[encryption]] and [[decryption]] was delegated to such [[computer chip]] which used the [[Skipjack]] [[encryption algorithm]] but in the event of criminal charges it would allow the government to recover the [[encryption key]] and the messages.
The [[clipper chip]] contained 2 [[encryption key]]s, one called a [[family key]] common to all [[clipper chip]]s and one called [[unit key]], made of 80 bit, 40 stored by the Treasury and 40 by the [[NIST]] to eliminate the risk for corruption.
The [[clipper chip]] worked in this way, 2 devices negotiated an 80 bit [[session key]] to [[encrypt]] the messages with.
The sender [[encrypt]] the message with the [[session key]] and the session key with the [[unit key]].
The result is combined with an [[hash]] and some information and than re-encrypted with the [[family key]], the result is called the [[LEAF]].
The computer transmit the encrypted message and the [[LEAF]] to the receiver, the receiver discard the [[LEAF]] and use the [[session key]] to decrypt the message.
If the government wants to read the message they can get the [[encrypted]] messages and the [[LEAF]].
They than use the [[family key]] to remove the first layer of [[encryption]], get the permission of a judge obtain the [[unit key]], use it to remove the second layer of [[encryption]] and finally get to the [[session key]].
They can than use the [[session key]] to decrypt the conversation.
![[clipper chip]]

However great this design might seem it has some flaws. First it did not eliminate fully the concern that the government could spy innocent citizens. Second, researchers that studied the design found that a [[LEAF]] was authenticated by a 16 bit [[hash]] with $2^{16}$ values but the [[LEAF]] had $2^{128}$ values and therefore a singe [[hash]] authenticated $2^{128}/2^{16} = 2^{112}$ keys and therefore [[hashing collisions]] where relatively easy to find.
This meant that a criminal could find a [[hash]] for a [[session key]] that had a [[hashing collisions]] with the real one and use that to make impossible for the government to get the [[session key]].
After this finding the government decided to shut down the [[clipper chip]] and a few years later made the [[Skipjack]] [[encryption algorithm]] public. A day after the publication researchers found a vulnerability in it proving once more that the best [[encryption]] technologies are the once that remain public following the [[security through publicity]] ideal and this also ended the [[crypto wars]] of governments.


In reality the struggle of politicians to find a way to make encryption safe for citizens but not a weapon for criminals never ended and maybe never will. With the advent of [[end-to-end encryption]], new messaging apps protect communications fully from any possible interception, and do it in a way that is fully transparent to the user removing the problem of having to manage and store your own keys. These apps all use some implementation of the [[TLS/SSL]] protocol making the process of generating and storing [[encryption key]] very safe and for these reasons more and more people moved away from conventional messages which can be spied by governments.
Politicians keep pressing scientists and corporations to include [[backdoor]]s and [[golden key]]s to the [[encryption algorithm]]s, however this reintroduce the problem of the government spying on citizens or not being able to keep the keys safe.
To this we have to add the complications that designing such new [[encryption algorithm]]s would bring, where possible new vulnerabilities are likely to arise.