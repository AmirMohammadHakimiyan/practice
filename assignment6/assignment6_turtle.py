import turtle 
import time
import random
p=turtle.Pen()
x=5
n=2
while True:
    p.pencolor("black")
    n+=1
    color=["green","red","orange"]
    v=random.choice(color)
    f=((n-2)*180)//n-180
    x+=7
    p.width(2)
    for i in range(n):
        p.pencolor(v)
        p.right(f)
        p.forward(x)
    p.pencolor("white")
    p.forward(7)
    p.right(90)
    p.forward(7)
    p.left(90)
    