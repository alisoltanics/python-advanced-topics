Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.


import copy


class Prototype:

    def __init__(self, *args, **kwargs):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:

    def __init__(self, *args, **kwargs):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(
            self.name,
            self.color,
            self.options
        )


c = Car()
prototype = Prototype()
prototype.register_object("skylark", c)

c1 = prototype.clone('skylark')

print(c1)



https://refactoring.guru/design-patterns/prototype
https://www.linkedin.com/learning/python-design-patterns/prototype-example