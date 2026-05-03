class CoffeeStore:
    """Build the attributes for coffee and methods that users can perform"""

    def __init__(self, coffee_name, coffee_cost):
        self.coffee_name = coffee_name
        self.coffee_cost = coffee_cost

    def calculate_subtotal(self, quantity):
        """Add new items to a specific order of coffee and update the subtotal"""
        return quantity * self.coffee_cost

    def price_off(self):
        """If the coffee has a price off, display the new price"""
        pass


class Customer:
    """The user that defines very basic attributes for interacting with the coffee app"""

    def __init__(self, name, last_name, money, user_id, token):
        self.name = name
        self.last_name = last_name
        self.money = money
        self.user_id = user_id
        self.token = token
        self.order = []

    def change_token(self, new_token):
        pass

    def make_order(self, coffee_name, quantity, subtotal):
        """Take/Update the order of the customer"""
        ordered_coffees = []
        for entry in self.order:
            ordered_coffees.append(entry['coffee'])

        if coffee_name in ordered_coffees:
            print('The coffee has already been ordered')
            for coffee in self.order:
                if coffee['coffee'] == coffee_name:
                    coffee['quantity'] = coffee['quantity'] + quantity
                    coffee['subtotal'] = coffee['subtotal'] + subtotal
        else:
            incoming_order = {
                'coffee': coffee_name,
                'quantity': quantity,
                'subtotal': subtotal,
            }
            self.order.append(incoming_order)

    def show_subtotal(self):
        """Display the orders stored in the self.order attribute"""
        for entry in self.order:
            print(entry)

    def show_order(self):
        """Show the current order of the user with all the coffees, its subtotal and a total"""
        total = 0
        if len(self.order) == 0:
            print('\n== You haven\'t ordered anything yet ==')
        else:
            print('\n========= YOUR ORDER =========')
            for entry in self.order:
                print(f'Coffee: {entry['coffee'].title()}: x{entry['quantity']} - {entry['subtotal']:.2f}')
                total = total + entry['subtotal']
            print('==============================')
            print(f'Total = ${total:.2f}')

    def remove_order(self, coffee, remove_quantity):  # Receive the coffee object
        """Depending on the order, delete part of the order, one whole entry, or the whole order"""
        counter = 0
        for entry in self.order:
            if entry['coffee'] == coffee.coffee_name:
                if remove_quantity > entry['quantity']:
                    return 1
                elif 0 < remove_quantity < entry['quantity']:
                    entry['quantity'] = entry['quantity'] - remove_quantity
                    entry['subtotal'] = entry['quantity'] * coffee.coffee_cost
                    return 0
                elif remove_quantity < 0:
                    return -1
                else:
                    del self.order[counter]
                    return 0
            else:
                counter += 1
        return None