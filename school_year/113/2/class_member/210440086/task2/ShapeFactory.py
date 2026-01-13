from Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args, **kwargs):
        shape_type = shape_type.lower()
        
        if shape_type == 'square':
            return Square(*args, **kwargs)
        elif shape_type == 'circle':
            return Circle(*args, **kwargs)
        elif shape_type == 'equilateraltriangle':
            return EquilateralTriangle(*args, **kwargs)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")