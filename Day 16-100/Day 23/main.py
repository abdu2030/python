import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()

key_pressed = {"Up" : False}

def key_press(key):
    key_pressed[key] = True

def key_release(key):
    key_pressed[key] = False

screen.listen()
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")


speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    # spawn and move cars each frame
    cars.create_car()
    cars.move_cars()

    if key_pressed["Up"]:
        player.go_up()

    if player.ycor() > 280 :
        player.game_over()
        speed *= 0.9
        # increase difficulty by speeding up cars
        cars.increase_speed()
        score.l_point()
    # check collisions with each car (don't compare player to the manager object)
    for car in cars.all_cars[:]:
        # remove cars that moved off_screen to the left
        if car.xcor() < -320:
            car.hideturtle()
            cars.all_cars.remove(car)
            continue
        # collision detection: if a car is close to the player, reset player
        if car.distance(player) < 37:
            # handle collision - reset player to start
            player.game_over()
            score.goto(0,0)
            score.write("Game Over", align="center", font=("Courier", 26, "bold"))
            game_is_on = False


screen.exitonclick()


