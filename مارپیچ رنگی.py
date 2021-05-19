from turtle import*
speed(1000)
j=0
a = ["red","blue","green","yellow"]
for i in range(0,1000,5):
    j=j+1
    c = j%4
    color(a[c])
    forward(i)
    left(90)
