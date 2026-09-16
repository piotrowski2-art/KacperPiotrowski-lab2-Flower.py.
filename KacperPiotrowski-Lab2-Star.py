

siurek = "red"
color = "siurek"

import turtle
 
def drawStar(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

bob = turtle.Turtle()
bob.color(siurek)
bob.speed(5)

drawStar(bob, 150)

































