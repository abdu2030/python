from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("red")
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)
    def l_point(self):
        self.level += 1
        self.update_scoreboard()
