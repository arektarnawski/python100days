from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Greet the user & get user's drink choice

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

finish = False

while finish == False:
    order_prompt = input(f"What would you like: {menu.get_items()}?  ")
    order_product = menu.find_drink(order_prompt)

    if order_prompt == 'off':
        print('Turning off')
        finish = True
    elif order_prompt == 'report':
        coffe_maker.report()
        money_machine.report()
        finish = False # Take next prompt
    elif menu.find_drink(order_prompt):
        if coffe_maker.is_resource_sufficient(order_product):
            if money_machine.make_payment(order_product.cost):
                coffe_maker.make_coffee(order_product)
                finish = False # Serve next customer
            else:
                print('Try again.')
                finish = True
        else:
            print('Resources not sufficient, try again.')
            finish = True
    else:
        print('Wrong product name entered, try again.')
        finish = True