Visitor is a behavioral design pattern that allows adding new behaviors to existing class hierarchy without altering any existing code.


class House:
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print('havc')

    def work_on_elecrticity(self, electrician):
        print('electrician')

    def __str__(self):
        return self.__class__.__name__


class Visitor():
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_elecrticity(self)



hv = HvacSpecialist()

e = Electrician()

home = House()

home.accept(hv)

home.accept(e)



https://www.linkedin.com/learning/python-design-patterns/visitor-example
