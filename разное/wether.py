from tkinter import ttk
import requests
from tkinter import messagebox
import time
from ttkthemes import ThemedTk


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']

        return f'Местоположение: {city}, {country} \nТемпература: {temp} C \nАтм. давление: {press} гПа \n' \
               f'Влажность: {humidity}% \nСкорость ветра: {wind} м/с \nПогдные условия: {desc}'
    except:
        return 'Ошибка получения данных ...'


def get_weather(event=''):
    if not e.get():
        messagebox.showerror(title='Error', message='Введите запрос в формате city, country_code')
    else:
        params = {
            'appid': API_KEY,
            'q': e.get(),
            'units': 'metric',
            'lang': 'ru'
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        l['text'] = print_weather(weather)


root = ThemedTk(theme="arc")
root.geometry('500x400')
root.resizable(0, 0)

API_KEY = 'd252670b1a076d7d62ebd3eea58a3bab'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

e = ttk.Entry(top_frame)
e.place(relwidth=0.7, relheight=1)

e = ttk.Entry(top_frame)
e.place(relwidth=0.7, relheight=1)

b = ttk.Button(top_frame, text='Запрос погоды', command=get_weather)
b.place(relx=0.7, relwidth=0.3, relheight=1)

low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

l = ttk.Label(low_frame, anchor='n')
l.place(relwidth=1, relheight=1)

e.bind('<Return>', get_weather)

root.mainloop()
