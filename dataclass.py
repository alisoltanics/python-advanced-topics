from dataclasses import dataclass, asdict, field

# The following example shows a simple usage of the dataclass decorator.
@dataclass
class Person:
    name: str
    age: int


p = Person('John Doe', 34)


# It is possible to provide default values to the fields.
@dataclass
class Person:
    name: str = 'unknown'
    age: int = 0


p = Person('John Doe', 34)
print(p.name)

p2 = Person()
print(p2.name)


# If the frozen parameter is set to True, we cannot assign values to fields.
@dataclass(frozen=True)
class Person:
    name: str
    age: int


p = Person('John Doe', 34)
p.occupation = 'gardener'

print(p)
print(p.occupation)
# In the example, the frozen parameter is set to True.
# The program fails with the following error message:
# dataclasses.FrozenInstanceError: cannot assign to field 'occupation'.


# The asdict() function converts a dataclass instance to a dict of its fields.
@dataclass
class Person:
    name: str
    occupation: str
    age: int


p = Person('John Doe', 'gardener', 34)
print(p)

print(asdict(p))


# With the field() function, we can provide some additional per-field information.
@dataclass
class Person:
    name: str
    age: int
    occupation: str = field(init=False, repr=False)


p = Person('John Doe', 34)
print(p)

p.occupation = "Gardener"
print(f'{p.name} is a {p.occupation}')
# In the example, we have an additional occupation field.

occupation: str = field(init=False, repr=False)
# The occupation field is not included in the __init__() and __repr__() methods.

Person(name='John Doe', age=34)
# John Doe is a Gardener
# This is the output.






https://zetcode.com/python/dataclass/