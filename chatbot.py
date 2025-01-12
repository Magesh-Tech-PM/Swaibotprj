# Description: Main chatbot script to run SwaiBot, providing a menu-driven interface.
# Author:Mags

from modules import (
    play_rock_paper_scissors,
    play_number_guess,
    play_word_scramble,
    run_quiz,
    movie_questions,
    general_questions,
    math_questions,
    capital_questions,
    solve_math_problem,
    multiplayer_number_guess,
    tell_joke
)
from random import choice

def greet_user():
    print("Hi there! I’m Swai, your friendly chatbot. Let’s have some fun!")

def show_main_menu():
    print("""
Main Menu:
1. Feelings
2. Fun and Games
3. Quizzes
4. Utilities
5. Quit
    """)

def repeat_prompt(function, *args):
    """Repeats a game or quiz based on user input."""
    while True:
        function(*args)
        repeat = input("Swai: Would you like to try again? (yes/no): ").strip().lower()
        if repeat == "no":
            print("Swai: Returning to the main menu...")
            break
        elif repeat != "yes":
            print("Swai: Invalid input. Please type 'yes' or 'no'.")

def handle_feelings():
    user_input = input("Swai: Are you feeling 'happy' or 'sad'? ").lower()
    bot_response_happy = [
        "That's so good to hear!",
        "That makes ME happy to hear!",
        "There is nothing more than that, makes me happier!"
    ]
    bot_response_sad = [
        "Don't worry. You're not alone!",
        "I wish there was something I could do to help you feel better!",
        "Well, I'm sorry, but hey, I'm sending you only the best of vibes!"
    ]
    if user_input == "happy":
        print(f"Swai: {choice(bot_response_happy)}")
    elif user_input == "sad":
        print(f"Swai: {choice(bot_response_sad)}")
    else:
        print("Swai: Hmm, I didn’t understand that. Try 'happy' or 'sad'.")

def handle_fun_and_games():
    while True:
        print("""
Fun and Games:
1. Tell a Joke
2. Play Rock-Paper-Scissors
3. Play Word Scramble
4. Back to Main Menu
        """)
        user_input = input("Choose an option: ").lower()
        if user_input == "1":
            repeat_prompt(tell_joke)
        elif user_input == "2":
            repeat_prompt(play_rock_paper_scissors)
        elif user_input == "3":
            repeat_prompt(play_word_scramble)
        elif user_input == "4":
            break
        else:
            print("Swai: Invalid option. Try again.")

def handle_quizzes():
    while True:
        print("""
Quizzes:
1. Movie Quiz
2. General Knowledge Quiz
3. Math Quiz
4. Capital Quiz
5. Back to Main Menu
        """)
        user_input = input("Choose a quiz category: ").lower()
        if user_input == "1":
            repeat_prompt(run_quiz, movie_questions)
        elif user_input == "2":
            repeat_prompt(run_quiz, general_questions)
        elif user_input == "3":
            repeat_prompt(run_quiz, math_questions)
        elif user_input == "4":
            repeat_prompt(run_quiz, capital_questions)
        elif user_input == "5":
            break
        else:
            print("Swai: Invalid option. Try again.")

def handle_utilities():
    while True:
        print("""
    Utilities:
    1. Solve a Math Problem
    2. Ask a Predefined Question (Q&A)
    3. Multiplayer Number Guessing Game
    4. Birthday Reminder
    5. Back to Main Menu
            """)
        user_input = input("Choose an option: ").lower()
        if user_input == "1":
            repeat_prompt(solve_math_problem)
        elif user_input == "2":
            repeat_prompt(answer_question)
        elif user_input == "3":
            repeat_prompt(multiplayer_number_guess)
        elif user_input == "4":
            handle_birthday_reminder()
        elif user_input == "5":
            break
        else:
            print("Swai: Invalid option. Try again.")

def start_chatbot():
    greet_user()
    while True:
        show_main_menu()
        user_input = input("Choose an option: ").lower()
        if user_input == "1":
            handle_feelings()
        elif user_input == "2":
            handle_fun_and_games()
        elif user_input == "3":
            handle_quizzes()
        elif user_input == "4":
            handle_utilities()
        elif user_input == "5":
            print("Swai: Goodbye! Come back soon.")
            break
        else:
            print("Swai: Invalid option. Try again.")

def handle_birthday_reminder():
    while True:
        print("""
Birthday Reminder Menu:
1. View All Birthdays
2. Add a New Birthday
3. Check a Specific Birthday
4. Back to Utilities
        """)
        user_input = input("Choose an option: ").lower()
        if user_input == "1":
            view_birthdays()
        elif user_input == "2":
            add_birthday()
        elif user_input == "3":
            check_birthday()
        elif user_input == "4":
            break
        else:
            print("Swai: Invalid option. Try again.")


if __name__ == "__main__":
    start_chatbot()
