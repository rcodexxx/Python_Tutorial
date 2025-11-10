# Python 應用題練習

## 題目一：學生成績管理系統

設計一個函數 `analyze_grades(students)`，接收一個字典，其中鍵是學生姓名（字串），值是該學生的成績列表（list）。

函數需要回傳一個新字典，包含每位學生的：
- 平均成績（四捨五入到小數點後一位）
- 等第（A: ≥90, B: ≥80, C: ≥70, D: ≥60, F: <60）
- 是否及格（平均≥60）

**範例輸入：**
```python
students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": [55, 60, 58]
}

result = analyze_grades(students)
```

**期望輸出：**
```python
{
    "Alice": {"average": 84.3, "grade": "B", "pass": True},
    "Bob": {"average": 91.7, "grade": "A", "pass": True},
    "Charlie": {"average": 57.7, "grade": "F", "pass": False}
}
```

---

## 題目二：購物車折扣計算

設計一個函數 `calculate_total(cart, discount_code=None)`，計算購物車總金額。

購物車 `cart` 是一個 tuple 的 list，每個 tuple 包含 `(商品名稱, 單價, 數量)`。

**折扣規則：**
- 若總金額 ≥ 1000，自動打9折
- 若總金額 ≥ 2000，自動打85折
- 若有折扣碼 "VIP"，額外再打95折
- 折扣碼 "NEW100"，折抵100元（在其他折扣後）

**範例輸入：**
```python
cart = [
    ("notebook", 50, 3),
    ("pen", 15, 10),
    ("eraser", 10, 5)
]

print(calculate_total(cart))
print(calculate_total(cart, "VIP"))

cart2 = [
    ("backpack", 800, 2), 
    ("bottle", 250, 2)
]

print(calculate_total(cart2))
print(calculate_total(cart2, "NEW100"))
```

**期望輸出：**
```
350
332.5
1785.0
1685.0
```

## 題目三：圖書館借閱記錄分析

設計一個函數 analyze_borrowing(records)，分析圖書館的借閱記錄。
records 是一個 list，每個元素是一個 tuple，包含 (書名, 借閱者, 借閱天數)。
函數需要回傳一個字典，包含：

- ```popular_books```: 借閱次數最多的前3本書，格式為 list of tuple [(書名, 借閱次數), ...]，按次數由高到低排序
- ```active_readers```: 借閱總天數最多的前3位讀者，格式為 list of tuple [(借閱者, 總天數), ...]，按天數由高到低排序
- ```overdue_count```: 借閱天數超過30天的記錄數量

**範例輸入：**
```python
records = [
    ("Python Basics", "Alice", 14),
    ("Data Structures", "Bob", 28),
    ("Python Basics", "Charlie", 35),
    ("Algorithms", "Alice", 21),
    ("Data Structures", "David", 42),
    ("Python Basics", "Eve", 7),
    ("Algorithms", "Bob", 33),
    ("Data Structures", "Charlie", 15),
    ("Machine Learning", "Alice", 45),
    ("Python Basics", "David", 12)
]

result = analyze_borrowing(records)
print(result)
```

**期望輸出：**
```python
{
    "popular_books": [("Python Basics", 4), ("Data Structures", 3), ("Algorithms", 2)],
    "active_readers": [("Alice", 80), ("Bob", 61), ("David", 54)],
    "overdue_count": 4
}
```