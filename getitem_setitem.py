__setitem__ is a method used for assigning a value to an item. It is implicitly
invoked when we set a value to an item of a list, dictionary, etc. __getitem__ is
a method used for getting the value of an item. It is implicitly invoked when we access
the items of a list, dictionary, etc. We can overload their operations by explicitly defining
them.

class Counter():
    def __init__(self, floors):
        self._floors = [None]*floors

    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self._floors[floor_number]


index = Counter(4)
index[0] = 'ABCD'
index[1] = 'EFGH'
index[2] = 'IJKL'
index[3] = 'MNOP'

print(index[2])



https://www.codespeedy.com/__setitem__-and-__getitem__-in-python-with-example/#:~:text=Both%20__setitem__%20and,generally%20used%20for%20operator%20overloading.