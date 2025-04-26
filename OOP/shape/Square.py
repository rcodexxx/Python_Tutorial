from Shape import Shape

class Square(Shape):
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    def get_area(self):
        return self._length * self._length

    def get_perimeter(self):
        return 4 * self._length
