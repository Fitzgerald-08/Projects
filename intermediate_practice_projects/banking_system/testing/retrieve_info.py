import csv
from pathlib import Path
import shutil


class User:

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show_userinfo(self):
        return f"{self.username.capitalize()} {self.age}"


cwd = Path.cwd()
dst_file_path = Path.joinpath(cwd, 'testing.csv')
place_holder_file = Path.joinpath(cwd, 'place_holder.csv')


def add_entries():
    while True:
        name = input('Enter name: ')
        if name == 'q':
            break
        age = int(input('Enter age: '))
        if age == 0:
            break

        if dst_file_path.exists():
            with open(dst_file_path, 'a', newline='') as file:
                fieldnames = ["name", "age"]
                writer = csv.DictWriter(file, fieldnames)

                writer.writerow({'name': name, 'age': age})
        else:
            with open(dst_file_path, 'x', newline='') as file:
                fieldnames = ["name", "age"]
                writer = csv.DictWriter(file, fieldnames)

                writer.writeheader()
                writer.writerow({'name': name, 'age': age})

    print('\nShowing data saved for the file testing.csv...')



add_entries()

select_user = input('Enter new user: ')

with open(dst_file_path, 'r', newline='') as file, open(place_holder_file, 'w', newline='') as f:
    reader = csv.DictReader(file)

    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    for row in reader:
        if row['name'] != select_user:
            writer.writerow({'name': row['name'], 'age': row['age']})

shutil.copy(place_holder_file, dst_file_path)