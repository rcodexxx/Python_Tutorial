from abc import ABC, abstractmethod
import math

# 抽象基底類別
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

# Square 類別
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

# Circle 類別
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

# EquilateralTriangle 類別
class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def get_perimeter(self):
        return 3 * self.side
