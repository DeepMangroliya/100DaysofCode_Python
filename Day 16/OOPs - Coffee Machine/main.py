from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True


while is_on:
    status = input("What would you like? report or drink:")

    if status == 'off':
        is_on = False
    elif status == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = input(f"What would you like? latte/espresso/capuccino:")
        drink_item = menu.find_drink(drink)
        print(drink_item.name)
        paid = money_machine.make_payment(drink_item.cost)

        if paid:
            coffee_maker.make_coffee(drink_item)
        else:
            print("You paid less, no drink 😈")
