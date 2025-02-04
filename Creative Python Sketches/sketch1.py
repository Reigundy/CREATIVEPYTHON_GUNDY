positions = []
def setup():
    size(400, 400)

def draw():
    background(100)
    for pos in positions:
        drawBear(pos["x"], pos["y"])
    
def mouse_clicked(e):
    pos = {
        "x": mouse_x,
        "y": mouse_y
        
    }
    positions.append(pos)
    #print(positions)
    #drawBear(mouse_x, mouse_y)
            
def drawBear(x_pos, y_pos):
    ear_size = 30
    spacing = 20
    circle(x_pos - spacing, y_pos - spacing, ear_size)
    circle(x_pos + spacing, y_pos + spacing, ear_size)
    circle(x_pos, y_pos, 50)
    
run_sketch()
