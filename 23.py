nume = 7
user_nume = 0
x = 0  # число попыток

while True:
    user_nume = int(input('отгадай число от 1 до 10: '))
    x = x +  1
    if user_nume == nume:
        print(f'ты угадал число.сделано попыток {x}')
        print('спасибо за игру')
        break
    elif user_nume > nume:
        print('не угадал, число меньше')
    else:
        print('не угадал, число больше')
