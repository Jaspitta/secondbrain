A string of bits used as input to a [[cipher]] in conjunction with the [[plaintext]] to produce the [[ciphertext]]. Since a key is made of bits, for a given length $n$ there are $2^n$ possible keys.

For keys to be safe they need to be of a large enough number of bits that testing every possible key is not feasible for a [[brute force attack]], consider that moderns PCs can easily test millions of keys per second. [[Encrpytion]] that uses sufficiently large [[encryption key]] plus is resistant to known vulnerabilities is defined as [[strong encryption]].

The [[encryption key]] is the most important part of the [[encryption]] process, everything else can be exposed as long as the key remain secret, for this reason the key is protected in many ways:
- in a file called [[key chain]]
- in computer hardware
- in [[HSM]]
- generated on the fly like a [[session key]]
