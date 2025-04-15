import matplotlib.pyplot as plt

import turtle

from OOP.shape.Shape import EquilateralTriangle

# x = [1, 2, 3, 4]
# y = [5, 6, 7, 8]
#
# plt.plot(x, y)
# plt.title('figure 1')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

et = EquilateralTriangle(100)
t = turtle.Turtle()
for _ in range(3):
    t.forward(et.side)
    t.left(120)
turtle.done()

