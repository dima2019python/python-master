from tkinter import Tk, simpledialog,messagebox


def read_from_file():
    with open('capital_data.txt',encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
            
def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a', encoding='utf=8') as file:
        file.write(country_name + '/' + city_name + '\n')
    

print('знаток-столицы мира')
root = Tk()
root.withdraw()

the_world = {}

read_from_file()


while True:
    guery_country = simpledialog.askstring('Страна','Введите название страны:' )

    if guery_country in the_world:
        result = the_world[guery_country]
        messagebox.showinfo('ответ',
                            guery_country + ': столица этой страны - ' + result + '!')
    else:
        new_city = simpledialog.askstring('научите меня',
                                          'я не знаю, ' +
                                          'как называется столица страны ' + guery_country + '!')
        the_world[guery_country] = new_city
        write_to_file(guery_country, new_city)

root.mainloop
