from tkinter import *
from tkinter import messagebox
import time

def open_win():
    win = Toplevel()
    win.geometry("200x100+1000+300")
    win.overrideredirect(1)
    win.grab_set()
    l = Label(win, text="Hello from TopLevel", bg="black", fg="white")
    l.pack(expand=True, fill=BOTH)
    win.after(3000, lambda: win.destroy())


root = Tk()
# root.geometry("1000x500+500+300")


b1 = Button(root, text="Open", command=open_win, padx=40, pady=5)
b1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

for i in range(5):
    print(1)