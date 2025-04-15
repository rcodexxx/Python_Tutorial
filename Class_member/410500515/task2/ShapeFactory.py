from Shape import Square, Circle, EquilateralTriangle

shape_map = {
    "square": Square,
    "circle": Circle,
    "triangle": EquilateralTriangle,
    "equilateraltriangle": EquilateralTriangle
}

def create_shape(shape_type, value):
    shape_type = shape_type.lower()
    if shape_type in shape_map:
        return shape_map[shape_type](value)
    else:
        raise ValueError(f"未知的形狀類型：{shape_type}")
