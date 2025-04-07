from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
import math
import numpy as np


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


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


if __name__ == "__main__":
    # s = Square(100)
    # length = s.length
    # vertices_x = [0, length, length, 0, 0]
    # vertices_y = [0, 0, length, length, 0]
    #
    # plt.figure()
    # plt.plot(vertices_x, vertices_y, 'b-')
    # plt.title("Square")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axis("equal")

    # c = Circle(50)
    # theta = np.linspace(0, 2 * np.pi, 100)
    # circle_x = c.radius + c.radius * np.cos(theta)
    # circle_y = c.radius + c.radius * np.sin(theta)
    #
    # plt.figure()
    # plt.plot(circle_x, circle_y, 'r-')
    # plt.title("Circle")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axis("equal")

    et = EquilateralTriangle(100)

    v0 = (0, 0)
    v1 = (et.side, 0)
    v2 = (et.side/2, et.get_height())

    vertices = [v0, v1, v2, v0]
    vertices_x = [v[0] for v in vertices]
    vertices_y = [v[1] for v in vertices]

    plt.figure()
    plt.plot(vertices_x, vertices_y, 'g-')
    plt.title("Equilateral Triangle")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")

    plt.show()
