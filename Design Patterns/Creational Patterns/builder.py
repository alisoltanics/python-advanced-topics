Builder is a creational design pattern that lets you construct complex objects step by step.
The pattern allows you to produce different types and representations of an object using the same construction code.



class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

    def get_car(self):
        return self._builder.car


class Builder():
    """Creates car object"""
    def __init__(self, *args, **kwargs):
        self.car = None

    def create_new_car(self):
        self.car = Car()


class SkyLarBuilder(Builder):

    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Turbo engine"


class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(
            self.model,
            self.tires,
            self.engine
        )


builder = SkyLarBuilder()
director = Director(builder)
director.construct_car()
director.get_car()




https://www.linkedin.com/learning/python-design-patterns/builder
https://refactoring.guru/design-patterns/builder