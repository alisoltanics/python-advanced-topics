https://stackabuse.com/the-factory-method-design-pattern-in-python/
https://www.geeksforgeeks.org/factory-method-python-design-patterns/




import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width 

    def calculate_perimeter(self):
        return 2 * (self.height + self.width) 


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class ShapeFactory:
    def __init__(self, name):
        self.name = name

    def create_shape(self):
        if self.name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif self.name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif self.name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))


shape_factory = ShapeFactory('circle')
shape = shape_factory.create_shape()



Read factory_pattern_vs_factory_method
