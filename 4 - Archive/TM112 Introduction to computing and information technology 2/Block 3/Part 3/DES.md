---
aliases:
  - Data encryption standard
---
A standard set up by the [[National Bureau of Standards]] with the [[National Security Agency]] which established the [[cipher]] [[Lucifer IBM]] from [[IBM]] to be the national [[encryption algorithm]].
Initially the [[encryption key]] was supposed to be 64 bits, the [[National Security Agency]] asked to reduce to 48 and than settled to 56, causing a lot of controversy.

The [[cipher]] worked by:
```
break text in 64 bit chunks
for each chunk:
	loop 6 time:
		split chunk in half
		scramble it with the F-function
		recombine the halves
		swap them	
```
the [[decryption]] could be performed by reversing the algorithm. The bit controversy was that the [[National Security Agency]] changed the [[DES]] algorithm to make it weaker and easier for them to read [[ciphertext]], but these accusations were later proved to be false.

DES became the US standard in 1976, and with the backing of governments, [[IBM]] and the fact that is was really fast (specialized [[microchip]] were made) made it become the world standard after a few years.

DES fell simply due to increase in computer power, in 2000 DES could be broken by a [[brute force attack]] in less than a day, much earlier before that super computers where able to force it and the world started to move away from it.

In response the government developed [[3DES]], simply a key bundle of 2 or 3 keys was used. [[plaintext]] was encrypted with the first key, done again with the second key and finally again with the first or third if there is one. This is still used today in many application and became the new standard.






