from pathlib import Path
import csv


def read_data():
    with open('accounting.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['first_name']} {row['last_name']}")


class BankUser:
    """Define very basic information about the user from a bank"""

    def __init__(self, first_name, last_name, money):
        """Only very basi attributes of the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.money = money
    
    def add_money(self, addition):
        """Add money to the bank account of the user"""
        self.money = self.money + addition
        return self.money

    def write_new_data(self):
        """Write to a CSV file the updated information about the user and the new money"""
        with open('accounting.csv', 'w', newline='') as file:
            fieldnames = ["first_name", "last_name", "money"]
            writer = csv.DictWriter(file, fieldnames)

            writer.writeheader()
            writer.writerow({"first_name": self.first_name, "last_name": self.last_name, "money": self.money})


def show_menu():
    print('Welcome. What kind of activity would you like to perform?')
    print('r. Register')
    print('1. Add money')
    print('2. Grab some money')
    print('3. Check money')


user1 = BankUser(first_name='Cristiano', last_name='Royaldo', money=1000.00)

users_list = [user1]


def get_new_user():
    new_name = input('Enter name: ')
    new_last_name = input('Enter last name: ')

    return new_name, new_last_name


def find_user(users, user_name, last_name):
    for user in users:
        if user.first_name == user_name and user.last_name == last_name:
            return user
    
    return None


def authenticate(users):
    user_name = input("First name: ")
    last_name = input("Last name: ")
    
    return find_user(users, user_name, last_name)


def add_money(user, quantity):
    old_quantity = user.money
    new_quantity = user.add_money(quantity)
    if new_quantity > old_quantity:
        print("[+] Money successfully updated")


def get_money(user_info):
    add_new_quantity = input("Introduce quantity: ")
    try:
        add_new_quantity = int(add_new_quantity)
    except ValueError as e:
        print(e)
    else:
        add_money(user=user_info, quantity=add_new_quantity)
        user_info.write_new_data()


if __name__ == "__main__":
    show_menu()
    decision = ""
    while decision != 'q':
        decision = input()
        try:
            match decision:
                case 'r':
                    new_credentials = get_new_user()
                case '1':
                    user = ""
                    while user != 'q':
                        user = authenticate(users=users_list)
                        if user == 'q':
                            break
                        elif user is None:
                            print("No user was found with these credentials")
                        else:
                            get_money(user_info=user)

                case '2':
                    pass
                case '3':
                    pass
                case _:
                    print("Invalid selection. Choose one from the menu")
        except ValueError:
            print('[!] Invalid input. Try again')