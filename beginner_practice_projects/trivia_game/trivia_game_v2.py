#!/bin/python3

from pathlib import Path
import time
import csv
import json
import sys
import random


# Allow the user to:
# - Register a new username
# - Log in

# During a match (PHASE #1)
# - Welcome the user and present them with the available options
# - Grab the input | Difficulty level
# - Show questions one by one
# - Grab the input | Answer
# - Show if the answer was actually correct
# > Once all questions have been answered:
# -- Show the final score for that match
# -- Ask the user if they want to play once again

# Post-match functionality (PHASE #2)
# -- Ask the user if they desire to save the progress

welcome = ("Welcome to the NFL trivia game!\n"
           "Choose difficulty:\n"
           "1. Easy [5 questions]\n"
           "2. Medium [10 questions]\n"
           "3. Hard [15 questions]\n"
           "4. Impossible [20 questions]\n")


def retrieve_user_data():
    """Retrieve user scores of previous matches"""
    # Load json file
    with open("user_score.json", "r") as file:
        json_file = json.load(file)
        return json_file
    """
    with open("user_scores", "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['user'].title()}: {row['score']} | {row['difficulty'].title()}")
    """


def start_game(difficulty, questions_number):
    """The actual start of the game: show questions --> capture answers"""
    score = 0

    print(f"You have chosen the \"{difficulty}\" difficulty")
    print(f"You'll be shown {questions_number} questions. 1 point for each correct answer.")
    print("Ready?")
    time.sleep(1.5)
    print("GO!")

    # Store in a regular dictionary the key=value pairs obtained from the csv file (questions_trivia_game.csv)
    questions_dict = {}
    questions = []  # Grab only the keys(questions) from the questions_dict dictionary

    # Open the file
    with open("questions_trivia_game.csv", "r", newline="") as file:
        reader = csv.DictReader(file)  # Read the contents of the csv file
        for row in reader:  # Move the contents of the csv file to the questions_dict dictionary
            key = row["question"]
            value = row["answer"]
            questions_dict[key] = value  # This is the line that does the trick
    
    # Move the keys to the questions list | Important, since it will allow me to use it as the population
    for key in questions_dict.keys():
        questions.append(key)

    # Store the randomly generated questions
    random_questions = random.sample(questions, questions_number)
    for idx, random_question in enumerate(random_questions):
        print(f"{idx + 1}. {random_question}")  # Show the questions to the user
        user_answer = input("").strip().lower()  # Ask the user for an answer
        if user_answer == questions_dict[random_question]:
            print("The answer is correct!")
            score += 1
        else:
            print(f"Incorrect. The answer is: {questions_dict[random_question]}")
    print("The trivia has ended. Let's see how you did...")
    print(f"The number of correct answers is {score}/{questions_number}.")
    if score == questions_number:
        print("Very impressive. Sure you are a heck of an NFL fan")
    elif 7 <= score <= 9:
        print("Pretty good. You deserve an applause")
    elif 5 <= score <= 6:
        print("Mam, you should watch more football")
    else:
        print("Get out of here and go watch some football right now")

    play_again = input("Would you like to play again?").strip().lower()
    if play_again == "y":
        return
    elif play_again == "n":
        print("Exiting game...")
        time.sleep(1)
        sys.exit(0)



def main():
    while True:
        print(welcome) 
        difficulty_selection = input()
        match difficulty_selection:
            case "1":
                start_game(difficulty="easy", questions_number=5)
            case "2":
                start_game(difficulty="medium", questions_number=10)
            case "3":
                start_game(difficutly="hard", questions_number=15)
            case "4":
                start_game(difficulty="impossible", questions_number=20)
            case "q":
                sys.exit(0)
            case _:
                print("Incorrect input. Choose from the menu...")


if __name__ == "__main__":
    main()
    """
    file = retrieve_user_data()
    for key, value in file.items():
        for item in value:
            print(f"User {item['name'].title()}")
            for difficulty in item['score_history']['difficulty']:
                print(f"{item['score_history']['score']} {difficulty}")
            print()
    """
