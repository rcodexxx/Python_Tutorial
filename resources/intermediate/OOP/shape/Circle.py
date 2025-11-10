from Shape import Shape

class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def get_area(self):
        return math.pi * (self._radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self._radius