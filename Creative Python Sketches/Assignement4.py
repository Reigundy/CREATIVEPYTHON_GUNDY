from turtle import *
import math
import random

title("Assignment 4")  #window title
shape('turtle')
speed(3000)

# Function to draw a hexagon at a given position
def draw_hexagon(x, y):
    penup()
    goto(x, y)
    pendown()
    
    color(random.choice(["black", "gray", "white"]))  # random color from this choce
    begin_fill()
    for _ in range(6):
        forward(50)  # Hexagon side length
        right(60)
    end_fill()

#hexagon drawing on mouse click
onscreenclick(draw_hexagon)

mainloop()  # Keeps the window open
