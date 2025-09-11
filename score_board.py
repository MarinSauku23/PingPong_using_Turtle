from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(x, y)
        self.write(arg=f"{self.score}", align="center", font=('Courier', 24, 'normal'))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"{self.score}", align="center", font=('Courier', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


