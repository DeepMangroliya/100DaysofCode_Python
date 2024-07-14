import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data['state']. tolist()
guessed_states = []

is_game_on = True

while(is_game_on):
    title_string = f"{len(guessed_states)}/50 States Correct"
    answer_state = turtle.textinput(title=title_string, prompt="What's another state name:").title()

    if answer_state == 'Exit':
        break;

    if (answer_state in all_states) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data['x']), int(state_data['y']))
        t.write(state_data['state'].item())

    if len(guessed_states) == len(all_states):
        is_game_on = False

#states_to_learn.csv
unguessed_data = []

for state in all_states:
    if state not in guessed_states:
        unguessed_data.append(state)

states_to_learn = pd.DataFrame(unguessed_data)
pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv")