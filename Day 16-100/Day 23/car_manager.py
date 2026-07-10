from turtle import Turtle
import random

COLORS = ["#e74c3c", "#e67e22", "#f1c40f", "#2ecc71", "#3498db", "#9b59b6"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager:
    """Manages multiple car turtles on the screen, including speed scaling and modifiers."""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.is_slowed = False

    def create_car(self):
        """Randomly spawns a new car at the right side of the screen."""
        should_create = random.randint(1, 6) == 1
        if should_create:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2.5, stretch_wid=1.1)
            
            # Spawn in one of the key road lanes
            # Lanes are bounded from y=-200 to y=200
            random_y = random.randint(-220, 220)
            new_car.goto(320, random_y)
            new_car.setheading(180)  # Face left
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars leftwards. Applies 65% speed reduction if slowed."""
        speed = self.car_speed * 0.35 if self.is_slowed else self.car_speed
        for car in self.all_cars:
            car.forward(speed)

    def increase_speed(self):
        """Increase general base speed of cars (on level up)."""
        self.car_speed += MOVE_INCREMENT

    def reset_manager(self):
        """Resets cars speed to default and turns off slow-motion."""
        self.car_speed = STARTING_MOVE_DISTANCE
        self.is_slowed = False
        self.clear_all_cars()

    def clear_all_cars(self):
        """Hides and deletes all car objects from memory and screen."""
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
