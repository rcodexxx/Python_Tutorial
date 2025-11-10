# TASK 2 (期中考) - Shape
請在自己的資料夾中建立一個task2資料夾, 並且需要完成以下三個內容並且分在Shape, ShapeFactory兩個檔案中
1. 請寫一個Shape的抽象父類別, 其中包含計算面積的get_area()抽象方法
2. 請完成Square, Circle, EquilateralTriangle三個子類別, 並繼承Shape, 其中每一個類別都以輸入邊長的方式建立, 類別內請根據以下規則
   1. Square 需要包含計算周長的方法
   2. Circle 需要包含計算圓周長的方法
   3. EquilateralTriangle 需要包含計算高, 周長的方法
3. 請建立一個工廠類別 ShapeFactory, 其中要有一個方法create_shape, 功能是當我輸入'Square'的字串的時候要建立Square的物件

### 計分方式
第一題: 30%

第二題: 每一個物件 10%

第三題: 40% 

### 寫作風格規範
1. 函數名稱
   1. 取得面積 get_area
   2. 取得周長 get_perimeter
   3. 取得圓周長 get_circumference
   4. 建立形狀 create_shape
2. 物件名稱
   1. Shape
   2. ShapeFactory
   3. Square
   4. Circle
   5. EquilateralTriangle