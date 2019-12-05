import random

lives=9
print('пицца','ангел','мираж','носки','выдра','петух')
words=['пицца','ангел','мираж','носки','выдра','петух']
secret_word = random.choice(words)
clue = list('?????')
heart_symbol = u'\u2764'
guessed_word_correctly = False


def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
            index = index + 1
            
            
while lives > 0:
    print(clue)
    print('осталось жизней: ' + heart_symbol * lives)
    guess = input('угадайте букву или слово целиком.Выбирайте из списка:')
    
    if guess == secret_word:
        guessed_word_correctly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    
    else:
        
        print('неправильно. Вы теряйте жизнь')
        lives = lives-1
        
        
if guessed_word_correctly:
    print('Победа! Было загадоно слово ' + secret_word)
else:
    print('Пройгрыш! Было загадано слово ' + secret_word)
    
