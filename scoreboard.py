from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1