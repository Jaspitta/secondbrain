---
aliases:
  - digital certificate
---

They are one of the applications of [[asymmetric encryption]] to ensure the validity of data, in particular to prove the validity of [[digital signature]].
If we simply trusted a [[digital signature]] for how it is, everyone could put out a fake [[public key]] in the name of someone else and you would have no way of verifying the validity of it.

A [[digital certificates|digital certificate]] is a document that proves the public key belong to who it says. It is issued by a [[certificate authority]] which is an organisation that has the responsibility of verifying the identity of who ask a digital certificate and provide it only if the necessary standards are met, they can be trusted because they are companies that are held accountable by basically the rest of the world, if they do not meet the standards required they simply sto being trusted by the browsers.
A [[digital certificates|digital certificate]] contains a whole set of information including, date and uses for which it is valid, the person it belong to, the issuer, signature of the issuer, the key of the holder and a [[digital fingerprint]] which is a hash of the document itself, like a [[digital signature]].