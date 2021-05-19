from turtle import*
from random import*
left(150)
speed(10000)
for i in range(20):
    x = randint(-150,150)
    y = randint(-150,150)
    f = randint(10,50)
    penup()
    goto(x,y)
    pendown()
    forward(f)
    left(90)
    forward(f)
    left(90)
    forward(f)
    left(90)
    forward(f)
    left(90)

    
