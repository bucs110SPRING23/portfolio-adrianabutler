import turtle
import random
x = random.randrange(1,10)
print(x)

# Race 1

screen = turtle.Screen()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.penup()
turtle1.goto(-100,20)
turtle1.pendown

turtle2.penup()
turtle2.goto(-100,-20)
turtle2.pendown

turtle1.forward(random.randrange(1,100))
turtle2.forward(random.randrange(1,100))

turtle1.penup()
turtle2.penup()

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

# Race 2
turtle1.pendown()
turtle2.pendown()

turtle1.speed(1)
turtle2.speed(2)

turtle1.color("pink")
turtle2.color("green")

for i in range(10):
    turtle1.forward(random.randrange(1,100))
    turtle2.forward(random.randrange(1,100))

turtle1.penup()
turtle2.penup()

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

turtle.exitonclick()

# Part B

import pygame
import math
pygame.init()
window = pygame.display.set_mode()

points = []
side_length = 100
xpos = 300
ypos = 300
num_sides = [ 3, 4, 6, 20, 100, 360]

for side in num_sides:
    window.fill("gray")
    pygame.display.flip()
    pygame.time.wait(2000)
    for i in range(side):
        angle = 360 / side
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x , y])
    pygame.display.flip()
    pygame.draw.polygon(window, "green", points)
    pygame.display.flip()
    pygame.time.wait(2000)
