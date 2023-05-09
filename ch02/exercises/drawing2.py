import turtle
sides=input("Enter the number of sides:")
sides=int(sides)
length=int(input("Enter the length of sides"))
pen=turtle.Turtle()
pen.color("orange")
window=turtle.Screen()
for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)
window.exitonclick()

import pygame
pygame.init()
screen = pygame.display.set_mode()
#screen: is just a variable in pygame
#pygame: module
#display: submodule pygame