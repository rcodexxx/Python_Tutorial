import turtle

class control():
    def __init__(self):
        pass

    @staticmethod    
    def move_forward(player, distance):
        player.forward(distance)

    @staticmethod
    def move_left(player, angle):
        player.left(angle)

    @staticmethod
    def move_right(player, angle):
        player.right(angle)

# 建立畫面
screen = turtle.Screen()
screen.setup(width=1000, height=720)

# 建立烏龜角色
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.shapesize(10, 10)
player.penup()

# 監聽鍵盤事件，使用 lambda 傳參數給 control 類的靜態方法
screen.listen()
screen.onkeypress(lambda: control.move_forward(player, 15), "Up")
screen.onkeypress(lambda: control.move_left(player, 15), "Left")
screen.onkeypress(lambda: control.move_right(player, 20), "Right")
screen.onkeypress(screen.bye, "q")

player.write("按 q 退出", align="center")

screen.mainloop()