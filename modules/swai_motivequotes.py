import random

quotes = [
    "The best way to predict the future is to create it.",
    "Believe you can and you're halfway there.",
    "Don't watch the clock; do what it does. Keep going."
]

def get_quote():
    return random.choice(quotes)
