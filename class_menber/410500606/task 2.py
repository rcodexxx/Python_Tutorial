import math

# 父類別：Shape
class Shape:
    def get_area(self):
        raise NotImplementedError("請在子類別中實作 get_area 方法")

    def get_周長(self):
        raise NotImplementedError("請在子類別中實作 get_周長 方法")

# 子類別：正方形
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_周長(self):
        return 4 * self.side

# 子類別：圓形
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_周長(self):
        return math.pi * self.radius * 2  # 或 return 2 * math.pi * self.radius 如果你要周長

# 子類別：正三角形
class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def get_周長(self):
        return 3 * self.side

square = Square(4)
circle = Circle(3)
triangle = EquilateralTriangle(2)

print("正方形：")
print("面積 =", square.get_area())
print("周長 =", square.get_周長())

print("\n圓形：")
print("面積 =", circle.get_area())
print("周長 =", circle.get_周長())

print("\n正三角形：")
print("面積 =", triangle.get_area())
print("周長 =", triangle.get_周長())
