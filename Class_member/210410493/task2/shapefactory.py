# shapefactory.py
from shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, side):
        if shape_type == "Square":
            return Square(side)
        elif shape_type == "Circle":
            return Circle(side)
        elif shape_type == "EquilateralTriangle":
            return EquilateralTriangle(side)
        else:
            raise ValueError(f"未知的形狀類型: {shape_type}")
