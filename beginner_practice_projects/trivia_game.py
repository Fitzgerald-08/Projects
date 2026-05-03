#!/bin/env python3


# NEW GOALS
# Ask the user to enter a difficulty level
# Allow the user to decided if they want 5, 10 or 15 questions

# 1. Show the answers
# 2. Capture user input
# 3. Check if the answer is correct and keep track of the score
# 4. Display the final score

import random


questions = {
    "When was the last time the Buffalo Bills went to a Super Bowl?": "1984",
    "Which was the last team Tom Brady played for?": "tampa bay",
    "How many teams are there in the NFL?": "32",
    "As of 2026, Who is the HC for the New York Giants?": "john harbough",
    "How many Super Bowl rings does Tom Brady earned in his career?": "7",
    "In what round was Tom Brady drafted?": "6",
    "Which teams belong to the AFC East division?": "buffalo",
}

def trivia_game():
    question_number = 5
    score = 0

    questions_list = list(questions.keys())
    random_questions = random.sample(questions_list, question_number)

    for index, question in enumerate(random_questions):
        print(f"{index + 1}. {question}")
        answer = input("Answer: ").lower().strip()

        correct_answer = questions[question]
        if correct_answer == answer:
            print("The answer is correct")
            score += 1

    print(f"The final score is: {score}")


trivia_game()


# FINAL NOTES ON WHAT HAS BEEN LEARNED
# 1. The use of the enumerate() function
# 2. The different ways in which a dictionary can be used
# 3. (Again) how to use the keys and values in a dictionary to get a concrete result
