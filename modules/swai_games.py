import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        return "Swai: Invalid choice. Please choose rock, paper, or scissors."
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        return f"Swai: It's a tie! We both chose {bot_choice}."
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return f"Swai: You win! I chose {bot_choice}."
    else:
        return f"Swai: I win! I chose {bot_choice}."


def play_number_guess():
    import random
    number = random.randint(1, 20)
    print("Swai: I'm thinking of a number between 1 and 20. Can you guess it?")

    attempts = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            if guess < number:
                print("Swai: Too low! Try again.")
            elif guess > number:
                print("Swai: Too high! Try again.")
            else:
                return f"Swai: Congratulations! You guessed it in {attempts} attempts."
        except ValueError:
            print("Swai: Please enter a valid number.")


def play_word_scramble():
    words = ["python", "chatbot", "programming", "developer", "algorithm"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))

    print(f"Swai: Unscramble this word: {scrambled}")
    attempts = 0
    while True:
        user_guess = input("Your guess: ").lower()
        attempts += 1
        if user_guess == word:
            return f"Swai: Well done! You unscrambled the word in {attempts} attempts."
        else:
            print("Swai: Incorrect. Try again.")
