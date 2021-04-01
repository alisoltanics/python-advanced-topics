class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg


class ElectricCar(Car):

    def __init__(self, battery_type, model, color, mpg):
        self.battery_type = battery_type
        super().__init__(model, color, mpg)


# use super without any argument
# https://stackoverflow.com/a/27740540/6173668