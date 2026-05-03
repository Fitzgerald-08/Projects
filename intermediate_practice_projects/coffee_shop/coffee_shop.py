# PLANS FOR THE FUTURE:
#   -- Create a function that allows to, based on input, return one step in whatever part of the program you are
#   -- and also, an option to exit the program prematurely

# !! -- Change this float to a more convenient part of the program, where it can be handled more efficiently
total = float(0)

coffee_menu = [
    {'name': 'moka', 'cost': 7.50},
    {'name': 'white moka', 'cost': 8.00},
    {'name': 'cappuccino', 'cost': 7.25},
    {'name': 'latte', 'cost': 8.50},
    {'name': 'americano', 'cost': 6.00},
    {'name': 'caramel', 'cost': 9.00}
]

# This empty dictionary will be populated with the following structure:
# order = [
#     {'name': value, 'cost': value, 'quantity': value, 'total': value},
order = []

# !! -- Document what every function does
def calculate_total(cost, subtotal_amount, update=False, old_total=None):
    if update:
        new_cost = cost - old_total
        return new_cost + subtotal_amount
    else:
        return cost + subtotal_amount

def print_menu():
    """Simply print the menu on the screen"""
    print(f'\n======== MENU ========')
    for coffee_entry in coffee_menu:
        print(f'- {coffee_entry['name'].capitalize()} ${coffee_entry['cost']}')
    print('======================')

def show_order():
    print(f'\n======== ORDER ========')
    for entry in order:
        print(f'{entry['name'].capitalize()}: x{entry['quantity']}')
    print('\n_______________________')
    print(f'Total: ${total:.2f}')
    print('=======================')

def find_coffee(coffee_name, coffee_list):
    for coffee in coffee_list:
        if coffee['name'] == coffee_name:
            return coffee
    return None

def remove_coffee_func(order_list, coffee_name, quantity):
    list_position = 0

    new_quantity = 0
    new_total = 0
    old_total = 0
    for entry in order_list:
        if entry['name'] == coffee_name:
            if quantity == entry['quantity']:
                del(order_list[list_position])
            else:
                old_total = entry['total']
                new_quantity = entry['quantity'] - quantity
                new_total = new_quantity * entry['cost']
        else:
            list_position = list_position + 1
    return new_quantity, new_total, old_total


print('What would you like to do?')
while True:
    print('1. See menu')
    print('2. Place order')
    print('3. Make your payment')
    print('4. Remove item')
    print('5. Show order')

    decision = input('Enter \'q\' to quit: ').lower()

    if decision == 'q':
        exit()
    try:
        decision = int(decision)
    except ValueError:
        print('[!] Invalid input')

    if decision == 1:
        print_menu()
    elif decision == 2:
        countdown = 0  # This will count the times an error was found
        selection = True  # Control the next while loop's lifetime
        while selection:
            selection = input('Choose your coffee: ([R]eturn/[q]uit): ').lower()
            if selection == 'r':
                break
            if selection == 'q':
                exit()

            # The value returned is a tuple
            coffee_info = find_coffee(coffee_name=selection, coffee_list=coffee_menu)
            # If the coffee is found in the list, show the information related to it
            if coffee_info is not None:
                quantity = True
                while quantity:
                    # [ ] MINI TASK - Fix behavior:
                    # If the user enters a coffee already ordered, just add the new quantity, do not create a new entry
                    quantity = input('Quantity ([R]eturn/[q]uit): ').lower()

                    if quantity == 'r':
                        break
                    if quantity == 'q':
                        print('Exiting program...')
                        exit()

                    try:
                        quantity = int(quantity)
                    except ValueError:
                        print('[!] Invalid input detected. Please, only use numbers...')
                    else:
                        # Get the cost of the coffee, multiply it by the quantity and print the subtotal
                        coffee_cost = coffee_info['cost']
                        sub_total = float(coffee_cost * quantity)
                        print(f'\n[#] Order placed successfully')
                        print(f'Subtotal: ${sub_total:.2f}')

                        # Show the total and a message
                        total = calculate_total(cost=total, subtotal_amount=sub_total)
                        print(f'Total: ${total:.2f}\n')

                        # Create a dictionary with the information of the current order
                        # Append the information to a list
                        coffee_order = {
                            'name': selection,
                            'cost': coffee_cost,
                            'quantity': quantity,
                            'total': sub_total,
                        }
                        order.append(coffee_order)

                        # This, and the next line control the core flow of the program
                        quantity = False  # This line exits the "quantity" loop
                        selection = False  # And this one exits the main loop, "selection", back to the menu
                        # Both completely return to the main menu, OTHERWISE, I can return between menus
            else:
                print('\n[*] Coffee not found')
                countdown = countdown + 1
                counter = 3

                if countdown == 3:
                    display_menu = True
                    while display_menu:
                        display_menu = input('Would you like to see the menu? ').lower()
                        if display_menu == 'y' or display_menu == 'yes':
                            print_menu()
                            countdown = 0
                            display_menu = False
                        if display_menu == 'n' or display_menu == 'no':
                            countdown = 0
                            display_menu = False
    elif decision == 3:
        print('Proceeding to make your payment')
        exit()
    elif decision == 'q':
        print('Exiting...')
        exit()
    elif decision == 4:
        # [ ] SECOND TASK - Make this part finally work
        # Delete a whole entry or just a given quantity of coffees
        if len(order) == 0:
            print('=== You have to order something first ===')
        else:
            show_order()
            remove_coffee = True
            while remove_coffee:
                remove_coffee = input('Enter coffee name: ').lower()
                remove_coffee_name = find_coffee(coffee_name=remove_coffee, coffee_list=order)
                if remove_coffee_name is not None:
                    while True:
                        remove_quantity = input('How many?: ')

                        try:
                            remove_quantity = int(remove_quantity)
                        except ValueError:
                            print('\n[!] Only numbers are permitted\n')

                        if remove_quantity > remove_coffee_name['quantity']:
                            print('\n[!] Value greater than ordered\n')
                        elif 0 < remove_quantity <= remove_coffee_name['quantity'] :
                            # Returns: 'new_quantity', 'new_total', 'old_total'
                            new_data = remove_coffee_func(order_list=order, coffee_name=remove_coffee, quantity=remove_quantity)
                            total =  calculate_total(cost=total, subtotal_amount=new_data[1], update=True, old_total=new_data[2])
                            new_quantity = new_data[0]
                            for entry in order:
                                if entry['name'] == remove_coffee:
                                    entry['quantity'] = new_quantity
                            print('[#] YOUR ORDER HAS BEEN UPDATED')
                            show_order()
                            remove_coffee = False
                            break
                        else:
                            print('[!] Only positive values accepted.')
                else:
                    print('Coffee is not in the list')
    elif decision == 5:  # Very straightforward options
        if len(order) == 0:
            print('=== You have to order something first ===')
        else:
            show_order()
    else:
        print('Invalid selection...')
