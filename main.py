from turtle import Screen
from puddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard


screen = Screen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_paddle_score = ScoreBoard(100, 260)
l_paddle_score = ScoreBoard(-100, 260)


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1 / ball.ballspeed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_off_walls()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_off_paddles()
        ball.increase_ball_speed()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_off_paddles()
        ball.increase_ball_speed()

    if ball.xcor() > 390:
        ball.reset_ball()
        l_paddle_score.increase_score()

    if ball.xcor() < -390:
        ball.reset_ball()
        r_paddle_score.increase_score()

    if r_paddle_score.score == 5 or l_paddle_score.score == 5:
        game_is_on = False
        ball.game_over()

screen.exitonclick()