#!/bin/env python3

import random
import string


# How to make this little program better:
# - Include hashing and salting techniques to provide a more of a real-life scenario


def generate_password():
    length = int(input("Enter the lenght of the password: "))
    include_uppercase = input("Include uppercase characters? [y/n]: ").lower().strip()
    include_special = input("Include special characters? [y/n]: ").lower().strip()
    include_digits = input("Include digits? [y/n]: ").lower().strip()

    if length < 8:
        print("The password has to be at least 8 characters long")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""

    selected_characters = lower + uppercase + special + digits

    password = []
    if include_uppercase == "y":
        password.append(random.choice(uppercase))
    if include_special == "y":
        password.append(random.choice(special))
    if include_digits == "y":
        password.append(random.choice(digits))

    remaining_password_length = length - len(password)
    for _ in range(remaining_password_length):
        password.append(random.choice(selected_characters))

    str_password = "".join(password)
    print(str_password)


if __name__ == "__main__":
    generate_password()
