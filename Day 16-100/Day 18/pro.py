# import colorgram
import random
import turtle
from turtle import Turtle

timmy = Turtle()
turtle.colormode(255)

# rgb_colors = []
# colors = colorgram.extract('j.jpg',38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
timmy.hideturtle()
timmy.speed('fastest')
timmy.penup()
color_list = [(234, 232, 227), (230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44), (132, 41, 33), (36, 57, 57), (221, 177, 170), (46, 77, 66)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    timmy.dot(10,random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)





screen = turtle.Screen()
screen.exitonclick()