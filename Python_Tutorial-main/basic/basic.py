''' 0. Hello world'''

print("hello world")


''' 1. Variable '''

# 計算兩個數字的和
num1 = 10           # 整數
num2 = 5.5          # 浮點數
total = num1 + num2
print("總和是:", total)  # 輸出：總和是: 15.5

name = "小明"       # 字串
age = 20
print(name, "今年", age, "歲")  # 輸出：小明 今年 20 歲


''' 2. Operator and Input '''

# 簡單計算機
num1 = float(input("請輸入第一個數字："))
num2 = float(input("請輸入第二個數字："))
result = num1 * num2
print("兩數相乘結果為:", result)

# 判斷奇偶數
number = int(input("請輸入一個數字："))
if number % 2 == 0:
    print(number, "是偶數")
else:
    print(number, "是奇數")


''' 3. Conditions and If statements '''

# 判斷成績等級
score = int(input("請輸入你的分數（0-100）："))
if score >= 90:
    print("等級：A")
elif score >= 80:
    print("等級：B")
elif score >= 60:
    print("等級：C")
else:
    print("等級：F")


''' 4. Loops '''

# 列印 1 到 10
for i in range(1, 11):
    print(i, end=" ")  # 輸出：1 2 3 4 5 6 7 8 9 10

# 猜數字遊戲
secret = 42
guess = 0
while guess != secret:
    guess = int(input("猜一個數字（1-100）："))
    if guess > secret:
        print("太大了！")
    elif guess < secret:
        print("太小了！")
print("恭喜你猜對了！")


''' 5. Basic Datatype '''

# 列表 (List)
fruits = ["蘋果", "香蕉", "橙子"]
print("第一個水果：", fruits[0])  # 輸出：蘋果
fruits.append("葡萄")             # 添加元素
print("新增後：", fruits)         # 輸出：['蘋果', '香蕉', '橙子', '葡萄']

# 字典 (Dict)
student = {"name": "小明", "age": 20, "grade": "A"}
print("姓名：", student["name"])   # 輸出：小明
student["age"] = 21                # 修改值
print("更新後：", student)         # 輸出：{'name': '小明', 'age': 21, 'grade': 'A'}

# 元組 (Tuple)
coordinates = (10, 20)
print("X 座標：", coordinates[0])  # 輸出：10
# coordinates[0] = 15  # 這會報錯，因為元組不可修改

# 集合 (Set)
numbers = {1, 2, 3, 3, 4}         # 自動移除重複的 3
print("集合：", numbers)           # 輸出：{1, 2, 3, 4}
numbers.add(5)                     # 添加元素
print("新增後：", numbers)         # 輸出：{1, 2, 3, 4, 5}


''' 6. Functions '''

# 計算面積的函數
def calc_area(width, height):
    area = width * height
    return area

w = float(input("請輸入寬："))
h = float(input("請輸入高："))
result = calc_area(w, h)
print("面積為:", result)

# 簡單問候函數
def greet(name):
    return "你好, " + name + "!"

print(greet("小華"))  # 輸出：你好, 小華!

