import turtle
import math

window = turtle.Screen()
window.bgcolor("pink")
pen = turtle.Turtle()
pen.shape("circle")
pen.color("black")

def movePen (pen, x, y):
    pen.penup()
    pen.setposition(x, y)
    pen.pendown()

def movePenX (pen, x):
    pen.penup()
    pen.setx(x)

def movePenY (pen, y):
    pen.penup()
    pen.sety(y)
    pen.pendown()

def positionAlongCircle (x, y, radius, angle):
    radians = math.radians(angle)
    return [ x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]

# Head

movePenY(pen, -150)
pen.circle(150)

# Nose

noseMouthOffset = -15

movePenY (pen, -20 + noseMouthOffset)
pen.circle(20)

# Mouth

movePen(pen, -100, -20 + noseMouthOffset)
pen.right(90)
pen.circle(50, 180)
pen.left(180)
pen.circle(50, 180)

# Eyes

eyeSpacingX = 30
eyePosY = 40
eyeRadius = 30

movePen (pen, eyeSpacingX, eyePosY)
pen.right(180)
pen.circle(eyeRadius, -180)

movePen(pen, -eyeSpacingX, eyePosY)
pen.circle(eyeRadius, 180)

# Tongue

movePen (pen, -20, -60 + noseMouthOffset)
pen.circle(20, 180)

# Ears

earBeginAngle = 25
earSize = 85
earWidth = 22
positionA = positionAlongCircle(0, 0, 150, earBeginAngle)
movePen(pen, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, earBeginAngle + earWidth)
pen.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
pen.setposition(positionC[0], positionC[1])

positionA = positionAlongCircle(0, 0, 150, -earBeginAngle)
movePen(pen, positionA[0], positionA[1])

positionB = positionAlongCircle(0, 0, 150 + earSize, -earBeginAngle + - earWidth)
pen.setposition(positionB[0], positionB[1])

positionC = positionAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
pen.setposition(positionC[0], positionC[1])

# Whiskers

whiskerLength = 180

movePen(pen, 50, -15)
pen.setheading(0)
pen.forward(whiskerLength)

movePen(pen, 50, 0)
pen.left(5)
pen.forward(whiskerLength)

movePen(pen, -50, -15)
pen.setheading(180)
pen.forward(whiskerLength)

movePen(pen, -50, 0)
pen.left(-5)
pen.forward(whiskerLength)

window.exitonclick()