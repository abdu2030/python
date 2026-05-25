from turtle import Turtle
ALIGNMENT  = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        #self.content = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt") as high:
            content = high.read()
        self.write(f"Score: {self.score} High Score: {content}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt",mode="w") as high:
                high.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
