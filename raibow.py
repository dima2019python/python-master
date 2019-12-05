import random
import turtle as t
import time

def get_line_lenght():
    choice = input('выберите длинну линий(длинные,средние,короткие): ')
    if choice == 'длинные':
        line_lenght = 250
    elif choice == 'средние':
        line_lenght = 200
    else:
        line_lenght = 100
    return line_lenght

def get_line_width():
    choice = input('выберите толщину линий(суперширокие,широкие,тонкие): ')
    if choice == 'суперширокие':
        line_wigth = 40
    elif choice == 'широкие':
        line_wigth = 25
    else:
        line_wigth = 10
    return line_wigth



line_lenght = get_line_lenght()


def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x,y)=t.pos()
    inside = left_limit < x <right_limit and bottom_limit < y < top_limit
    return inside

def move_turtle(line_lenght):
    pen_colors = ['red','orange','yellow','green','blue','purple']
    t.pencolor(random.choice(pen_colors))
    if inside_window():
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_lenght)
    else:
        t.backward(line_lenght)
        
        
line_wigth = get_line_width()

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_wigth)

while True:
    move_turtle(line_lenght)