from turtle import Turtle

STARTING_POSITION = (0, -285)
FINISH_LINE_Y = 280
DEFAULT_SPEED = 20
BOOSTED_SPEED = 32

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        
        # State modifiers for power-ups
        self.has_shield = False
        self.is_boosted = False
        self.move_speed = DEFAULT_SPEED
        
        self.update_color()

    def update_color(self):
        """Update turtle color to reflect active power-up states."""
        if self.has_shield and self.is_boosted:
            self.color("cyan")
        elif self.has_shield:
            self.color("#00d2d3")  # Cyan/Blue shield
        elif self.is_boosted:
            self.color("#ff9f43")  # Orange speed boost
        else:
            self.color("#2e8b57")  # Sea green (default)

    def reset_position(self):
        """Send player back to the starting point and clean up modifiers."""
        self.goto(STARTING_POSITION)
        self.has_shield = False
        self.is_boosted = False
        self.move_speed = DEFAULT_SPEED
        self.update_color()

    def go_up(self):
        new_y = self.ycor() + self.move_speed
        if new_y <= FINISH_LINE_Y + 10:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_speed
        if new_y >= -285:
            self.goto(self.xcor(), new_y)

    def go_left(self):
        new_x = self.xcor() - self.move_speed
        if new_x >= -280:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + self.move_speed
        if new_x <= 280:
            self.goto(new_x, self.ycor())

    def activate_shield(self):
        self.has_shield = True
        self.update_color()

    def deactivate_shield(self):
        self.has_shield = False
        self.update_color()

    def activate_boost(self):
        self.is_boosted = True
        self.move_speed = BOOSTED_SPEED
        self.update_color()

    def deactivate_boost(self):
        self.is_boosted = False
        self.move_speed = DEFAULT_SPEED
        self.update_color()
