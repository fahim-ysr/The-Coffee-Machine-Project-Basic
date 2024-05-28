MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Informs user about the menu
print("Items Available:")
for key in MENU:
    print(key + ": $" + str(MENU[key]["cost"]))
print("\n")

# TODO: 1. Prompt for user's input

def main(MENU, resources):
    '''Operates the coffee machine program.'''
    running = True
    money = 0

    while running:
        milk_available = get_milk(resources)
        coffee_available = get_coffee(resources)
        water_available = get_water(resources)

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
        if choice == "off":
            print("Shutting down...")
            running = False

        # TODO: 3. Print report
        elif choice == "report":
            print("Water: " + str(water_available) + "ml")
            print("Milk: " + str(milk_available) + "ml")
            print("Coffee: " + str(coffee_available) + "ml")
            print("Money: $" + str(money))

        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            sufficient = check_resources(resources, choice)

            if sufficient == True:
                print("Please insert coins.")
                quarters = get_quarters()
                dimes = get_dimes()
                nickles = get_nickles()
                pennies = get_pennies()
                paid = calculate_money(quarters, dimes, nickles, pennies)
                check_transaction(choice, MENU, paid)
                money = money + MENU[choice]["cost"]
                update_ingredients(choice, MENU, resources, milk_available, water_available, coffee_available)
                print("Here is your " + choice + "☕️. Enjoy!")

        else:
            print("Input Error.")
            running = False




# Reports the water available in the machine
def get_water(resources):
    '''Returns the amount of water available in the machine.'''
    water_available = resources["water"]
    return water_available


# Reports the milk available in the machine
def get_milk(resources):
    '''Returns the amount of milk available in the machine.'''
    milk_available = resources["milk"]
    return milk_available


# Reports the coffee available in the machine
def get_coffee(resources):
    '''Returns the amount of coffee available in the machine.'''
    coffee_available = resources["coffee"]
    return coffee_available


# TODO: 4. Check resources sufficient?
def check_resources(resources, choice):
    '''Checks whether the coffee machine has sufficient resources to make a coffee.'''
    water_required = MENU[choice]["ingredients"]["water"]
    water_available = get_water(resources)
    coffee_required = MENU[choice]["ingredients"]["coffee"]
    coffee_available = get_coffee(resources)
    milk_required = MENU[choice]["ingredients"]["milk"]
    milk_available = get_milk(resources)

    if water_required > water_available:
        print("Sorry there is not enough water.")
        return False
    elif coffee_required > coffee_available:
        print("Sorry there is not enough coffee.")
        return False
    elif milk_required > milk_available:
        print("Sorry there is not enough milk")
        return False
    else:
        return True



# TODO: 5. Process coins

def get_quarters():
    '''Asks the user for the number of quarters inserted in the machine.'''
    # quarter = $0.25
    quarters = int(input("how many quarters?: "))
    return quarters


def get_dimes():
    '''Asks the user for the number of dimes inserted in the machine.'''
    # dimes = $0.10
    dimes = int(input("how many dimes?: "))
    return dimes


def get_nickles():
    '''Asks the user for the number of nickles inserted in the machine.'''
    # nickles = $0.05
    nickles = int(input("how many nickles?: "))
    return nickles


def get_pennies():
    '''Asks the user for the number of pennies inserted in the machine.'''
    # pennies = $0.01
    pennies = int(input("how many pennies?: "))
    return pennies


def calculate_money(quarters, dimes, nickles, pennies):
    '''Calculates user's payment by converting the coins into dollar.'''
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


# TODO: 6. Check transaction successful?
def check_transaction(choice, MENU, total):
    '''Compares the paid amount with the cost of coffee to return the change to the user.'''
    cost = MENU[choice]["cost"]
    paid = total
    change = paid - cost

    if cost > paid:
        print("Sorry that's not enough money. Money refunded.")

    else:
        print("Here is $" + str(change) + " in change.")



# TODO: 7. Make Coffee (update ingredients)...
def update_ingredients(choice, MENU, resources, milk_available, water_available, coffee_available):
    '''Updates the ingredients after a coffee has been served.'''
    updated_milk = milk_available - MENU[choice]["ingredients"]["milk"]
    updated_water = water_available - MENU[choice]["ingredients"]["water"]
    updated_coffee = coffee_available - MENU[choice]["ingredients"]["coffee"]
    resources["water"] = updated_water
    resources["milk"] = updated_milk
    resources["coffee"] = updated_coffee



# TODO: 8. Call main()
main(MENU, resources)