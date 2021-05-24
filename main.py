from turtle import Turtle, Screen
import random
import turtle
timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')

colours = ['cornflower blue', 'sky blue', 'yellow green', 'medium spring green',
           'dark sea green', 'dark khaki', 'light pink', 'blue violet', 'medium purple']

timmy.pensize(1)


def draw_shape(sides):
    angle = 360/sides
    timmy.color(random.choice(colours))
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


""" draw_shape(3)
draw_shape(4)
draw_shape(5)
draw_shape(6)
draw_shape(7)
draw_shape(8)
draw_shape(9)
draw_shape(10)
draw_shape(11)
draw_shape(12)
 """
timmy.speed(0)

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk():
    for _ in range(400):
        choice = random.randint(1, 4)
        if choice == 1:
            timmy.color(random_color())
            timmy.forward(15)
        if choice == 2:
            timmy.color(random.choice(colours))
            timmy.right(90)
            timmy.forward(15)
        if choice == 3:
            timmy.color(random.choice(colours))
            timmy.right(180)
            timmy.forward(15)
        if choice == 4:
            timmy.color(random.choice(colours))
            timmy.right(250)
            timmy.forward(15)


def spirograph():
    for _ in range(360):
        timmy.color(random_color())
        timmy.circle(80)
        timmy.right(1)


# random_walk()
spirograph()
screen = Screen()
screen.exitonclick()
