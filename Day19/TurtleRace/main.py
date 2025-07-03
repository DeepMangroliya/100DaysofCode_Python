import random
from turtle import Turtle,Screen

screen = Screen()
turtles = []
color_list = ["red", "orange", "pink", "blue", "yellow", "cyan"]

screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

pos = -70


for i in range(len(color_list)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color_list[i])
    turtles.append(turtle)
    turtle.goto(x=-230, y=pos)
    pos += 30
    print(turtles)

if user_bet:
    race_is_on = True

    while race_is_on:
            for turtle in turtles:
                print(turtle.pos())
                if turtle.xcor() > 230:
                    race_is_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You have won!, the {winning_color} turtle won the race!")
                    else:
                        print(f"You have lost!, the {winning_color} turtle lost the race!")
                steps = random.randint(0, 10)
                turtle.forward(steps)
screen.exitonclick()