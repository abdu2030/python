from turtle import Turtle

FONT_SCORE    = ("Courier", 40, "bold")
FONT_LABEL    = ("Courier", 14, "normal")
FONT_GAME_OVER = ("Courier", 36, "bold")
FONT_SUB      = ("Courier", 16, "normal")

WIN_SCORE = 7   # First player to reach this wins the match


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self._draw_player_labels()
        self.update_scoreboard()

    # ------------------------------------------------------------------ #
    def _draw_player_labels(self):
        """Draw static 'Player 1' / 'Player 2' (or 'CPU') labels once."""
        self.goto(-200, 250)
        self.color("gray")
        self.write("Player 1", align="center", font=FONT_LABEL)
        self.goto(200, 250)
        self.write("Player 2", align="center", font=FONT_LABEL)
        self.color("white")

    def update_scoreboard(self):
        """Redraw score digits only (not the static labels)."""
        self.clear()
        self._draw_player_labels()    # re-draw after clear()
        self.color("white")
        self.goto(-200, 210)
        self.write(self.l_score, align="center", font=FONT_SCORE)
        self.goto(200, 210)
        self.write(self.r_score, align="center", font=FONT_SCORE)

    # ------------------------------------------------------------------ #
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # ------------------------------------------------------------------ #
    def l_wins(self):
        return self.l_score >= WIN_SCORE

    def r_wins(self):
        return self.r_score >= WIN_SCORE

    # ------------------------------------------------------------------ #
    def draw_game_over(self, winner: str):
        """Overlay a centered win message on the court."""
        self.goto(0, 30)
        self.color("#f1c40f")   # Golden yellow
        self.write(f"{winner} Wins!", align="center", font=FONT_GAME_OVER)
        self.goto(0, -20)
        self.color("gray")
        self.write("Click to exit", align="center", font=FONT_SUB)

    def draw_paused(self):
        """Overlay a PAUSED label."""
        self.goto(0, 30)
        self.color("cyan")
        self.write("PAUSED", align="center", font=FONT_GAME_OVER)
