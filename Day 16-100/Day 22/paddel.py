from turtle import Turtle

PADDLE_MOVE_SPEED = 20
BOUNDARY_Y = 225   # Max Y the paddle center can reach before hitting boundary

class Paddle(Turtle):
    """A Pong paddle that can be controlled by a player or an AI."""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
        self.is_ai = False   # Set True to activate AI control

    def go_up(self):
        """Move paddle up, clamped to the top boundary."""
        new_y = self.ycor() + PADDLE_MOVE_SPEED
        if new_y <= BOUNDARY_Y:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Move paddle down, clamped to the bottom boundary."""
        new_y = self.ycor() - PADDLE_MOVE_SPEED
        if new_y >= -BOUNDARY_Y:
            self.goto(self.xcor(), new_y)

    def ai_track(self, ball):
        """Simple AI: move toward the ball's Y position each tick.

        Uses a capped move speed so the AI is beatable — it can't teleport.
        """
        if not self.is_ai:
            return
        diff = ball.ycor() - self.ycor()
        if diff > 5:
            self.go_up()
        elif diff < -5:
            self.go_down()