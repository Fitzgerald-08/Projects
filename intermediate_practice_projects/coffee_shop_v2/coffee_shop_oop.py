import csv
import sys
import time

from modules import Customer, CoffeeStore


def is_positive(num):
    try:
        num = int(num)
    except ValueError as e:
        print(e)
    else:
        if num >= 1:
            return num
        else:
            return -1


def exit_program(parameter):  # WHENEVER NEEDED, USE THIS FUNCTION TO EXIT THE PROGRAM
    if parameter == 'q':
        sys.exit()


def show_actions():  # Show the user what they can do in this program
    print('\n1. See menu\n'
          '2. Order\n'
          '3. Show subtotal\n'
          '4. Remove coffee\n'
          '5. Proceed to payment\n'
          '6. Log out')


def show_menu(coffee_menu):  # Show the menu
    print('\n======== MENU ========')
    for coffee in coffee_menu:
        print(f'{coffee.coffee_name.title()} - ${coffee.coffee_cost:.2f}')
    print('========================')


# ONCE IN THE PROGRAM, TAKE THE ORDER OF THE CUSTOMER
def take_order(coffee_name, coffee_list):
    for coffee in coffee_list:
        if coffee_name == coffee.coffee_name:
            return coffee  # If the coffee does not exist, return the coffee object
    return None  # Return None if the coffee does not exist


# OBTAIN THE CREDENTIALS OF THE CUSTOMER TO KEEP TRACK OF THEIR ORDERS ACROSS SESSIONS
def customer_login():
    print('=== LOG IN TO CONTINUE ===')
    name = input('Name: ').lower()
    last_name = input('Last Name: ').lower()
    return name, last_name


# FIND, FROM A LIST OF REGISTERED CUSTOMERS, A SPECIFIC CUSTOMER
def find_customer(username, lastname, users_list):
    for user in users_list:
        if user.name == username and user.last_name == lastname:
            return user
    return None


# ================= USER REGISTRATION AND AUTHORIZATION ====================

def register_new_customer(user_info, default_name, default_last_name):
    """Given a pair of customer credentials, authorize or register a new user"""
    if user_info is None:
        create_new_user = input('There\'s no user registered with this name.\n'
                                'Would you like to create one? (y/n): ')
        if create_new_user == 'y':
            print(f'\nUser: {default_name.capitalize()}\n'
                  f'Last name: {default_last_name.capitalize()}')
            default_credentials = input('Would you like to use pre-entered values? ')
            if default_credentials == 'y':
                return default_name, default_last_name
            elif default_credentials == 'n':
                new_name = input('\nEnter a new name: ')
                new_last_name = input('Enter new last_name: ')
                return new_name, new_last_name
        elif create_new_user == 'n':
            return None
    return None


# =========================================================================

def update_order(coffee_name, coffee_quantity, subtotal, logged_customer):
    order = {
        'name': coffee_name,
        'quantity': coffee_quantity,
        'subtotal': subtotal,
    }
    new_subtotal = logged_customer.make_order(order, subtotal)
    print(f'The new subtotal is: ${new_subtotal:.2f}')


def remove_coffee(coffee_name, coffee_menu):
    for entry in coffee_menu:
        if entry.coffee_name == coffee_name:
            return entry
    return None


def save_order_csv(user, order):
    """Save and keep track of the order of a customer across sessions"""
    with open('./orders.csv', 'a', newline='') as csvfile:
        fieldnames = ['user', 'order']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'user': user, 'order': order})

# -----------------------------------------------------------------------------
# THIS AREA STORES THE CUSTOMER AND COFFEE OBJECTS

# This is the list of registered customers along with the respective list
customer1 = Customer(name='cristiano', last_name='royaldo', money=200, user_id='aa11bb22', token=10)
customer2 = Customer(name='trixie', last_name='caranchoa', money=150, user_id='bb22cc33', token=20)
customer3 = Customer(name='coco', last_name='truko', money=250, user_id='cc33dd44', token=30)

registered_customers = [customer1, customer2, customer3]

# These are all the coffees the Coffee Store has to offer and a list at the end
coffee1 = CoffeeStore(coffee_name='moka', coffee_cost=7.50)
coffee2 = CoffeeStore(coffee_name='white moka', coffee_cost=8.00)
coffee3 = CoffeeStore(coffee_name='cappuccino', coffee_cost=7.25)
coffee4 = CoffeeStore(coffee_name='latte', coffee_cost=8.50)
coffee5 = CoffeeStore(coffee_name='americano', coffee_cost=6.00)
coffee6 = CoffeeStore(coffee_name='caramel', coffee_cost=9.00)
coffee7 = CoffeeStore(coffee_name='frappuccino', coffee_cost=7.50)

coffees = [coffee1, coffee2, coffee3, coffee4, coffee5, coffee6]

# This is an empty list that keeps track of all the unregistered customers
unregistered_customers = []


# -----------------------------------------------------------------------------


def main():
    logged_customer = []
    authenticate_user = True
    while True:
        if authenticate_user:
            while True:
                returned_data = customer_login()  # Get the name and last name of the customer
                name = returned_data[0]  # Store the name from the tuple returned above
                last_name = returned_data[1]  # Store the last name
                found_customer = find_customer(username=name, lastname=last_name, users_list=registered_customers)
                if found_customer is not None:
                    print(f'Welcome back {found_customer.name.capitalize()}. Glad to see you again!!')
                    logged_customer.append(found_customer)
                    authenticate_user = False
                    break
                else:
                    register_customer = register_new_customer(user_info=found_customer, default_name=name, default_last_name=last_name)
                    if register_customer is None:
                        continue
                    else:
                        new_customer = Customer(name=register_customer[0], last_name=register_customer[1], money=200, user_id='aabbcc', token=50)
                        registered_customers.append(new_customer)
                        print('Registering new user...')
                        time.sleep(0.75)
        show_actions()
        print('================================')
        decision = input('Select from the menu (q to exit): ')
        exit_program(parameter=decision)

        usr = logged_customer[0]  # Store the user object in a variable
        match decision:
            case '1':
                show_menu(coffees)
            case '2':  # Take the order
                show_menu(coffees)
                # Now, take the order of the customer
                coffee_switch = True
                while coffee_switch:
                    coffee = input('Enter your coffee ([r]eturn/[q]uit): ').lower()
                    if coffee == 'q':
                        sys.exit()
                    elif coffee == 'r':
                        break

                    found_coffee = take_order(coffee_name=coffee, coffee_list=coffees)  # Returns the coffee object
                    if found_coffee is None:
                        print('Could not find anything')
                    else:
                        quantity_switch = True
                        while quantity_switch:
                            input_quantity = input('Quantity ([r]eturn/[q]uit): ').lower()

                            if input_quantity == 'q':
                                sys.exit()
                            elif input_quantity == 'r':
                                break

                            try:
                                quantity = int(input_quantity)
                                if quantity <= 0:
                                    continue
                            except ValueError as e:
                                print(e)
                            else:
                                subtotal = found_coffee.calculate_subtotal(quantity)
                                # Update the information about the order
                                usr.make_order(coffee_name=found_coffee.coffee_name, quantity=quantity, subtotal=subtotal)
                                # usr.show_subtotal()  # Show the order made before
                                print('[+] Order successfully added\n')
                                break
            case '3':  # Show current order
                usr.show_order()
            case '4':  # Remove coffee from the order
                usr.show_order()
                while True:
                    coffee = input('Enter coffee ([r]eturn/[q]uit): ').lower()

                    if coffee == 'q':
                        sys.exit()
                    elif coffee == 'r':
                        break

                    coffee_object = remove_coffee(coffee_name=coffee, coffee_menu=coffees)
                    if not coffee_object is None:
                        remove_quantity = int(input('Quantity: '))
                        operation = usr.remove_order(coffee_object, remove_quantity)
                        if operation == 0:
                            print('[-] Coffees removed successfully from the order')
                        elif operation == -1:
                            print('Negative or 0 values not permitted')
                        elif operation == 1:
                            print('You are trying to enter a value greater than that of your order')
                        elif operation is None:
                            print('The coffee was not found')
                    else:
                        print('Coffee not found...')

                    usr.show_order()
            case '5':  # Give the user an interface for the payment
                usr.show_order()
                print('[INTERFACE TO PROCEED WITH YOUR PAY]')
            case '6':  # Logout and (possibly) save data to a CSV file
                save_order = input('Would you like to save your order for later? ')
                if save_order == 'y':  # 'y' for saving, other than that, continue without saving
                    save_order_csv(user=usr.name, order=usr.order)  # Save the order calling the function in charge
                    print('[!] Saving order...')
                    time.sleep(0.25)

                print('\nLogging out...\n')
                del logged_customer[0]  # Delete the customer from the list of logged customers
                authenticate_user = True  # Reset the flag back to True to bring back the logging page
                time.sleep(0.25)
            case _:
                print('No action corresponds to this value')


if __name__ == "__main__":
    main()