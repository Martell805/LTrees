import turtle

WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.delay(0)

tur = turtle.Turtle()
tur.pensize(3)
tur.speed(0)
tur.penup()
tur.pendown()
tur.color('orange')

gens = 0
axiom = 'AB'
rules = {
    'A': 'AB',
    'B': 'A'
}
actions = 