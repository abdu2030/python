import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()
guessed_states = []
missing_states = []

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn")
        turtle.bye()
        break

    answer_state = answer_state.title()

    if answer_state in all_state and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_row = data[data["state"] == answer_state]

        x = state_row["x"].iloc[0].to
        y = state_row["y"].iloc[0]

        writer.goto(x, y)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.mainloop()