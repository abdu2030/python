from turtle import Turtle
import os

FONT = ("Courier", 15, "bold")
GAME_OVER_FONT = ("Courier", 24, "bold")
HIGHSCORE_FILE = "highscore.txt"

# Resolve path relative to this script
current_dir = os.path.dirname(os.path.abspath(__file__))
HIGHSCORE_PATH = os.path.join(current_dir, HIGHSCORE_FILE)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.lives = 3
        self.high_score = self.load_high_score()
        self.color("white")  # White color displays well on the green sidewalk
        self.update_scoreboard()

    def load_high_score(self):
        """Load persistent high score from highscore.txt."""
        if os.path.exists(HIGHSCORE_PATH):
            try:
                with open(HIGHSCORE_PATH, "r") as file:
                    return int(file.read().strip())
            except Exception:
                pass
        return 1

    def save_high_score(self):
        """Save current high score to highscore.txt."""
        try:
            with open(HIGHSCORE_PATH, "w") as file:
                file.write(str(self.high_score))
        except Exception:
            pass

    def update_scoreboard(self):
        self.clear()
        
        # Draw current level & high score on the left
        self.goto(-280, 265)
        self.color("black")  # Dark text is very readable on the bright green sidewalk
        self.write(f"Level: {self.level}   HI: {self.high_score}", align="left", font=FONT)
        
        # Draw lives on the right
        self.goto(280, 265)
        lives_display = "❤️ " * self.lives if self.lives > 0 else "💀"
        self.color("red" if self.lives > 0 else "black")
        self.write(f"Lives: {lives_display}", align="right", font=FONT)

    def l_point(self):
        """Call when player levels up."""
        self.level += 1
        if self.level > self.high_score:
            self.high_score = self.level
            self.save_high_score()
        self.update_scoreboard()

    def lose_life(self) -> bool:
        """Subtract a life. Returns True if lives > 0, False if Game Over."""
        self.lives -= 1
        self.update_scoreboard()
        return self.lives > 0

    def draw_game_over(self):
        """Draw game over card on the screen."""
        self.goto(0, 15)
        self.color("red")
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
        
        self.goto(0, -25)
        self.color("black")
        self.write(f"Final Level: {self.level}", align="center", font=FONT)
