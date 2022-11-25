import turtle
from math import sqrt
label = turtle.Turtle()

window = turtle.Screen()
window.bgcolor("#dac2bc")

label.speed(1000)
label.color("purple")
label.pensize(5)
label.shape("turtle")
label.right(90)
label.forward(150)
label.left(90)
label.forward(90)
label.left(90)
label.forward(30)

for i in range(4):
    label.left(135)
    label.forward(sqrt((30**2)+(30**2)))
    label.right(45)
    label.forward(15)
    label.right(135)
    label.forward(sqrt((30**2)+(30**2)))
    label.left(45)

label.forward(150-30)
label.left(90)
label.forward(30)
label.left(90)
label.forward(30)

for i in range(8):
    label.left(135)
    label.forward(sqrt((30**2)+(30**2)))
    label.right(135)
    label.forward(15)
    label.right(45)
    label.forward(sqrt((30**2)+(30**2)))
    label.left(45)

label.left(90)
label.forward(90)
label.left(90)
label.forward(30)
label.left(90)
label.forward(60)
label.backward(60)
label.left(90)
label.forward(30)
label.right(90)
label.forward(45)
label.left(90)
label.pensize(0)
label.forward(80)
label.left(115)
label.color("red")
label.pensize(5)

for i in range(65):
    label.forward(5.2)
    label.left(1)

for i in range(180):
    label.forward(1.5)
    label.left(1)

label.right(180)

for i in range(180):
    label.forward(1.5)
    label.left(1)

for i in range(65):
    label.forward(5.2)
    label.left(1)
    
turtle.mainloop()