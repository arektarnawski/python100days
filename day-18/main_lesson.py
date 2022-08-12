from turtle import Turtle, Screen
import random
tim =  Turtle()
tim.shape("arrow")
screen = Screen()
screen.colormode(255)
tim.speed("fastest")
tim.pensize(2)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# for i in range(3,11):
#     tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360/i)

# for i in range(100):
#      tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#      tim.forward(20)
#      tim.right(90*random.choice([-1,0,1]))

size = 90
for i in range(int(360/size)):
    tim.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    tim.circle(50)
    tim.setheading(tim.heading() + size)

screen.exitonclick()