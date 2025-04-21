from task2.Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, length):
        shape_type = shape_type.lower()
        if shape_type == 'square':
            return Square(length)
        elif shape_type == 'circle':
            return Circle(length)
        elif shape_type == 'equilateraltriangle':
            return EquilateralTriangle(length)
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")
