from myFunctions import *
from random import randint

turtle.bgcolor("black")
turtle.colormode(255)

#bob.speed(0)
turtle.tracer(0)

for times in range(210):
    fill = (0, times+10, 200)
    jump(times*-3, times * 3.5)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(50)

for times in range(210):
    fill = (times+40, times+10, 200)
    jump(times*-2.9, times * 0)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(50)

for times in range(210):
    fill = (times+10, 0, 200)
    jump(times*-3, times * -3.5)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(50)

for times in range(210):
    fill = (times, times, 210)
    jump(times-10, times * -3.5)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(50)

for times in range(210):
    fill = (times+10, times+40, 200)
    jump(times*2.9, times * 0)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(50)

for times in range(210):
    fill = (times+40, times, 250)
    jump(times+10, times * 3.4)
    circle(times+ 15 - 10, "yellow", fill)
    bob.right(-50)

home()
bob.setheading(0)
for times in range(10):
    bob.left(times*800)
    comet("yellow",80,15)
    home()
    bob.setheading(0)

for times in range(10):
    bob.left(times*36+36)
    comet("yellow",11,15)
    home()
    bob.setheading(0)

for times in range(10):
    bob.left(times*36+24)
    comet("yellow",11,15)
    home()
    bob.setheading(0)

for times in range(10):
    bob.left(times*36+12)
    comet("yellow",11,15)
    home()
    bob.setheading(0)
