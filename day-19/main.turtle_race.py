from turtle import Turtle, Screen, penup
import random

screen = Screen()
race_on = False

player_turtles = []
player_turtle_colors = ['red','green','blue','yellow','pink']
starting_positions = [-100,-50,0, 50, 100,]

for turtle_index in range(len(player_turtle_colors)):
    turtle = Turtle( shape='turtle')
    turtle.color(player_turtle_colors[turtle_index])
    turtle.penup()
    turtle.goto(-400,starting_positions[turtle_index])
    turtle.speed("fast")
    player_turtles.append(turtle)

refree = Turtle(shape="turtle")
refree.color("black")
refree.speed("fast")
refree.penup()
refree.goto(150,150)
refree.right(90)
refree.pendown()
refree.forward(300)
refree.left(180)
refree.penup()

predicted_winner = screen.textinput("Choose a winner","Who will win the race?: ")
if predicted_winner:
    race_on = True

while race_on:
    for turtle in player_turtles:
        if race_on == True:
            move = random.choice(range(11))
            turtle.forward(move)
            if turtle.xcor() >= 150:
                race_on = False
                refree.goto(-300,300)
                refree.write(f"Winner: {turtle.color()[0]}",font=('Arial', 30, 'normal'))
                refree.goto(-300,270)
                if predicted_winner == turtle.color():
                    refree.write(f"You guessed {predicted_winner}, well done!",font=('Arial', 30, 'normal'))
                else:
                    refree.write(f"You guessed {predicted_winner}, better luck next time!",font=('Arial', 30, 'normal'))
                refree.hideturtle()

screen.exitonclick()