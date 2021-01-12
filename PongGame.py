'''Player 1 controls :
    w = up
    s = down

   Player 2 controls:
    up arrow = up
    down arrow = down
'''
import  turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0        Player 2: 0", align="center", font=("Courier", 24, "normal"))

#score
score1 = 0
score2 = 0
#Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)
def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_down, "Down")
#main game loop
while True:
    wn.update()

    # Paddle Border Checking


    #move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Ball border checking
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() >= 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}        Player 2: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() <= -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}        Player 2: {}".format(score1, score2), align="center",font=("Courier", 24, "normal"))

    # Ball Bounce off Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40  and ball.ycor() > paddle_2.ycor() - 40):
       ball.setx(340)
       ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
'''
    # Speed up game
    count = 0
    while score1 > count and score2 > count:
        if ball.xcor() > 0:
            ball.dx += .000001
            ball.dy += .000001
        else:
            ball.dx -= .000001
            ball.dy -= .000001
        count += 1
        '''