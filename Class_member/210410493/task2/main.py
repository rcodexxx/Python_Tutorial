# main.py
from shapefactory import ShapeFactory

def main():
    side = 5

    square = ShapeFactory.create_shape("Square", side)
    print(f"正方形 面積: {square.get_area()}，周長: {square.get_perimeter()}")

    circle = ShapeFactory.create_shape("Circle", side)
    print(f"圓形 面積: {circle.get_area():.2f}，圓周長: {circle.get_circumference():.2f}")

    triangle = ShapeFactory.create_shape("EquilateralTriangle", side)
    print(f"等邊三角形 面積: {triangle.get_area():.2f}，高: {triangle.get_height():.2f}，周長: {triangle.get_perimeter()}")

if __name__ == "__main__":
    main()
