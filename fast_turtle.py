import turtle as t
from itertools import cycle

colors = cycle(['yellow','green','blue','brown','white','red','orange','khaki'])

def draw_circle(size,angle,shift):
    t.bgcolor(next(colors))
    t.pencolor(next(colors))
    t.shape('turtle')
    t.fillcolor('green')
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 3,angle+1,shift+1)
    
t.bgcolor('black')
t.speed('fastest')
t.pensize(15)
draw_circle(30,0,1)