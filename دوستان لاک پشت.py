from turtle import*
 

def move_right():
    tud.setheading(0)
    bud.setheading(270)
    rob.setheading(180)
    bob.setheading(90)
    tud.fd(100)
    bud.fd(100)
    rob.fd(100)
    bob.fd(100)

def move_left():
    tud.setheading(180)
    bud.setheading(90)
    rob.setheading(0)
    bob.setheading(270)
    tud.fd(100)
    bud.fd(100)
    rob.fd(100)
    bob.fd(100)

def move_up():
    tud.setheading(90)
    bud.setheading(0)
    rob.setheading(270)
    bob.setheading(180)
    tud.fd(100)
    bud.fd(100)
    rob.fd(100)
    bob.fd(100)

def move_down():
    tud.setheading(270)
    bud.setheading(180)
    rob.setheading(90)
    bob.setheading(0)
    tud.fd(100)
    bud.fd(100)
    rob.fd(100)
    bob.fd(100)

tud = Turtle() 
tud.shape("turtle") 
tud.color("red")
tud.setheading(0)

rob = Turtle() 
rob.shape("turtle") 
rob.color("blue") 
rob.setheading(180)

bob = Turtle() 
bob.shape("turtle") 
bob.color("purple") 
bob.setheading(90)

bud = Turtle() 
bud.shape("turtle") 
bud.color("green")
bud.setheading(270)

listen()
onkeypress(move_right ,'Right')
onkeypress(move_left ,'Left')
onkeypress(move_down ,'Down')
onkeypress(move_up ,'Up')


mainloop()