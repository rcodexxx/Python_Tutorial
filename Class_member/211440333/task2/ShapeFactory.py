from Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, side):
        shape_type = shape_type.lower()
        if shape_type == 'square':
            return Square(side)
        elif shape_type == 'circle':
            return Circle(side)
        elif shape_type == 'equilateraltriangle':
            return EquilateralTriangle(side)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")
if __name__ == "__main__":
    shape_names = ['Square', 'Circle', 'EquilateralTriangle']
    sides = [4, 3, 5]

    for name, side in zip(shape_names, sides):
        shape = ShapeFactory.create_shape(name, side)
        print(shape)
        print(f"Area: {shape.get_area():.2f}")
        if isinstance(shape, Square):
            print(f"Perimeter: {shape.get_perimeter():.2f}")
        elif isinstance(shape, Circle):
            print(f"Circumference: {shape.get_circumference():.2f}")
        elif isinstance(shape, EquilateralTriangle):
            print(f"Perimeter: {shape.get_perimeter():.2f}")
            print(f"Height: {shape.get_height():.2f}")
        print()
