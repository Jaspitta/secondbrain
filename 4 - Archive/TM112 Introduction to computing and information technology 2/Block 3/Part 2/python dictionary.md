It is a python object type that define a [[python object]] with one or more [[key-value pair]]. Being an object it has an id, type and value like all the others. The value, much like [[list]] is a set of [[object reference|object label]] called keys pointing to other [[python object]].

The [[dictionary keys]] can be strings or numbers but not [[list]] or other [[python dictionary]].

The [[dictionary object value]] is the collection of keys, not the values they are attached to.

Given the similarities to [[list]], adding an element to a dictionary follow the syntax of `a_dict[key] = value`. Unsurprisingly, accessing values also works like a list, `a_dict[key]`. Checking a dictionary is also simple with `key in a_dict` which will evaluate to true if there is a value with such key.

