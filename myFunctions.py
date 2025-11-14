import turtle
bob=turtle.Turtle()

def circle(radius, border_color, fill_color):
    bob.pencolor(border_color)
    bob.fillcolor(fill_color)
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()

def polygon(sides, distance, color):
    angle=360/sides
    for times in range(sides):
        bob.color(color)
        bob.forward(distance)
        bob.left(angle)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def comet(c, distance, angle):
    bob.color(c)
    for times in range(10):
        bob.width(times)
        bob.forward(distance)
        bob.left(angle)

def home():
  bob.penup()
  bob.home()
  bob.pendown()
