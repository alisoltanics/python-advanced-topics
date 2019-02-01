def func():
    number = 2
    while True:
        new_number = number + 2
        yield new_number
        number += 4


a = func()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
 