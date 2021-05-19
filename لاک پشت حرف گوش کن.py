from turtle import *
penup()
listen()
def draw_circle() : 
    r = int(textinput("Draw circle","Radius:"))
    pendown()
    begin_fill()
    circle(r)
    end_fill()
    penup()
def draw_rectangle() : 
    w = int(textinput("Draw Rectangle","Width:"))
    h = int(textinput("Draw Rectangle","Height:"))
    pendown()
    begin_fill()
    for i in range(2):
        fd(w)
        right(90)
        fd(h)
        right(90)
    end_fill()
    penup()
def change_fcolor() : 
    fc = textinput("Change color","Fill color:")
    fillcolor(fc)
    listen()
    
def change_lcolor() : 
    lc = textinput("Change color","Line color:")
    pencolor(lc)
    listen()
           
def go_right() : 
    if heading()==0 :
        forward(100)
    else :
        setheading(0)
    
def go_left() :
    if heading()==180 :
        forward(100)
    else :
        setheading(180)
def go_up () :
    if heading()==90 :
        forward(100)
    else :
        setheading(90)
def go_down ( ) :
    if heading()==270 :
        forward(100)
    else :
        setheading(270)

shape('turtle')
onkeypress  ( go_up, 'Up')
onkeypress  ( go_down, 'Down')
onkeypress  ( go_right, 'Right')
onkeypress  ( go_left, 'Left')
onkeypress  (clear, 'Delete')
onkeypress  ( pendown, 'Shift_L')
onkeyrelease  ( penup, 'Shift_L')
onkeypress  ( begin_fill, 'Alt_L')
onkeyrelease  ( end_fill, 'Alt_L')
onkeypress  (change_fcolor,'f')
onkeypress  (change_lcolor,'l')
onkeypress  (draw_circle,'c')
onkeypress  (draw_rectangle,'r')




