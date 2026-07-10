from turtle import Turtle

def draw_road():
    """Draws sidewalks, lane divider lines, and road pavements on the turtle screen."""
    drawer = Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()

    # 1. Draw green sidewalks at bottom (-300 to -250) and top (250 to 300)
    # Bottom sidewalk
    drawer.goto(-300, -300)
    drawer.color("#27ae60")  # Nice emerald green
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(600)
        drawer.left(90)
        drawer.forward(50)
        drawer.left(90)
    drawer.end_fill()

    # Top sidewalk
    drawer.goto(-300, 250)
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(600)
        drawer.left(90)
        drawer.forward(50)
        drawer.left(90)
    drawer.end_fill()

    # 2. Draw dark road pavement in between (-250 to 250)
    drawer.goto(-300, -250)
    drawer.color("#2c3e50")  # Sleek dark gray
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(600)
        drawer.left(90)
        drawer.forward(500)
        drawer.left(90)
    drawer.end_fill()

    # 3. Draw solid white boundaries for sidewalks
    drawer.color("white")
    drawer.pensize(3)
    
    # Bottom border line
    drawer.goto(-300, -250)
    drawer.pendown()
    drawer.goto(300, -250)
    drawer.penup()
    
    # Top border line
    drawer.goto(-300, 250)
    drawer.pendown()
    drawer.goto(300, 250)
    drawer.penup()

    # 4. Draw dashed yellow lane markings (4 divisions)
    drawer.color("#f1c40f")  # Golden yellow
    drawer.pensize(2)
    
    lane_ys = [-150, -50, 50, 150]
    for y in lane_ys:
        drawer.goto(-300, y)
        while drawer.xcor() < 300:
            drawer.pendown()
            drawer.forward(20)
            drawer.penup()
            drawer.forward(20)
