import turtle

def drawSquare(t, size):
    for _ in range(4):
     t.forward(size)
    t.left(90)

def drawFlower(t, numSquares, size):
    angle = 360 / numSquares
    for _ in range(numSquares):
        drawSquare(t, size)
        t.left(angle)

window = turtle.Screen()
window.bgcolor("White")

alex = turtle.Turtle()
alex.color("blue")
alex.speed(10)

drawFlower(alex, 24, 100)

window.exitonclick()



