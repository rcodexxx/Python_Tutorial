import turtle
import random

screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.title("事件處理範例 (滑鼠與鍵盤)")

# 用於繪圖的 Turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

# 用於鍵盤控制的 Turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.shapesize(1.5)
player.penup()
player.goto(0, -200) # 初始位置

# 滑鼠點擊事件處理函式
def draw_random_shape_at(x, y):
    """在滑鼠點擊位置 (x, y) 繪製隨機形狀"""
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.random(), random.random(), random.random()) # 隨機 RGB 顏色
    pen.begin_fill()
    size = random.randint(20, 50)
    sides = random.randint(3, 7) # 隨機邊數 (三角形到七邊形)
    for _ in range(sides):
        pen.forward(size)
        pen.left(360.0 / sides)
    pen.end_fill()
    pen.penup()

# 鍵盤事件處理函式
def move_forward():
    player.forward(15)

def turn_left():
    player.left(20)

def turn_right():
    player.right(20)

def clear_drawings():
    pen.clear() # 清除 pen 畫的所有圖形

def quit_program():
    screen.bye() # 關閉 Turtle 視窗

# 綁定滑鼠點擊事件 (點擊螢幕任何位置)
screen.onclick(draw_random_shape_at)

# 開始監聽鍵盤事件
screen.listen()

# 綁定鍵盤按鍵事件
screen.onkeypress(move_forward, "Up")    # 按向上箭頭
screen.onkeypress(turn_left, "Left")     # 按向左箭頭
screen.onkeypress(turn_right, "Right")   # 按向右箭頭
screen.onkey(clear_drawings, "c")        # 按 'c' 鍵清除繪圖
screen.onkey(quit_program, "q")          # 按 'q' 鍵退出程式

# 提示文字
player.goto(0, screen.window_height()//2 - 30)
player.write("點擊螢幕繪製圖形，使用方向鍵移動烏龜，按 'c' 清除，按 'q' 退出",
             align="center", font=("Arial", 12, "normal"))
player.goto(0, -200) # 玩家烏龜回到初始位置

screen.mainloop()
