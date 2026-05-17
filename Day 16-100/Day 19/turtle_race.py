import random
from turtle import Turtle,Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make a guess", prompt="which turtle win the race? enter a color: ")
colors = ['red','orange','yellow','green', 'blue', 'purple']
ya = -100
all_turtle = []
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=ya)
    ya += 40
    all_turtle.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on  = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won!!! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost!!! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)








screen.exitonclick()
