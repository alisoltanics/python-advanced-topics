---------------Shallow copy---------------:

list.copy() or list[:]


a = [[1, 2], [2, 4]]
b = a[:]
b.append([3, 6])

b
>>> [[1, 2], [2, 4], [3, 6]]

a
>>> [[1, 2], [2, 4]]


now change first item in b:

b[0][0] = 2

>>> b
[[2, 2], [2, 4], [3, 6]]
>>> a
[[2, 2], [2, 4]]
>>> 

items that copied to "b" still refrece to a list. so changing items in "b" also changes items of "a".




---------------Deep copy---------------:
import copy

a = [[1, 2], [2, 4]]
b = copy.deepcopy(a)
