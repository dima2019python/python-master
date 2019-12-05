print("Привет, как дела?")
a = input('Как тебя зовут?\n')
print('Привет '+ a)
def check_guess(guess, answer):
    global score
    still_guessing=True
    attemp=0
    while still_guessing and attemp < 3:
        if guess.lower() == answer.lower():
            print('Ответ верный')
            score = score + 1
            still_guessing = False
        else:
            if attemp < 2:
                guess = input('Ответ неверный. Попробуйте еще раз')
            attemp = attemp + 1

    if attemp == 3:
        print('Правильный ответ: ' +answer)

score = 0
print('Тест животныые')
import turtle as t
guess1 = input('Какой медведь живет за полярным кругом? ')
check_guess(guess1, 'белый медведь')
guess2= input('какое сухопутное животное самое быстрое? ')
check_guess(guess2, 'гепард' )
guess3= input('какое животное самое боьшое? ')
check_guess(guess3, 'синий кит')
guess4= input('Как быстро страусы могут бегать? ')
check_guess(guess , '70')
guess5= input('Где была выведена собака породы далматин')
check_guess(guess , 'хорватская провинция Далматия? ')
guess6= input('Какая пища является основным продуктом питания для панд, живущим на воле?')
check_guess(guess , 'бамбук')
guess7= input('Какого цвета кожа полярного медведя?')
check_guess(guess , 'чёрного')
guess8= input('Как быстро колибри машет крыльями?')
check_guess(guess , '200 взмахов в секунду')
guess9= input('Какие два вида млекопитающих откладывают яйца? ')
check_guess(guess , 'ехидны и утконосы')
guess10= input('Какие виды морских черепах самые большие?')
check_guess(guess , 'кожистые черепахи')
print('Вы наброали очков: ' + str(score))




     
