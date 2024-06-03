from data import menu, resources
profit = 0
flag=0
def is_resource_sufficient(order):
    global flag
    component = menu[order]['ingredients']
    remaining = report()

    for ingredient in component:
        if component[ingredient] > remaining[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            flag=1

    if flag:
        return False
    return True


def report():
    return resources


def print_report():
    print("The machine has: -")
    for resource in resources:
        print(f"{resource} : {resources[resource]}")
    print(f"Money: {profit}")


def process_coins(order):
    total=0
    print("Please insert coins.")

    total = float(input("Enter the quantity of each quarters inserted:")) * 0.25
    total += float(input("Enter the quantity of each dime inserted:")) * 0.10
    total += float(input("Enter the quantity of each nickel inserted:")) * 0.05
    total += float(input("Enter the quantity of each penny inserted:")) * 0.01
    return total

def is_transaction_success(inserted_coins, order):
    cost_of_drink = menu[order]['cost']
    if cost_of_drink <= inserted_coins:
        global profit
        profit += cost_of_drink
        change = round(inserted_coins - cost_of_drink,2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(order):
    component = menu[order]['ingredients']
    remaining = report()

    for ingredient in component:
        resources[ingredient] -= component[ingredient]
    print(f"Here is your {order} ☕. Enjoy!")

is_on = True
while is_on:
    status = input("Enter your choice: 'report' or 'drink'?")

    if status == 'off':
        is_on = False
    elif status == 'report':
        print_report()
    else:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if is_resource_sufficient(order):
            inserted_coins = process_coins(order)
            if is_transaction_success(inserted_coins, order):
                make_coffee(order)



