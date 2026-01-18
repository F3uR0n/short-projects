import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make Your Bet!!", "Guess which turtle will win the race, Pick the color")
color = ["red", "green", "blue", "purple", "yellow", "orange"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for _ in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[_])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner")

screen.exitonclick()
