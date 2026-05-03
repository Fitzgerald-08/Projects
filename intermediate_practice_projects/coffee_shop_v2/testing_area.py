from pathlib import Path
import os
import csv


import sys


def condition():
    while True:
        try:
            value = int(input('Enter one number: '))
        except ValueError as e:
            print(e)
        else:
            print(f'The value entered was {value}')


def pos_num(num):
    try:
        num = int(num)
    except ValueError as e:
        print(e)
    else:
        if num >= 1:
            print('The number is positive')
        else:
            print('It\'s a negative value')


def find_delete_item():
    dict = [
        {'name': 'roy', 'age': 18},
        {'name': 'trixie', 'age': 20},
        {'name': 'coco', 'age': 16},
    ]

    for di in dict:
        i = 0
        if di['name'] == 'roy':
            del dict[i]
        else:
            i = i + 1

    print(dict)


def find_element():
    """Move all the elements from a dictionary and use it to find a given element"""
    while True:
        dict = [
            {'name': 'roy', 'age': 18},
            {'name': 'trixie', 'age': 20},
            {'name': 'coco', 'age': 16},
        ]
        empty_list = []

        enter = input('Enter element: ')
        if enter == 'q':
            sys.exit()

        for di in dict:
            empty_list.append(di['name'])

        if enter in empty_list:
            print(f'{enter} has been found in the list')
        else:
            print('An error has occurred')

"""
while True:
    enter_user = input('Enter your username: ')
    desktop = './orders.csv'
    with open(desktop, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['user'] == enter_user:
                print(f'The user {row['user'].capitalize()} has the order number {row['order_number']}')
"""

path = './orders.csv'
with open(path, 'a', newline='') as csvfile:
    fieldnames = ['user', 'order', 'subtotal', 'order_number']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'user': 'cristiano', 'order': 'french fries', 'subtotal': 20, 'order_number': 1})
    writer.writerow({'user': 'coco', 'order': 'kk', 'subtotal': 0, 'order_number': 2})