from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.ballspeed = 1.5
        self.speed(self.ballspeed)

    def move_ball(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_off_paddles(self):
        self.x_move *= -1

    def bounce_off_walls(self):
        self.y_move *= -1

    def reset_ball(self):
        self.ballspeed = 1.5
        self.goto(0, 0)
        self.bounce_off_paddles()

    def increase_ball_speed(self):
        self.ballspeed *= 1.1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=('Arial', 24, 'normal'))
