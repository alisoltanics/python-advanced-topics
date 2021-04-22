class DrawingAPIOne():
    def draw_circle(self, x, y, radius):
        print("api one draw")


class DrawingAPITwo():
    def draw_circle(self, x, y, radius):
        print("api two draw")


class Circle():

    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api(self._x, self._y, self._radius)


    
circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()


circle2 = Circle(1, 5, 6, DrawingAPITwo())
circle2.draw()



https://www.linkedin.com/learning/python-design-patterns/bridge-example