from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Red, Green, Blue, Purple, Orange. Make your bet.").lower()
colors = ["red", "green", "blue", "purple", "orange"]
init_position = [-160, 160, -80, 80, 0]
turtles = []

for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x= -285, y= init_position[i])
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in turtles:
        if i.xcor() > 280:
            winning_color = i.pencolor()
            if winning_color == user_bet:
                print("Youve Won!")
            else:
                print("You Lose")
            is_race_on = False

        r_dist = random.randint(0, 10)
        i.forward(r_dist)
        

screen.exitonclick()