---
aliases:
  - public key encryption
---

Developed in 1973 at the UK Government Communications Headquarters by James Ellis, Clifford Cocks and Malcolm Williamson, also known as [[asymmetric encryption|public key encryption]] to avoid the [[key distribution problem]] of [[symmetric encryption]] and remained secret until 1997.

It uses what is known as a [[key pair]], each user generate 2 keys, one private that must never be shared and one public that can be given to others. [[ciphertext]] created using one key can be [[decrypted]] only with the other, therefore you can use someones public key to encrypt a message you want to send to them and only their private key will be able to decrypt such message.

You might loose your key, it might become obsolete or it might get stolen, for many reasons there has to be a process to change your public/private key if needed and this process is called [[revoking keys]]. This is achieved with 2 parts, a software is used to mark the key as obsolete (adds a comment to the key) and than, the [[key chain server]] is updated to hold the new public key.

It is worth mentioning that it is quite difficult to judge the strength of [[asymmetric encryption]] comparing it to [[symmetric encryption]], in the first keys are generally much longer (even 4096 bits) but this does not make them immediately more or less secure.

While this might look like [[asymmetric encryption]] is overall superior it is worth noting that the true advantage over [[symmetric encryption]] is that it solves the key distribution problem, [[symmetric encryption]] is still used a lot because it is really fast, file size independent and require much smaller keys

[[asymmetric encryption]] can also be used to sign documents or data in general, if I encrypt something with my private key, only my public key can be used to get the original text back, to save on computation the document is usually [[hashed]], than the hash is encrypted with the private key and now you have the [[digital signature]]. The digital signature can be attached to the document to prove that it has not been modified, others can hash the document themselves, and than use the [[public key]] to get the hash sent with the file and verify that they match (assuming there are no [[hashing collisions]])



