A function that is normally used with [[list]] in the [[list generation]] and similar problems.
It can be implemented in different ways depending on the language but it always add a value to the end of the list.
It is not hard to see that if we use the [[append function]] in conjunction with the [[sequence generation problem]] we can obtain a list that follows the same order of the sequence since every new item is appended last.

In [[Python]] a way to append a value to a list is to simply "add" the value as a list itself so new_sequence = sequence + \[ value_to_append \]