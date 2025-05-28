from ShapeFactory import ShapeFactory

def main():
    # 創建工廠實例
    factory = ShapeFactory()
    
    # 創建不同的形狀
    square = factory.create_shape('Square', 5)
    circle = factory.create_shape('Circle', 3)
    triangle = factory.create_shape('EquilateralTriangle', 4)
    
    # 輸出正方形結果
    print("\n正方形測試結果：")
    print(f"邊長: 5")
    print(f"面積: {square.get_area():.2f}")
    print(f"周長: {square.get_perimeter():.2f}")
    
    # 輸出圓形結果
    print("\n圓形測試結果：")
    print(f"半徑: 3")
    print(f"面積: {circle.get_area():.2f}")
    print(f"圓周長: {circle.get_circumference():.2f}")
    
    # 輸出等邊三角形結果
    print("\n等邊三角形測試結果：")
    print(f"邊長: 4")
    print(f"面積: {triangle.get_area():.2f}")
    print(f"周長: {triangle.get_perimeter():.2f}")
    print(f"高: {triangle.get_height():.2f}")

if __name__ == "__main__":
    main() 