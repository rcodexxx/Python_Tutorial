import turtle
import math

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Vec2D 範例 - Turtle 跟隨滑鼠")
screen.tracer(0) # 為了動畫流暢

follower = turtle.Turtle()
follower.shape("turtle")
follower.color("blue")
follower.penup()
follower.speed(0) # 最快速度 (動畫由 ontimer 控制)

# 目標位置，初始設為螢幕中心
target_pos = turtle.Vec2D(0, 0)

def update_target_position(x, y):
    """當滑鼠在螢幕上移動時更新目標位置 (需要拖曳滑鼠才觸發 onmotion)"""
    global target_pos
    target_pos = turtle.Vec2D(x, y)

# 綁定滑鼠移動事件 (按住滑鼠左鍵拖曳時觸發)
# screen.onmotion(update_target_position) # 若要即時跟隨滑鼠移動
# 或者，使用點擊來設定目標位置：
def set_target_on_click(x,y):
    global target_pos
    target_pos = turtle.Vec2D(x,y)
    follower.clearstamps() # 清除舊的目標標記 (如果有的話)
    follower.goto(x,y)
    follower.stamp() # 在目標位置蓋章
    follower.goto(follower.position()) # 回到原位準備移動

screen.onclick(set_target_on_click) # 點擊設定目標

# 讓螢幕監聽滑鼠事件
# screen.listen() # 如果使用 onmotion 或 onkey

def move_follower_towards_target():
    current_pos = follower.position() # 獲取 Turtle 當前位置 (也是 Vec2D)
    direction_vector = target_pos - current_pos # 計算指向目標的向量

    distance_to_target = abs(direction_vector) # 計算到目標的距離 (向量的模)

    if distance_to_target > 5: # 如果距離大於一個小閾值，才移動
        # 設定 Turtle 朝向目標
        # `towards` 方法返回從 Turtle 到目標點的角度
        angle_to_target = follower.towards(target_pos)
        follower.setheading(angle_to_target)

        # 移動一小步。可以設定固定速度，或根據距離調整速度
        # 這裡我們讓它移動方向向量的一小部分，模擬減速靠近
        move_vector = direction_vector * 0.05 # 移動向量長度的 5%
        if abs(move_vector) > 5: # 最大移動速度限制
            move_vector = move_vector / abs(move_vector) * 5

        follower.goto(current_pos + move_vector) # 更新位置
    else:
        follower.goto(target_pos) # 如果很近，直接到達目標

    screen.update()
    screen.ontimer(move_follower_towards_target, 30) # 約 33 FPS

# 提示文字
info_pen = turtle.Turtle()
info_pen.hideturtle()
info_pen.penup()
info_pen.goto(0, screen.window_height()//2 - 30)
info_pen.write("請點擊螢幕設定目標，藍色烏龜將會跟隨。", align="center", font=("Arial", 14, "normal"))

move_follower_towards_target() # 啟動跟隨動畫
screen.mainloop()