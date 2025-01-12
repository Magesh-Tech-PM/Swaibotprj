# Description: Module for solving math problems.
# Author: Mags

def solve_math_problem():
    """
    This function prompts the user to enter a math expression and evaluates it.
    It handles basic arithmetic operations like addition, subtraction, multiplication,
    and division. If the input is invalid, it provides an error message.
    """
    try:
        expression = input("Swai: Enter a math problem (e.g., 5 + 3): ")
        result = eval(expression)
        print(f"Swai: The answer is {result}.")
    except ZeroDivisionError:
        print("Swai: Oops! Division by zero is not allowed.")
    except Exception as e:
        print(f"Swai: Hmm, there seems to be an error: {e}")
