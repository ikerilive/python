import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)

# Read the CSV file
data = pandas.read_csv('50_states.csv')
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # Get user input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50: Guess the States", prompt="What is another state's name?").title()

    # Check if the answer is correct
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] # Get the state data
        t.goto(state_data.x.item(), state_data.y.item()) # Move to the coordinates and write the state name
        t.write(answer_state, align="center")


