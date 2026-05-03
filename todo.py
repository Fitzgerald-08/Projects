#!/bin/python3

import json
import sys


file_name = "tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}


def create_task(tasks):
    description = input("Enter a description for the task.")
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_tasks(tasks)
        print("Task added successfully")
    else:
        print("Description cannot be empty")


def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("There are no tasks pending")
    else:
        print(f"\nThese are your tasks:")
        for index, task in enumerate(task_list):
            status  = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task["description"]} | {status}")
    print()


def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file)
    except:
        print("Failed to save")


def mark_task_complete(tasks):
    view_tasks(tasks)

    number = int(input("Choose a task to complete: ").strip())
    if 1 <= number <= len(tasks["tasks"]):
        tasks["tasks"][number - 1]["completed"] = True
        save_tasks(tasks)


def main():
    tasks = load_tasks()

    while True:
        print("Welcome to your To-Do!")
        print("1. View tasks")
        print("2. Create tasks")
        print("3. Complete task")
        print("q. Exit")

        action = input("Enter your action: ").strip()

        match action:
            case "1":
                view_tasks(tasks)
            case "2":
                create_task(tasks)
            case "3":
                mark_task_complete(tasks)
            case "q":
                print("Exiting program")
                sys.exit(0)
            case _:
                print("Invalid selection. Choose again from the options")

main()
