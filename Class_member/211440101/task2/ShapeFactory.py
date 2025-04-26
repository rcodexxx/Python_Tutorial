from Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, size):
        if shape_type == 'Square':
            return Square(size)
        elif shape_type == 'Circle':
            return Circle(size)
        elif shape_type == 'EquilateralTriangle':
            return EquilateralTriangle(size)
        else:
            raise ValueError(f"不支持的形状类型: {shape_type}") 