---
aliases:
  - secure socket layer
---
SSL and its successor [[TLS]] are 2 applications of the most important [[encryption]] technologies we have seen so far to everyday usage. They use [[encryption algorithm]], [[digital certificates|digital certificate]], [[digital signature]], [[asymmetric encryption]], [[symmetric encryption]], [[hashing algorithm]] and more…

They differ slightly but at the core the process is:
- [[handshake]]
	- [[browser]] contact the [[server]]
	- send time, random bytes of data and a list of supported algorithms from most to least secure
	- [[server]] responds with time, random data and a choice of one [[asymmetric encryption]] algorithms, one [[symmetric encryption]] algorithm and one [[hashing algorithm]].
	- [[server]] send its [[digital certificates|digital certificate]] signed by a trusted [[certificate authority]]
- [[verification]]
	- [[browser]] verify the [[digital certificates|digital certificate]] of the [[server]] also using the [[digital fingerprint]]
- [[pre-master key generation]]
	- [[browser]] uses the random data and time from the [[server]] to generate a [[pre-master key]], [[encrypt]] it with the [[public key]] in the [[digital certificates|digital certificate]] and send it to the [[server]]
- [[generating symmetric key]]
	- using the time, random data and [[pre-master key]], [[server]] and [[browser]] simultaneously generate a [[symmetric key]] for [[symmetric encryption]]
	- when the [[browser]] is finished it informs the [[server]] and secure communication can now begin
as an additional measure it is common to also common to check every piece of data sent using the [[hashing algorithm]] agreed upon during the [[handshake]].
