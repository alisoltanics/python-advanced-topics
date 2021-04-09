Iteration:

Iteration is a general term for taking each item of something, one after another.
Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

########################################################################################

Iterable:

An iterable is an object (like tuple, list, string) that has an __iter__ method which returns an iterator,
or which defines a __getitem__ method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no longer valid).
So an iterable is an object that you can get an iterator from.

########################################################################################

Iterator:

When call iter() method of an iterable, it returns an iterator object.
When call next method and send iterator to it, returns an object from iterable to us.

