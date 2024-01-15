import random
#turtle är det som används för att röra runt ormen
import turtle as t
#bakgrunds färg
t.bgcolor('Yellow')

#catterpillar är min orm
#importerat t.Turtle som orm
orm = t.Turtle()
#formen på ormen
orm.shape('square')
#färg på ormen
orm.color('pink')
#ställs in för att den inte ska börja röra sig innan spelet startar
#nåt fackar mig med hur den ska röra sig då den tar ett skutt sen slutar
orm.speed(0)
#Pen up används för att den inte ska rita efter sig som turtle vanligtvis gör
orm.penup()
orm.hideturtle()

#vad ormen ska käkas
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('purple')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
#den känner av om spelet har starta eller inte och om den inte har gjort det skriver det hur man startar spelet
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Tryck MELLANSLAG för att börja', align='center', font=('Arial', 16, 'bold'))
text_turtle.hideturtle()
#hur snabb score turteln e samt att den finns, 0 = stå stilla
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
#vägar så man inte kan åka åt helvete för evigt
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = orm.pos()
    outside = \
            x< left_wall or \
            x> right_wall or \
            y< bottom_wall or \
            y> top_wall
    return outside
            
#bestämmer färgen på saker
def game_over():
    orm.color('red')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('DU ÄR SÄMST!', align='center', font=('Arial', 30, 'normal'))
#visar ens score
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))
#placerar ut löven man äter
def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

#känner av om spelet har startad om det är true så startar den loopen med att man flyttar o så
def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

#nåt fackar mig med hur den ska röra sig då den tar ett skutt sen slutar
    orm_speed = 2
    orm_length = 3
    orm.shapesize(1, orm_length, 1)
    orm.showturtle()
    display_score(score)
    place_leaf()
    i=0

#här visar hur mycket större/snabbare man blir av att äta ett löv
    while True:
        orm.forward(orm_speed)
        if orm.distance(leaf) < 20:
            place_leaf()
            orm_length = orm_length + 1
            orm.shapesize(1, orm_length, 1)
            orm_speed = orm_speed + 1
            score = score + 1
            display_score(score)
        if outside_window():
            game_over()
            break
#det här visar vad knapparna gör beroende på vilket håll man åker
def move_up():
    if orm.heading() == 0 or orm.heading() == 180:
        orm.setheading(90)

def move_down():
    if orm.heading() == 0 or orm.heading() == 180:
        orm.setheading(270)

def move_left():
    if orm.heading() == 90 or orm.heading() == 270:
        orm.setheading(180)

def move_right():
    if orm.heading() == 90 or orm.heading() == 270:
        orm.setheading(0)



#här e knapparna o vad de gör
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()







