import matplotlib.pyplot as plt

import turtle

from EquilateralTriangle import EquilateralTriangle


if __name__ == "__main__":
    # s = Square(100)
    # length = s.length
    # vertices_x = [0, length, length, 0, 0]
    # vertices_y = [0, 0, length, length, 0]
    #
    # plt.figure()
    # plt.plot(vertices_x, vertices_y, 'b-')
    # plt.title("Square")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axis("equal")

    # c = Circle(50)
    # theta = np.linspace(0, 2 * np.pi, 100)
    # circle_x = c.radius + c.radius * np.cos(theta)
    # circle_y = c.radius + c.radius * np.sin(theta)
    #
    # plt.figure()
    # plt.plot(circle_x, circle_y, 'r-')
    # plt.title("Circle")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axis("equal")

    # et = EquilateralTriangle(100)
    #
    # v0 = (0, 0)
    # v1 = (et.side, 0)
    # v2 = (et.side/2, et.get_height())
    #
    # vertices = [v0, v1, v2, v0]
    # vertices_x = [v[0] for v in vertices]
    # vertices_y = [v[1] for v in vertices]
    #
    # plt.figure()
    # plt.plot(vertices_x, vertices_y, 'g-')
    # plt.title("Equilateral Triangle")
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.axis("equal")
    #
    # plt.show()

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

