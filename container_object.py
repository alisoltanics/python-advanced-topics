# https://stackoverflow.com/a/14109333/6173668

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __contains__(self, param1):
        return True if param1 in self.__dict__.keys() else False


p = Person('test', 23)
print('name' in p)
