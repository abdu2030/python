import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import road_drawer
import sound_manager
from powerup import PowerUp

# 1. Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Antigravity Turtle Crossing")
screen.tracer(0)

# 2. Draw Road Visual Layout
road_drawer.draw_road()
screen.update()

# 3. Game Objects Setup
player = Player()
score = Scoreboard()
cars = CarManager()
powerup = PowerUp()

# 4. Keyboard Controls (Responsive Press/Release dictionary)
key_pressed = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}
key_last_state = {
    "Up": False,
    "Down": False,
    "Left": False,
    "Right": False
}

def key_press(direction):
    key_pressed[direction] = True

def key_release(direction):
    key_pressed[direction] = False

# Bind arrow keys and WASD
screen.listen()
directions = ["Up", "Down", "Left", "Right"]
wasd_map = {"w": "Up", "s": "Down", "a": "Left", "d": "Right"}

for d in directions:
    screen.onkeypress(lambda dir_val=d: key_press(dir_val), d)
    screen.onkeyrelease(lambda dir_val=d: key_release(dir_val), d)

for key, d in wasd_map.items():
    screen.onkeypress(lambda dir_val=d: key_press(dir_val), key)
    screen.onkeyrelease(lambda dir_val=d: key_release(dir_val), key)
    screen.onkeypress(lambda dir_val=d: key_press(dir_val), key.upper())
    screen.onkeyrelease(lambda dir_val=d: key_release(dir_val), key.upper())

# 5. Core Game Loop
speed = 0.1
game_is_on = True

# Power-up active timers
snail_timer = 0
boost_timer = 0

while game_is_on:
    time.sleep(speed)
    screen.update()

    # --- A. Power-Up Timers Tick Down ---
    if snail_timer > 0:
        snail_timer -= 1
        if snail_timer == 0:
            cars.is_slowed = False

    if boost_timer > 0:
        boost_timer -= 1
        if boost_timer == 0:
            player.deactivate_boost()

    # --- B. Power-Up Spawn & Collection ---
    if not powerup.active:
        # ~1-in-150 chance per frame to spawn a power-up (approx. 15 seconds)
        if random.randint(1, 150) == 1:
            powerup.spawn()
    else:
        powerup.update_ticks()
        
        # Check collision with power-up item
        if player.distance(powerup) < 22:
            sound_manager.play_powerup()
            effect = powerup.type
            
            if effect == "shield":
                player.activate_shield()
            elif effect == "snail":
                cars.is_slowed = True
                snail_timer = 80  # ~8 seconds
            elif effect == "feather":
                player.activate_boost()
                boost_timer = 80  # ~8 seconds
                
            powerup.collect()

    # --- C. Spawning and Moving Cars ---
    cars.create_car()
    cars.move_cars()

    # --- D. Player Movement and Move Sound ---
    new_press = False
    for d in directions:
        if key_pressed[d] and not key_last_state[d]:
            new_press = True
        key_last_state[d] = key_pressed[d]

    if key_pressed["Up"]:
        player.go_up()
    if key_pressed["Down"]:
        player.go_down()
    if key_pressed["Left"]:
        player.go_left()
    if key_pressed["Right"]:
        player.go_right()

    if new_press:
        sound_manager.play_move()

    # --- E. Check Finish Line (Level Up) ---
    if player.ycor() >= 250:  # Crossed the top sidewalk boundary
        sound_manager.play_level_up()
        score.l_point()
        cars.increase_speed()
        
        # Clean reset for new level
        player.reset_position()
        cars.clear_all_cars()
        powerup.deactivate()
        snail_timer = 0
        boost_timer = 0

    # --- F. Check Collisions with Cars ---
    for car in cars.all_cars[:]:
        # Despawn cars off-screen left
        if car.xcor() < -320:
            car.hideturtle()
            cars.all_cars.remove(car)
            continue

        # Bounding-box collision checks (fair rectangular overlapping)
        x_overlap = abs(player.xcor() - car.xcor()) < 35
        y_overlap = abs(player.ycor() - car.ycor()) < 20

        if x_overlap and y_overlap:
            if player.has_shield:
                # Shield absorbs crash, destroys car, deactivates
                player.deactivate_shield()
                car.hideturtle()
                cars.all_cars.remove(car)
                sound_manager.play_crash()
            else:
                # Fatal crash
                sound_manager.play_crash()
                still_alive = score.lose_life()
                
                # Reset lane state
                player.reset_position()
                cars.clear_all_cars()
                powerup.deactivate()
                snail_timer = 0
                boost_timer = 0
                
                if not still_alive:
                    score.draw_game_over()
                    game_is_on = False
                    break

screen.exitonclick()
