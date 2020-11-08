import turtle

wind = turtle.Screen()
wind.title("Ping Pong By Monaya")
wind.bgcolor("Black")
wind.setup(width=800, height=600)
wind.tracer(0)

m1 = turtle.Turtle()
m1.speed(0)
m1.shape("square")
m1.color("blue")
m1.penup()
m1.goto(-350, 0)
m1.shapesize(stretch_wid=5, stretch_len=1)

m2 = turtle.Turtle()
m2.speed(0)
m2.shape("square")
m2.color("red")
m2.penup()
m2.goto(350, 0)
m2.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

score1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0",align="center", font=("courier", 24, "normal"))


def m1_up():
    y = m1.ycor()
    y += 20
    m1.sety(y)


def m1_down():
    y = m1.ycor()
    y -= 20
    m1.sety(y)


def m2_up():
    y = m2.ycor()
    y += 20
    m2.sety(y)


def m2_down():
    y = m2.ycor()
    y -= 20
    m2.sety(y)


wind.listen()
wind.onkeypress(m1_up, "w")
wind.onkeypress(m1_down, "s")
wind.onkeypress(m2_up, "Up")
wind.onkeypress(m2_down, "Down")

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1,score2), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < m2.ycor() + 40 and ball.ycor() > m2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < m1.ycor() + 40 and ball.ycor() > m1.ycor() - 40):
         ball.setx(-340)
         ball.dx *= -1
