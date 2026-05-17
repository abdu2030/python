from turtle import Turtle,Screen



tim = Turtle()
screen = Screen()

def move_forwards():
   tim.forward(20)
def move_back():
    tim.backward(20)
def right():
    tim.right(20)
def left():
    tim.left(20)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_back, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(clear, "c")



screen.exitonclick()


