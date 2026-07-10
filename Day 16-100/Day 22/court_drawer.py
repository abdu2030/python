from turtle import Turtle

def draw_court():
    """Draws the center dashed divider line and mid-circle on the Pong court."""
    drawer = Turtle()
    drawer.hideturtle()
    drawer.speed(0)
    drawer.penup()
    drawer.color("gray")
    drawer.pensize(2)

    # --- Center dashed divider line ---
    drawer.goto(0, 290)
    drawer.setheading(270)  # Face downward
    y = 290
    while y > -290:
        drawer.goto(0, y)
        drawer.pendown()
        drawer.forward(15)
        drawer.penup()
        drawer.forward(15)
        y = drawer.ycor()

    # --- Center circle ---
    drawer.goto(0, -40)       # offset below center so circle is centered at (0,0)
    drawer.setheading(0)
    drawer.color("gray")
    drawer.pendown()
    drawer.circle(40)
    drawer.penup()

    # --- Top and bottom boundary lines ---
    drawer.color("#444444")
    drawer.pensize(3)

    drawer.goto(-400, 290)
    drawer.pendown()
    drawer.goto(400, 290)
    drawer.penup()

    drawer.goto(-400, -290)
    drawer.pendown()
    drawer.goto(400, -290)
    drawer.penup()
