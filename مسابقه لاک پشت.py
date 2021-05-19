from turtle import*
from random import*
from time import*

bgcolor('green')
turtle_number = 6

dis_list = [0,0,0,0,0]
rand_list = [0]*20
random_color = ["red","yellow","blue","purple","orange"]
name = ["tud","bob","rob","tub","bot"]

while int(turtle_number)>5 or int(turtle_number)<2:
    turtle_number = int(textinput("Enter the Turtle number","Maximium number is 5 and Minimium is 2"))

def timer(secound,x,y,my_color,my_font,size,bold_size) :
    pu()
    goto(x,y)
    pd()
    for i in (range(secound)):
        color(my_color)
        write(i+1,align="center",font=(my_font,size,bold_size))
        sleep(1)
        color('green')
        pensize(100)
        goto(x,y)
    color(my_color)
    write("Go!",align="center",font=("Arial",size+10,"normal"))

def write_text(x,y,my_color,text,align,font,font_bold,font_size):
    pu()
    goto(x,y)
    pd()
    color(my_color)
    write(text,align=align,font=(font,font_size,font_bold))
    hideturtle()


for j in range(turtle_number):
    name[j] = Turtle()
    name[j].shape("turtle") 
    name[j].color(random_color[j])
    name[j].pu()
    name[j].goto(-200,200-(j*70))
    name[j].pensize(5)
    name[j].pd()

pu()
goto(+200,220)
pd()
pensize(3)
color("white")
setheading(270)
fd(turtle_number*70-20)

write_text(0,-150,"white","Turtles Race","center","Arial","normal",20)

timer(3,0,-200,"white","Arial",30,"normal")

go = 1


while(go==1):
    for i in range(turtle_number):
        rand_list[i] = randint(0,20)
        name[i].fd(rand_list[i])
        dis_list[i] += rand_list[i]
        if (dis_list[i]>400):
            name[i].pu()
            name[i].goto(0,250)
            go = 0

write_text(0,255,"white","Winner","center","Arial","normal",20)
        

mainloop()