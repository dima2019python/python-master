from random import randrange, randint
from tkinter import Canvas, Tk, messagebox, font


def create_stars():
    x = randrange(10, 740)
    y = randrange(10, 450)
    c.create_oval(x, y, x + star_wight, y + star_height, fill='white', width=0)

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text='Жизней: ' + str(lives_remaining))


def create_met():
    x = randrange(10, 740)
    y = 10
    new_met = c.create_oval(x, y, x + met_wight, y + met_height, fill='brown', width=0)
    meteors.append(new_met)
    root.after(met_interval, create_met)


#if objectA.right > objectB.left and
# objectA.left < objectB.right and
# objectA.top < objectB.bottom and
# objectA.bottom > objectB.top
# [400.0, 400.0, 475.0, 490.0]


def check_ship():
    (ship_x, ship_y, ship_x2, ship_y2) = c.coords(space_ship)
    for met in meteors:
        (met_x, met_y, met_x2, met_y2) = c.coords(met)
        if ship_x < met_x and met_x2 < ship_x2 and ship_y2 - met_y2 < 40:
            lose_a_life()
            meteors.remove(met)
            c.delete(met)
    root.after(100, check_ship)


def move_met():
    for met in meteors:
        (met_x, met_y, met_x2, met_y2) = c.coords(met)
        c.move(met, 0, randrange(7, 15))
        if met_y2 > canvas_height:
            meteors.remove(met)
            c.delete(met)
    root.after(met_speed, move_met)


def move_left(event):
    (x1, y1, x2, y2) = c.coords(space_ship)
    if x1 > 0:
        c.move(space_ship, -25, 0)
        #c.move(space_ship_win, -25, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(space_ship)
    if x2 < canvas_width:
        c.move(space_ship, 25, 0)
        #c.move(space_ship_win, 25, 0)

canvas_width = 850
canvas_height = 500

root = Tk()

root.title('Space adventure')

c = Canvas(root, width=canvas_width, height=canvas_height, background='dark blue')
c.pack()

star_color = ['yellow', 'dark blue', 'red', 'pink', 'light green']
star_wight = 10
star_height = 10

for i in range(30):
    create_stars()

met_wight = 85
met_height = 85
met_speed = 550
met_interval = 4000
difficylti_factor = 0.95

space_ship_color = 'grey'
space_ship_wight = 75
space_ship_height = 90
win_wight = 30
win_height = 30
x = 400
y = 300
space_ship = c.create_oval(x, y, x + space_ship_wight, y + space_ship_height, fill=space_ship_color, width=0)
#space_ship_win = c.create_rectangle(417, 310, 454, 330, outline='red', fill='white')
print(c.coords(space_ship))


game_font = font.nametofont('TkFixedFont')
game_font.config(size=20)

lives_remaining = 3
lives_text = c.create_text(canvas_width - 10, 10, anchor='ne', font=game_font, fill='white',
                           text='Жизней: ' + str(lives_remaining))

meteors = []

if lives_remaining == 0:
    messagebox.showinfo('Конец игры!')
    root.destroy()


c.bind('<Left>', move_left)
c.bind('<Right>', move_right)
c.focus_set()

root.after(1000, create_met())
root.after(1000, move_met())
root.after(1000, check_ship())

root.mainloop()
