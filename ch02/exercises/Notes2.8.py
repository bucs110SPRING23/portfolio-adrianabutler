#mynums=[]
#var=int(input("Enter a number:"))
#mynums.append(var)
#print(mynums)
#mynums=[]
#var=int(input("Enter another number:"))
#mynums.append(var)
#print(mynums)
#mynums=[]
#var=int(input("Enter another number:"))
#mynums.append(var)
#print(mynums)


## for loop allows you to repeat a sequential algorithm on sequential data
#for iterating_variable in sequence:
    # itll do something with said variable

#msg = "Enter 3 numbers"
#mynums=[]
#for i in [0,0,0]:
#    var = int(input(":"))
#    mynums.append(var)
#    print(mynums)
#print("all done")

    #Block Statement
    #always ends in a colon

for ch in "hello":
    print(ch)

## range ()
#'range(5)' = [0,1,2,3,4]
#range generates list values dynamically
[0]*100 #generates a list of 100 0's and stores it in memory

result = range(5) #starts at 0 (default), stops at 5 (non inclusive)
print(list(result))
result = range(1,5) #starts at 1 (inclusive), stops at 5(non inclusive)
print(list(result))
result=range(1,20,2) #starts at 1 (inclusive), stops at 20(noninclusive) steps by 2
print(list(result))
result=range(11)
print(list(result))
result=range(3,10,2)
print(list(result))
result=range(100,-1,-1)
print(list(result))
## range(stop)  range(start,stop)   range(start,stop,step)
import turtle
donatello = turtle.Turtle()
donatello.shape("turtle")

colors = ["red","purple","cyan", "yellow"]
for colors in colors:
    donatello.color(colors)
    for _ in range(4):
        donatello.left(90)
        donatello.forward(50)
    donatello.up()
    donatello.forward(100)
    donatello.down()
window=turtle.Screen()
window.exitonclick()

## pygame

import pygame
pygame.init()
screen=pygame.display.set_mode()
screen.fill("red")
pygame.display.flip()
input("press enter to continue...")
screen.fill("green")
pygame.display.flip()
input("Press Enter to continue")
