from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    """Manage multiple cars: create randomly and move them across the screen.

    Public methods:
    - create_car(): maybe spawn a new car at the right edge at a random y
    - move_cars(): move all cars to the left by current speed
    - increase_speed(): increase the speed used when moving cars
    """
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Randomly create a new car on the right side.

        Roughly a 1-in-6 chance each call to keep spawn rate reasonable.
        """
        should_create = random.randint(1, 6) == 1
        if should_create:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            # spawn off-screen to the right and at a random y
            random_y = random.randint(-250, 250)
            new_car.goto(320, random_y)
            new_car.setheading(180)  # face left
            self.all_cars.append(new_car)

    def move_cars(self):
        """Move all cars left by the current car_speed."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        """Make cars move faster (call when player levels up)."""
        self.car_speed += MOVE_INCREMENT
