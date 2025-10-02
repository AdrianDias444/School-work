import math
import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(600, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Rosa simples mas realista
t.color("#ff6b8b")
t.begin_fill()

for angle in range(360):
    theta = math.radians(angle)

    # Equação paramétrica para forma orgânica
    r = 100 * (0.8 + 0.2 * math.sin(5 * theta)) * (0.9 + 0.1 * math.sin(3 * theta))

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    if angle == 0:
        t.penup()
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

t.end_fill()

# Centro amarelo
t.penup()
t.goto(0, 0)
t.color("gold")
t.begin_fill()
t.circle(12)
t.end_fill()

screen.exitonclick()
