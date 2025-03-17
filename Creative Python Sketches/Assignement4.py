from turtle import *
import math
import random

title("Honeycomb Pattern")  # Set window title
shape('turtle')
speed(100)
hideturtle()

HEX_SIZE = 50  # Side length of hexagons
GRID_SPACING_X = HEX_SIZE * 1.5
GRID_SPACING_Y = HEX_SIZE * math.sqrt(3)

hexagons = []  # Store drawn hexagons as (x, y) coordinates

# Function to draw a hexagon 
def draw_hexagon(x, y):
    penup()
    goto(x, y)
    pendown()
    
    # honey-colored border
    color("gold")
    pensize(3)
    
    # Random fill color
    fillcolor(random.choice(["black", "gray", "white"]))
    
    begin_fill()
    for _ in range(6):
        forward(HEX_SIZE)
        right(60)
    end_fill()
    
    # Store the hexagon's center in a grid-like structure
    hexagons.append((x, y))

# Function to snap clicks to the ""honeycomb grid"
def snap_to_grid(x, y):
    """Finds the nearest valid hexagon placement position."""
    col = round(x / GRID_SPACING_X)
    row = round(y / GRID_SPACING_Y)

    # Offset every other row (honeycomb)
    if row % 2 == 1:
        x = col * GRID_SPACING_X + (GRID_SPACING_X / 2)
    else:
        x = col * GRID_SPACING_X
    y = row * GRID_SPACING_Y

    return x, y

# On-screen click event handler
def on_click(x, y):
    x, y = snap_to_grid(x, y)
    
    # Check if a hexagon is already in that position (if so wont draw again)
    if (x, y) not in hexagons:
        draw_hexagon(x, y)

# Set up event listener for clicking
onscreenclick(on_click)

mainloop()  # Keeps the window openx