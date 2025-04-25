import math

from Shape import Shape

class EquilateralTriangle(Shape):
    def __init__(self, side):
        self._side = side

    @property
    def side(self):
        return self._side

    def get_area(self):
        return (math.sqrt(3) / 4) * (self._side ** 2)

    def get_perimeter(self):
        return 3 * self._side

    def get_height(self):
        return (math.sqrt(3) / 2) * self._side