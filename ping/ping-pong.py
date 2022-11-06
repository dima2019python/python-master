#Создай собственный Шутер!
from random import randint
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, picture,x, y, speed, sizex=100, sizey=100):
        super().__init__()
        self.image = transform.scale(image.load(picture),(sizex,sizey))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def start(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  

         
class Player(GameSprite):
    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x != 0:
            self.rect.x -= 10
        if key_pressed[K_RIGHT] and self.rect.x != 600:
           self.rect.x += 10


window = display.set_mode((700, 500))
display.set_caption('ping-pong')
background = transform.scale(image.load('1614383652_82-p-fon-dlya-rabochego-stola-odnotonnii-svetli-86.jpg'), (700, 500))



FPS = 60
clock = time.Clock()
game = True
finish = False
while game==True:
    for e in event.get():
            if e.type == QUIT:
                game = False
    window.blit(background, (0,0))
    if finish!=True:
        clock.tick(FPS)
    display.update()
