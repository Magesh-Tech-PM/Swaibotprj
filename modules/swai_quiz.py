# Description: Module for quizzes including movie, general knowledge, math, and capital quizzes.
# Author: [mags]


import random

# Movie Quiz
movie_questions = [
    {"question": "Who directed the movie 'Inception'?", "answer": "Christopher Nolan"},
    {"question": "Which movie features a ring that must be destroyed?", "answer": "The Lord of the Rings"},
    {"question": "What is the highest-grossing movie of all time?", "answer": "Avatar"},
]

# General Knowledge Quiz
general_questions = [
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
]

# Math Quiz
math_questions = [
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is 12 x 11?", "answer": "132"},
]

# Capital Quiz
capital_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the capital of Canada?", "answer": "Ottawa"},
]

# Function to run a quiz
def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    for q in questions:
        user_answer = input(f"Swai: {q['question']} ").strip().lower()
        if user_answer == q["answer"].lower():
            print("Swai: Correct!")
            score += 1
        else:
            print(f"Swai: Incorrect. The correct answer is '{q['answer']}'.")
    return f"Swai: Your final score is {score}/{len(questions)}."
