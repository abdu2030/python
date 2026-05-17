from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food
screen = Screen()

screen.setup(width=550,height=550)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect collision with the wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        game_is_on = False
        scoreboard.game_over()
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






screen.exitonclick()
