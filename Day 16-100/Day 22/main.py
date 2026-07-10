import time
from turtle import Screen
from paddel import Paddle
from ball import Ball
from scoreboard import Scoreboard
import court_drawer
import sound_manager

# ----------------------------- SCREEN SETUP -------------------------------- #
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong  |  W/S  vs  ↑/↓  |  A=AI  P=Pause")
screen.tracer(0)

# ----------------------------- DRAW COURT ---------------------------------- #
court_drawer.draw_court()
screen.update()

# ----------------------------- GAME OBJECTS -------------------------------- #
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
b_ball   = Ball()
score    = Scoreboard()

# ----------------------------- STATE --------------------------------------- #
keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}
is_paused    = False
game_is_on   = True

# ----------------------------- KEY BINDINGS -------------------------------- #
def key_press(key):
    keys_pressed[key] = True

def key_release(key):
    keys_pressed[key] = False

def toggle_ai():
    """Press A to toggle the left paddle between AI and manual control."""
    l_paddle.is_ai = not l_paddle.is_ai
    # Update window title to reflect AI state
    ai_str = "CPU" if l_paddle.is_ai else "Player 1"
    screen.title(f"Pong  |  {ai_str}  vs  Player 2  |  A=AI  P=Pause")

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        score.draw_paused()
    else:
        # Clear the pause overlay by refreshing the scoreboard
        score.update_scoreboard()

screen.listen()

# Right paddle — Arrow keys
screen.onkeypress(lambda: key_press("Up"),   "Up")
screen.onkeyrelease(lambda: key_release("Up"),   "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")

# Left paddle — W / S keys
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")

# Toggle keys
screen.onkeypress(toggle_ai,    "a")
screen.onkeypress(toggle_ai,    "A")
screen.onkeypress(toggle_pause, "p")
screen.onkeypress(toggle_pause, "P")

# ----------------------------- GAME LOOP ----------------------------------- #
FRAME_SLEEP = 0.05   # Fixed frame rate (~20 fps); speed comes from ball speed

while game_is_on:
    time.sleep(FRAME_SLEEP)
    screen.update()

    if is_paused:
        continue

    # --- Paddle movement ---
    if keys_pressed["Up"]:
        r_paddle.go_up()
    if keys_pressed["Down"]:
        r_paddle.go_down()
    if not l_paddle.is_ai:
        if keys_pressed["w"]:
            l_paddle.go_up()
        if keys_pressed["s"]:
            l_paddle.go_down()
    else:
        l_paddle.ai_track(b_ball)

    # --- Ball movement ---
    b_ball.move()

    # --- Wall bounce (top / bottom) ---
    if b_ball.ycor() > 280 or b_ball.ycor() < -280:
        b_ball.bounce_y()
        sound_manager.play_wall_bounce()

    # --- Paddle collision ---
    r_hit = b_ball.distance(r_paddle) < 50 and b_ball.xcor() > 330
    l_hit = b_ball.distance(l_paddle) < 50 and b_ball.xcor() < -330

    if r_hit or l_hit:
        b_ball.bounce_x()
        sound_manager.play_paddle_hit()

    # --- Ball out of bounds — point scored ---
    elif b_ball.xcor() > 390:
        # Right side missed — left player scores
        b_ball.game_over()
        score.l_point()
        sound_manager.play_score()
        if score.l_wins():
            winner = "CPU" if l_paddle.is_ai else "Player 1"
            score.draw_game_over(winner)
            sound_manager.play_win()
            game_is_on = False

    elif b_ball.xcor() < -390:
        # Left side missed — right player scores
        b_ball.game_over()
        score.r_point()
        sound_manager.play_score()
        if score.r_wins():
            score.draw_game_over("Player 2")
            sound_manager.play_win()
            game_is_on = False

screen.exitonclick()