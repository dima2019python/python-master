from tkinter import *


def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)


def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False


def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False


def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1500, toggle_tongue)
    root.after(1500, toggle_pupils)
    return


def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 1
    return


def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return


def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)


def draw_pet(size="NORM"):
    global body
    global ear_left
    global ear_right
    global foot_left
    global foot_right
    global eye_left
    global pupil_left
    global eye_right
    global pupil_right
    global mouth_normal
    global mouth_happy
    global mouth_sad
    global tongue_main
    global tongue_tip
    global cheek_left
    global cheek_right
    c.delete("all")
    if size == 'BIG':
        body = c.create_oval(15, 20, 395, 350, outline=c.body_color, fill=c.body_color)
    elif size == 'SMALL':
        body = c.create_oval(40, 20, 360, 350, outline=c.body_color, fill=c.body_color)
    else:
        body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
    ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
    ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
    foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
    foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

    eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
    pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
    eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
    pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

    mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
    mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
    mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
    tongue_main = c.create_rectangle(170, 250, 230, 270, outline='red', fill='red', state=HIDDEN)
    tongue_tip = c.create_oval(170, 250, 230, 300, outline='red', fill='red', state=HIDDEN)

    cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
    cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)


root = Tk()

c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)

c.body_color = 'yellow'
draw_pet()

btn = Button(text="кормить", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=lambda: draw_pet(size="BIG"))
btn.pack()

c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
c.eyes_crossed = False
c.happy_level = 2
c.tongue_out = False
root.after(1000, blink)
root.after(5000, sad)
root.after(6000, lambda: draw_pet(size='SMALL'))
root.mainloop()
