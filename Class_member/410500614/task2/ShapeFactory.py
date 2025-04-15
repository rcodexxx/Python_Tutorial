from Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_name, size):
        shape_name = shape_name.lower()
        if shape_name == "square":
            return Square(size)
        elif shape_name == "circle":
            return Circle(size)
        elif shape_name == "equilateraltriangle":
            return EquilateralTriangle(size)
        else:
            raise ValueError(f"Unknown shape: {shape_name}")
