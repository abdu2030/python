from turtle import Turtle
import random

POWER_UP_CONFIGS = {
    "shield": {"shape": "circle", "color": "#00d2d3"},    # Cyan circle
    "snail": {"shape": "square", "color": "#e67e22"},     # Orange square (slow motion)
    "feather": {"shape": "triangle", "color": "#f1c40f"}   # Golden triangle (player speed)
}

class PowerUp(Turtle):
    """Turtle object that represents a collectable power-up on the road."""
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.type = None
        self.active = False
        self.lifetime_ticks = 0

    def spawn(self):
        """Configure and place the power-up at a random location on the road."""
        self.type = random.choice(list(POWER_UP_CONFIGS.keys()))
        config = POWER_UP_CONFIGS[self.type]
        
        self.shape(config["shape"])
        self.color(config["color"])
        self.shapesize(0.9, 0.9)
        
        # Position randomly in road lanes (x: -240 to 240, y: -200 to 200)
        rand_x = random.randint(-240, 240)
        rand_y = random.randint(-200, 200)
        
        self.goto(rand_x, rand_y)
        self.showturtle()
        self.active = True
        self.lifetime_ticks = 100  # Stays visible for 100 ticks (~10 seconds at 0.1s step)

    def collect(self):
        """Triggered when player picks up the power-up."""
        self.deactivate()

    def deactivate(self):
        """Resets the power-up state and hides it."""
        self.hideturtle()
        self.active = False
        self.type = None

    def update_ticks(self):
        """Reduces lifetime of the power-up. Deactivates if expired."""
        if self.active:
            self.lifetime_ticks -= 1
            if self.lifetime_ticks <= 0:
                self.deactivate()
