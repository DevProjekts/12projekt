#Cannon, hitting targets with projectiles.


from random import randrange
from turtle import *
#The link to the module https://pypi.org/project/freegames/
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#This part of code is responding to tap the screen
def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

#We are returning the True if xy is within screen
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Drawing the ball and the targets
def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#We are creating moving ball and targets
def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
