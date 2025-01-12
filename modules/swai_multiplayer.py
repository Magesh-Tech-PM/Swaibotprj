# Description: Module for multiplayer games like the number guessing game.
# Author: Mags

import random


def multiplayer_number_guess():
    """
    A multiplayer number guessing game where two players compete to guess
    a random number. Swai announces the winner based on the number of attempts.
    """
    print("Swai: Welcome to the Multiplayer Number Guessing Game!")
    print("Swai: I'm thinking of a number between 1 and 50.")
    number_to_guess = random.randint(1, 50)

    # Track attempts for each player
    player_attempts = {"Player 1": 0, "Player 2": 0}
    players = ["Player 1", "Player 2"]

    while True:
        for player in players:
            try:
                guess = int(input(f"{player}, enter your guess: "))
                player_attempts[player] += 1

                if guess < number_to_guess:
                    print(f"Swai: Too low, {player}! Try again.")
                elif guess > number_to_guess:
                    print(f"Swai: Too high, {player}! Try again.")
                else:
                    print(f"Swai: Congratulations, {player}! You guessed the number.")
                    print(f"Swai: It took {player_attempts[player]} attempts.")
                    print(
                        f"Swai: {players[1 - players.index(player)]} took {player_attempts[players[1 - players.index(player)]]} attempts.")

                    # Determine the winner
                    if player_attempts["Player 1"] < player_attempts["Player 2"]:
                        return "Swai: Player 1 wins!"
                    elif player_attempts["Player 1"] > player_attempts["Player 2"]:
                        return "Swai: Player 2 wins!"
                    else:
                        return "Swai: It's a tie!"
            except ValueError:
                print("Swai: Please enter a valid number.")
