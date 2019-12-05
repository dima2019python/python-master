from tkinter import messagebox,simpledialog,Tk

def get_task():
    task = simpledialog.askstring('задание', 'что сделать: зашифровать или расшифровать?')
    return task
