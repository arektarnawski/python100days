import colorgram
from turtle import Turtle, Screen
import random

rgb_colors = []
colors = colorgram.extract('day-18/hirst_painting/img.jpg', 30)
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    color_tuple = (r,g,b)
    rgb_colors.append(color_tuple)
print(rgb_colors)

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.pensize(10) 

no_of_columns = 10
no_of_rows = 10
screen_size_x = 100
screen_size_y = 100

screen.screensize(screen_size_x,screen_size_y)

# From bottom-left to upper-right drawing
# offset_y = 0
# for i in range(no_of_rows): 
#     offset_x = 0
#     for i in range (no_of_columns): 
#         tim.penup()
#         tim.goto(-screen_size_x+offset_x,-screen_size_y+offset_y)
#         color = random.choice(rgb_colors)
#         tim.dot(10, color)
#         offset_x += 2*screen_size_x/no_of_columns
#     offset_y += 2*screen_size_y/no_of_rows
# tim.hideturtle()
# screen.exitonclick()

# Random drawing - more fun to watch
# Generate coordinates

x_cords = []
for x_cord in range(0,screen_size_x+no_of_columns,no_of_columns):
    x_cords.append(x_cord)
    x_cords.append(-x_cord)

y_cords = []
for y_cord in range(0,screen_size_y+no_of_rows,no_of_rows):
    y_cords.append(y_cord)
    y_cords.append(-y_cord)

gen = ((x, y) for x in x_cords for y in y_cords)

cords = []
for x, y in gen:
    cords.append((x,y))
cords = list(dict.fromkeys(cords))

while len(cords) > 0:
    cord = random.choice(cords)
    x = cord[0]
    y = cord[1]
    cords.remove(cord)

    tim.penup()
    tim.goto(x,y)
    color = random.choice(rgb_colors)
    tim.dot(10, color)

tim.hideturtle()
screen.exitonclick()