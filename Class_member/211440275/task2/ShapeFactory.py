from Shape import Square, Circle, EquilateralTriangle

class ShapeFactory:
    @staticmethod
    def create_shape(shape_name, size):
     
        # 型別檢查
        if not isinstance(size, (int, float)):
            raise TypeError(f"size 必須是數字類型，得到 {type(size)}")

        if shape_name == 'Square':
            return Square(size)
        elif shape_name == 'Circle':
            return Circle(size)
        elif shape_name == 'EquilateralTriangle':
            return EquilateralTriangle(size)
        else:
            raise ValueError(f"無效的形狀名稱: {shape_name}. 可用的選項為 'Square', 'Circle', 'EquilateralTriangle'")

# 主程式
def main():
    factory = ShapeFactory()

    try:
        # 使用工廠方法創建 Square 物件
        square = factory.create_shape('Square', 10)
        print("建立的形狀:", repr(square))
        print("[Square] area:", square.get_area())
        print("[Square] perimeter:", square.get_perimeter())

        # 使用工廠方法創建 Circle 物件
        circle = factory.create_shape('Circle', 3.5)
        print("建立的形狀:", repr(circle))
        print("[Circle] area:", circle.get_area())
        print("[Circle] circumference:", circle.get_circumference())

        # 使用工廠方法創建 EquilateralTriangle 物件
        triangle = factory.create_shape('EquilateralTriangle', 7)
        print("建立的形狀:", repr(triangle))
        print("[Triangle] area:", triangle.get_area())
        print("[Triangle] height:", triangle.get_height())
        print("[Triangle] perimeter:", triangle.get_perimeter())

    except (ValueError, TypeError) as e:
        print(f"錯誤: {e}")

# 如果是直接執行此檔案，則調用 main()
if __name__ == "__main__":
    main()
