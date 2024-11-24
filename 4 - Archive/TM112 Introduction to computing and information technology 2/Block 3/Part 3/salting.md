A process used commonly to protect data, in particular [[password]] and in conjunction with [[hashing]].
A random piece of data is attached to the user pass before hashing, at the next log in the [[salt]] for the user is recovered and recombined with the input before verifying the hash.

If we add salting, even a three [[bit]] salt means that for the same [[password]] there can be eight possible hashes (2^3) which has to be stored in the dictionary of an attacker, if we do not know weather the [[salt]] has been added at the beginning or end of the password we need to double the possibilities once more.
