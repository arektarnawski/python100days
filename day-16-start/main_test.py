# import another_module

# print(another_module.another_variable) 

# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('pink')
# timmy.forward(100)
# print(timmy)

# my_screen = Screen()

# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align = 'l'
print(table)