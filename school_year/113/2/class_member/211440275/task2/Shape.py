from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("邊長必須是正數")
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def get_perimeter(self):
        return self.side_length * 4

    def __repr__(self):
        return f"Square(side_length={self.side_length})"

class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("半徑必須是正數")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"

class EquilateralTriangle(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("邊長必須是正數")
        self.side_length = side_length

    def get_area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

    def get_height(self):
        return (math.sqrt(3) / 2) * self.side_length

    def get_perimeter(self):
        return 3 * self.side_length

    def __repr__(self):
        return f"EquilateralTriangle(side_length={self.side_length})"


