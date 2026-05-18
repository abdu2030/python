from turtle import Turtle,Screen
from paddel import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360,0))
l_paddle = Paddle((-360,0))
b_ball = Ball()
score = Scoreboard()


# Track which keys are currently pressed
keys_pressed = {"Up": False, "Down": False, "w": False, "s": False}

def key_press(key):
    keys_pressed[key] = True

def key_release(key):
    keys_pressed[key] = False

screen.listen()
screen.onkeypress(lambda: key_press("Up"), "Up")
screen.onkeyrelease(lambda: key_release("Up"), "Up")
screen.onkeypress(lambda: key_press("Down"), "Down")
screen.onkeyrelease(lambda: key_release("Down"), "Down")
screen.onkeypress(lambda: key_press("w"), "w")
screen.onkeyrelease(lambda: key_release("w"), "w")
screen.onkeypress(lambda: key_press("s"), "s")
screen.onkeyrelease(lambda: key_release("s"), "s")

game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(speed)
    # speed decreases to make the game faster
    
    # Check for continuous key presses
    if keys_pressed["Up"]:
        r_paddle.go_up()
    if keys_pressed["Down"]:
        r_paddle.go_down()
    if keys_pressed["w"]:
        l_paddle.go_up()
    if keys_pressed["s"]:
        l_paddle.go_down()
    
    screen.update()
    b_ball.move()

    #detect collision with the wall
    if b_ball.ycor() > 280 or b_ball.ycor() < -280:
        b_ball.bounce_y()
    #detect collision with the paddle
    if b_ball.distance(r_paddle) < 50 and b_ball.xcor() > 330 or b_ball.distance(l_paddle) < 50 and b_ball.xcor() < -330 :
    #b_ball.distance(r_paddle) < 50 this only detect the distance between the ball and the paddle center so if it bounces on the edge it will not detect it,
    #so we add b_ball.xcor() > 340 which make sure that when the ball crosses a certain distance in the screen it bounces
        b_ball.bounce_x()
        speed *= 0.9  # Decrease sleep time by 10% to make game faster
    elif b_ball.xcor() > 385:
        b_ball.game_over()
        score.l_point()
        if score.l_score >= 5:
            score.goto(0, 0)
            score.write("Game Over. L wins", align="center", font=("Courier", 46, "bold"))
            game_is_on = False
        speed = 0.1
    elif b_ball.xcor() < -385:
        b_ball.game_over()
        score.r_point()
        if score.r_score >= 5:
            score.goto(0, 0)
            score.write("Game Over. R wins", align="center", font=("Courier", 46, "bold"))
            game_is_on = False
        speed = 0.1




screen.exitonclick()