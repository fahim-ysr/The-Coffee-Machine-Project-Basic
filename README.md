------------------------------------------
--> The Coffee Machine Project (Basic) <--
------------------------------------------

    This program simulates the operation of a coffee machine, allowing users to choose from a menu of coffee options, check available resources, insert coins, and receive change.
    
    Features:
    ---------
    - Offers a selection of coffee options: espresso, latte, and cappuccino.
    - Provides a report of available resources (water, milk, coffee).
    - Processes user input for coins (quarters, dimes, nickels, pennies).
    - Checks whether the user has inserted enough coins for the chosen coffee.
    - Updates available resources after each coffee is made.
    - Returns change to the user if necessary.
    
    Functions:
    ----------
    - main(MENU, resources): Operates the coffee machine program.
    - get_water(resources): Reports the amount of water available in the machine.
    - get_milk(resources): Reports the amount of milk available in the machine.
    - get_coffee(resources): Reports the amount of coffee available in the machine.
    - check_resources(resources, choice): Checks whether the machine has sufficient resources to make the chosen coffee.
    - get_quarters(): Asks the user for the number of quarters inserted in the machine.
    - get_dimes(): Asks the user for the number of dimes inserted in the machine.
    - get_nickels(): Asks the user for the number of nickels inserted in the machine.
    - get_pennies(): Asks the user for the number of pennies inserted in the machine.
    - calculate_money(quarters, dimes, nickels, pennies): Calculates user's payment by converting the coins into dollars.
    - check_transaction(choice, MENU, total): Compares the paid amount with the cost of coffee to return the change to the user.
    - update_ingredients(choice, MENU, resources, milk_available, water_available, coffee_available): Updates the ingredients after a coffee has been served.
    
    Dependencies:
    -------------
    - The MENU dictionary contains the available coffee options and their ingredients/cost.
    - The resources dictionary contains the available resources in the coffee machine.
