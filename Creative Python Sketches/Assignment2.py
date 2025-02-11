angl3 = -20  # Initial angle

def setup():
    size(800, 800)

def draw():
    background(227, 213, 184)
      # Move origin to the ellipse's center
    translate(400, 400)  
 
  # Half Elipse
    rotate(angl3)  
    fill(0, 0, 255)  # Blue fill
    no_stroke()
    arc(0, 0, 500, 450, 0, PI, CHORD)  # Half ellipse centered at new origin
    
    reset_matrix()
    # Quarter-circle
    translate(400, 400)
    rotate(140)
    fill(255, 0, 0)  # Blue fill
    no_stroke()
    arc(0, 0, 500, 500, 0, 2, CHORD)
    reset_matrix()
    
    translate(400, 400)
    fill(255, 174, 66)
    rotate(-31)
    arc(-40, 0, 400, 400, 0, PI, CHORD) 
    reset_matrix()
    
    no_fill()
    translate(400, 400)
    stroke(0)       
    stroke_weight(5)  
    ellipse(0, -100, 450, 450)
    reset_matrix()
    no_stroke()
    
    fill(0, 0, 0)
    triangle(200, 255, 268, 197, 310, 560)
    reset_matrix()
    
    fill(255, 179, 71)
    triangle(175, 255, 110, 155, 360, 200)
    reset_matrix()
    
    fill(255, 179, 71)
    triangle(500, 660, 460, 200, 645, 560)
    reset_matrix()
    
    fill(204, 85, 0)
    triangle(560, 680, 520, 420, 640, 617)
    reset_matrix()
    
    fill(255, 0, 0)
    triangle(250, 620, 342, 162, 640, 333)
    reset_matrix()
    
    fill(0, 0, 255)
    triangle(218, 600, 243, 155, 495, 140)
    reset_matrix()
    
    translate(200,470)
    fill(70, 139, 151)
    ellipse(0, 0, 65, 65)
    reset_matrix()
    translate(205,470)
    fill(250, 243, 224)
    ellipse(0, 0, 45, 45)
    reset_matrix()
    translate(200,470)
    fill(255, 174, 66)
    ellipse(0, 0, 30, 30)
    reset_matrix()
    translate(200,470)
    fill(0, 0, 0)
    ellipse(0, 0, 15, 15)
    reset_matrix()
    
    translate(270,300)
    fill(250, 243, 224)
    ellipse(0, 0, 165, 65)
    reset_matrix()
    translate(270,300)
    fill(58, 95, 205)
    ellipse(0, 0, 50, 50)
    reset_matrix()
    translate(270,300)
    fill(0, 0, 0)
    ellipse(0, 0, 25, 25)
    reset_matrix()
    
    translate(450,240)
    fill(250, 243, 224)
    ellipse(0, 0, 170, 75)
    reset_matrix()
    translate(450,240)
    fill(144, 123, 166)
    ellipse(0, 0, 60,60)
    reset_matrix()
    translate(450,240)
    fill(0, 0, 0)
    ellipse(0, 0, 50, 50)
    reset_matrix()
    
    translate(335,420)
    fill(212, 138, 158)
    rect(0, 0, 130, 50)
    reset_matrix()
    
    translate(350,370)
    fill(0, 0, 0)
    rect(0, 0, 30, 150)
    reset_matrix()
    
    translate(350,435)
    fill(0, 0, 0)
    rect(0, 0, 50, 20)
    reset_matrix()
    
    translate(358,369)
    fill(0, 0, 0)
    rect(0, 0, 65, 9)
    reset_matrix()
    
    translate(359,74)
    fill(0, 0, 0)
    rect(0, 0, 7, 300)
    reset_matrix()
    
    
    max_radius = 10  
    dx = mouse_x - 450
    dy = mouse_y - 240
    distance = dist(0, 0, dx, dy)

    if distance > max_radius:
        angle = atan2(dy, dx)
        dx = cos(angle) * max_radius
        dy = sin(angle) * max_radius

    
    fill(0, 0, 0)
    ellipse(dx+450 , dy+240 , 50, 50)
    fill(0, 0, 0)
    ellipse(dx+270 , dy+300 , 25, 25)
    fill(0, 0, 0)
    ellipse(dx+200 , dy+470 , 15, 15)
    
    # Display the mouse coordinates
    fill(0)  
    text_size(16)
    text(f"Mouse: ({mouse_x}, {mouse_y})", 20, 20)  # Display in top-left corner
    
run_sketch()
