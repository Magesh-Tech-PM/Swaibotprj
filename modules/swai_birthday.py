# Description: Module for managing birthday reminders (view, add, and check birthdays).
# Author: [Your Name]

# Dictionary to store names and birthdays
birthdays = {
    "Alice": "1995-03-15",
    "Bob": "1990-07-22",
    "Charlie": "1985-12-05"
}

# Function to view all birthdays
def view_birthdays():
    if birthdays:
        print("Swai: Here are the birthdays I know:")
        for name, date in birthdays.items():
            print(f"{name}: {date}")
    else:
        print("Swai: No birthdays found!")

# Function to add a new birthday
def add_birthday():
    name = input("Swai: Enter the name: ").strip()
    if name in birthdays:
        print(f"Swai: {name}'s birthday is already recorded as {birthdays[name]}.")
    else:
        date = input("Swai: Enter their birthday (YYYY-MM-DD): ").strip()
        birthdays[name] = date
        print(f"Swai: Birthday for {name} added!")

# Function to check a specific birthday
def check_birthday():
    name = input("Swai: Whose birthday would you like to check? ").strip()
    if name in birthdays:
        print(f"Swai: {name}'s birthday is on {birthdays[name]}.")
    else:
        print(f"Swai: Sorry, I don't have {name}'s birthday on file.")
