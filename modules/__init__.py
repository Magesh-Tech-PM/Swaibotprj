"""
SwaiBot Modules Package
This package includes functionalities for games, quizzes, math utilities, Q&A, jokes, and more.
"""

# Importing games
from .swai_games import play_rock_paper_scissors, play_number_guess, play_word_scramble

# Importing quizzes
from .swai_quiz import run_quiz, movie_questions, general_questions, math_questions, capital_questions

# Importing math utilities
from .swai_math import solve_math_problem



# Importing jokes
from .swai_jokes import tell_joke

# Importing multiplayer game
from .swai_multiplayer import multiplayer_number_guess
