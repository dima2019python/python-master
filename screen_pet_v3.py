from tkinter import *
import time
import random
import pyloc
from pygame import mixer

def open_win(text):
    win = Toplevel()
    win.geometry("200x100+1000+300")
    win.overrideredirect(1)
    win.grab_set()
    l = Label(win, text=text, bg="black", fg="white")
    l.pack(expand=True, fill=BOTH)
    win.after(3000, lambda: win.destroy())


def change_color ():
    pet_colors = ['SkyBlue1', 'tomato', 'yellow', 'dark blue', 'green', 'orange']
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(ear_left, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(ear_right, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(foot_left, outline = c.body_color, fill = c.body_color)
    c.itemconfigure(foot_right, outline = c.body_color, fill = c.body_color)
    root.after(1500, change_color)

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(200, toggle_eyes)
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

def sound1():
    beep = mixer.Sound('lm_coin.wav')
    beep.play()

def sound2():
    beep = mixer.Sound('button-09.wav')
    beep.play()

def sound3():
    beep = mixer.Sound('sigh.wav')
    beep.play()

def sound4():
    beep = mixer.Sound('2fart1.wav')
    beep.play()

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

def show_bunch():
    time.sleep(1)
    sound4()
    bunch1 = c.create_oval(130, 470, 270, 450, outline = 'brown', fill = 'brown', state = NORMAL)
    bunch2 = c.create_oval(150, 460, 255, 440, outline = 'brown', fill = 'brown', state = NORMAL)
    bunch3 = c.create_oval(170, 450, 240, 430, outline = 'brown', fill = 'brown', state = NORMAL)
    return

def sad():
    if c.happy_level == 0:
        sound3()
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)

def dialog():
    global pet_command
    pet_command = e1.get()
    e1.delete(0, last=END)
    if pet_command == 'привет':
       # open_win('как тебя зовут?')
       # name = e1.get()
        open_win('приветствую' + name)

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
        sound1()
        body = c.create_oval(15, 20, 395, 350, outline=c.body_color, fill=c.body_color)
        root.after(2000, show_bunch)
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

def remove_bunch():
    sound2()
    bunch = c.create_oval(130, 470, 270, 450, outline = 'blue', fill = 'blue', state = NORMAL)
    bunch6 = c.create_oval(150, 460, 255, 440, outline = 'blue', fill = 'blue', state = NORMAL)
    bunch7 = c.create_oval(170, 450, 240, 430, outline = 'blue', fill = 'blue', state = NORMAL)

def delete_start_root():
    root2.destoy()
    
    
sms = ['привет', 'пока',  'приветствую',  'до свидания']
random.choice(sms)

root2 = Tk()
root2.geometry("600x600+350+0")

root = Tk()
root.geometry("600x600+350+0")

f2 = Frame(root)
f2.pack(side=RIGHT)

c = Canvas(f2, width=400, height=500)
c.configure(bg='blue', highlightthickness=0)

banch1 = None
pet_command = None

mixer.init()

c.body_color = 'yellow'
draw_pet()

f3 = Frame(root2)
e3 = Entry(f3)
e3.pack()
f3.pack()
f1 = Frame(root)
f1.pack(side=LEFT)
li = Label(f1, text='Команда для питомца', padx=20, pady=25)
e1 = Entry(f1)
bt = Button(f1, text="отправить", command=dialog, padx=20, pady=10)
btn = Button(f1, text="приветствие", command=open_win, padx=20, pady=25)
btn1 = Button(f1, text="кормить", command=lambda: draw_pet(size="BIG"), padx=20, pady=25)
btn2 = Button(f1, text="убрать кучку", command=remove_bunch, padx=20, pady=25)
li.pack()
e1.pack()
bt.pack()
btn1.pack()
btn2.pack()
btn.pack()

name = e3.get()

c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
c.eyes_crossed = False
c.happy_level = 2
c.tongue_out = False
root.after(1000, blink)
root.after(5000, sad)
root.after(20000, lambda: draw_pet(size='SMALL'))
root.after(1000, change_color)
root.mainloop()
