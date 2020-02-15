import random
import turtle as t

def outside_window(caterpillar):
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y > top_wall 
    return outside
        

def game_over (score, score2):
    caterpillar.color('yellow')
    caterpillar2.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    if score2 > score:
            t.write('Конец игры! Победил синий', align='center', font=('Arial', 30, 'bold'))
    if score > score2:
        t.write('Конец игры! Победил красный', align='center', font=('Arial', 30, 'bold'))
    if score == score2:
        t.write('Конец игры! Победилa дружба', align='center', font=('Arial', 30, 'bold'))
    
    
def display_score (current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 30, 'bold'))
    
def display_score2 (current_score2):
    score_turtle2.clear()
    score_turtle2.penup()
    x = (t.window_width() / 2) - 900
    y = (t.window_height() / 2) - 50
    score_turtle2.setpos(x, y)
    score_turtle2.write(str(current_score2), align='left', font=('Arial', 30, 'bold'))
    

def place_leaf ():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

def start_game ():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    score2 = 0
    text_turtle.clear()
    
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar_speed2 = 2
    caterpillar_length2 = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    caterpillar2.shapesize(1, caterpillar_length2, 1)
    caterpillar2.setheading(180)
    caterpillar2.showturtle()
    display_score(score)
    display_score2(score2)
    place_leaf()



    
    while True:
        caterpillar.forward(caterpillar_speed)
        caterpillar2.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if caterpillar2.distance(leaf) < 20:
            place_leaf()
            caterpillar_length2 = caterpillar_length2 + 1
            caterpillar2.shapesize(1, caterpillar_length2, 1)
            caterpillar_speed2 = caterpillar_speed2 + 1
            score2 = score2 + 10
            display_score2(score2)
        if outside_window(caterpillar) or outside_window(caterpillar2):
            game_over(score, score2)
            break
        
def move_up ():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
        
def move_down ():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
        
def move_left ():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
        
def move_right ():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
        
def  catepillar2_move_up ():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(90)
        
def catepillar2_move_down ():
    if caterpillar2.heading() == 0 or caterpillar2.heading() == 180:
        caterpillar2.setheading(270)
        
def catepillar2_move_left ():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(180)
        
def catepillar2_move_right ():
    if caterpillar2.heading() == 90 or caterpillar2.heading() == 270:
        caterpillar2.setheading(0)

t.bgcolor('yellow')

caterpillar  = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

caterpillar2 = t.Turtle()
caterpillar2.shape('square')
caterpillar2.color('blue')
caterpillar2.speed(0)
caterpillar2.penup()
caterpillar2.hideturtle()



leaf = t.Turtle()
leaf_shape = ((0, 0), (15, 3), (19, 7), (21, 21), (7, 19), (3, 15))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write('нажмите пробел, чтобы начать игру', align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

score_turtle2 = t.Turtle()
score_turtle2.hideturtle()
score_turtle2.speed(0)

t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left, 'Left')
t.onkey(catepillar2_move_up, 'w')
t.onkey(catepillar2_move_down, 's')
t.onkey(catepillar2_move_right, 'd')
t.onkey(catepillar2_move_left, 'a')
t.listen()

t.mainloop()


