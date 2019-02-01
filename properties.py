def is_valid_age(age: int) -> bool:
    if age > 200:
        return False
    return True


class Person:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age: int) -> None:
        if not is_valid_age(age):
            raise ValueError(
                "Age is not valid."
            )
        self._age = age


person = Person()
person.age = 23
print(person.age)
