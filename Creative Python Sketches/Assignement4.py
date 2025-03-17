from turtle import *
import math
import random

# Setup
title("Honeycomb Growth")  
shape('turtle')
speed(100)
hideturtle()

# Hexagon size settings
HEX_SIZE = 50  # Side length of hexagons
HEX_WIDTH = HEX_SIZE * 1.5
HEX_HEIGHT = math.sqrt(3) * HEX_SIZE  # Vertical spacing between rows

# Array to store  placed hexagons as (x, y) coordinates
hexagons = []

# Define valid neighbor offset
HEX_NEIGHBORS = [
    (HEX_WIDTH, 0),           # Right
    (-HEX_WIDTH, 0),          # Left
    (HEX_WIDTH / 2, HEX_HEIGHT / 2),  # Top-Right
    (-HEX_WIDTH / 2, HEX_HEIGHT / 2), # Top-Left
    (HEX_WIDTH / 2, -HEX_HEIGHT / 2), # Bottom-Right
    (-HEX_WIDTH / 2, -HEX_HEIGHT / 2) # Bottom-Left
]

# Function to draw a hexagon
def draw_hexagon(x, y):
    penup()
    goto(x, y - HEX_SIZE / 2)  # Adjust position to center the hexagon
    pendown()
    
    # Set color
    color("gold")  # Border color
    pensize(3)
    fillcolor(random.choice(["black", "gray", "white"]))  # Random fill color
    
    begin_fill()
    for _ in range(6):
        forward(HEX_SIZE)
        right(60)
    end_fill()
    
    # Store new hexagon position
    hexagons.append((x, y))

# Function to find a valid attachment point
def find_valid_attachment(x, y):
    """Finds the closest valid hexagon neighbor to attach to."""
    for hx, hy in hexagons:
        for dx, dy in HEX_NEIGHBORS:
            new_x, new_y = hx + dx, hy + dy
            if (new_x, new_y) not in hexagons:  # Ensure it's not already occupied
                return new_x, new_y  # Return first valid neighbor found
    return None  # No valid neighbor found

# Function to handle mouse clicks
def on_click(x, y):
    if -250 < x < 250 and -250 < y < -220:
        reset_canvas()  # If the reset button is clicked
    elif not hexagons:
        # Place the first hexagon anywhere
        draw_hexagon(x, y)
    else:
        # Try to attach to the closest valid hexagon
        valid_pos = find_valid_attachment(x, y)
        if valid_pos:
            draw_hexagon(*valid_pos)

# the reset button
def draw_reset_button():
    penup()
    goto(-50, -250)
    pendown()
    
    # Button outline
    color("black")
    fillcolor("red")
    begin_fill()
    for _ in range(2):
        forward(100)
        left(90)
        forward(30)
        left(90)
    end_fill()
    
    # Button text
    penup()
    goto(-40, -245)
    color("white")
    write("RESET", font=("Arial", 16, "bold"))

# Function to reset the canvas
def reset_canvas():
    clear()
    hexagons.clear()
    draw_reset_button()

# Draw the reset button initially
draw_reset_button()

# Set up event listener for clicking
onscreenclick(on_click)

mainloop()  # Keeps the window open