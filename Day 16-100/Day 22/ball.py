from turtle import Turtle
import random

STARTING_SPEED = 10
MAX_SPEED = 25       # Hard cap so ball never becomes impossibly fast
SPEED_INCREMENT = 1  # Added to x/y magnitude each paddle bounce

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_ball()

    def reset_ball(self):
        """Return ball to center with a randomized direction."""
        self.goto(0, 0)
        # Randomize vertical angle; always launch horizontally toward a side
        direction = random.choice([-1, 1])
        self.x_move = STARTING_SPEED * direction
        self.y_move = STARTING_SPEED * random.choice([-1, 1])

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverse vertical direction (wall bounce)."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverse horizontal direction and increase speed (paddle hit)."""
        self.x_move *= -1
        # Increase speed, capped at MAX_SPEED
        if abs(self.x_move) < MAX_SPEED:
            self.x_move += SPEED_INCREMENT * (1 if self.x_move > 0 else -1)
        if abs(self.y_move) < MAX_SPEED:
            self.y_move += SPEED_INCREMENT * (1 if self.y_move > 0 else -1)

    # Keep legacy game_over name for backward compatibility
    def game_over(self):
        self.reset_ball()
