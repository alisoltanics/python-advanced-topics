Abstract Factory is a creational design pattern that lets you produce
families of related objects without specifying their concrete classes.


class Dog:

    def speak(self):
        return "woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        return Dog()

    def get_food(self):
        """Returns dog food object"""
        return "Dog Food"


class PetStore:

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(pet)
        print(pet.speak())
        print(pet_food)


# Concrete Factory
factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()


https://refactoring.guru/design-patterns/abstract-factory
https://www.linkedin.com/learning/python-design-patterns/abstract-factory-example
