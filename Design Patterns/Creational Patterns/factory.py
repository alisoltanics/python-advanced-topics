https://www.linkedin.com/learning/python-design-patterns/factory-example


Read factory_pattern_vs_factory_method

#########################################################
Also this cab be Open-Closed Principle example. (SOLID)
https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd#file-2-ocp-py
#########################################################


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        pass

    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def get_animal(name):
    animal_classes = {
        'lion': Lion('lion'),
        'mouse': Mouse('mouse'),
        'snake': Snake('snake')
    }
    return animal_classes[name]()


animal = get_animal('lion')
animal.make_sound()

==> 'roar'

#########################################################
Also send message example with diffrent types.
#########################################################
