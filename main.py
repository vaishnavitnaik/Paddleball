from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Ping Pong")
screen.bgcolor("black")


screen.tracer(0)

paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
screen.onkey(paddle2.Up,"+")
screen.onkey(paddle2.Down,"-")


game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    ball.move()
    screen.update()
    #detect collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor()>380:
        ball.reset()
        score.l_score()
    # when left paddle misses
    if ball.xcor() <-380:
        ball.reset()
        score.r_score()

screen.exitonclick()