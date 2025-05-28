import turtle
import random

# 設定螢幕
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("螢幕刷新控制範例 (Tracer & Update)")

# 關閉螢幕自動刷新
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle() # 隱藏畫筆圖示
pen.speed(0)     # 設定最快繪圖速度 (與 tracer 配合使用)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan", "magenta"]

for _ in range(150): # 繪製 150 個圓圈
    pen.color(random.choice(colors))
    pen.penup()
    x = random.randint(-380, 380)
    y = random.randint(-280, 280)
    pen.goto(x, y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(random.randint(5, 35)) # 隨機半徑
    pen.end_fill()

# 所有繪圖指令完成後，一次性更新螢幕
screen.update()

screen.mainloop()