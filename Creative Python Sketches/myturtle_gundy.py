from turtle import *
import random

title("Fantasy Code Man") # customize the title of your turtle sketch window
shape('turtle')
speed(3000)

def draw_flower(x, y):
    penup()
    goto(x, -150)
    pendown()
    goto(x, y)
    for i in range(5):
        circle(20)
        left(360/5)
onscreenclick(draw_flower)


mainloop() # make the screen stay when the drawing ends