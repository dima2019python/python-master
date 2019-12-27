from tkinter import messagebox,simpledialog,Tk

def get_task():
    task = simpledialog.askstring('задание', 'что сделать: зашифровать или расшифровать?')
    return task

def get_message ():
    message = simpledialog.askstring('Сообщение','Введите секретное сообщение: ')
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters (message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    
    return new_message

root = Tk()
root.withdraw()
while True:
    task = get_task()
    if task == 'зашифровать':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('сообщение для зашифровки: ', encrypted)
    elif task == 'расшифровать':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Сообщение для дешифровки: ', decrypted)
    else:
        break


 
