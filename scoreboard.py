from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER", align="center", font=FONT)


    def update_score(self):
        self.score += 1
        self.update_scoreboard()