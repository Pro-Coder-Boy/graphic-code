from turtle import*
bgcolor("light green")
color("red")
speed(1000)
for i in range(10):
    for i in range(15,80,6):
        pensize(i)
        forward(10)
    penup()
    goto(0,0)
    pendown()
    left(36)
color("orange")
for i in range(10):
    for i in range(5,40,3):
        pensize(i)
        forward(7)
    penup()
    goto(0,0)
    pendown()
    left(36)
color("red")
for i in range(10):
    for i in range(5,20,2):
        pensize(i)
        forward(4)
    penup()
    goto(0,0)
    pendown()
    left(36)
color("orange")
goto(0,0)
pendown()



