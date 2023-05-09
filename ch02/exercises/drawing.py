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