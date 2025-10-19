# A5_T3 Ask name
# Create a Python program with two functions:

# main-function
# Does the routines ("Program starting." and "Program ending.")
# Utilizes askName-function.
# Utilizes greetUser-function.
# Returns None
# askName-function
# Prompts the user to insert name
# Returns name
# greetUser-function
# Which takes PName as an argument
# Greets the user "Hello {PName}!"
# Returns None
# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.

# run 1 run 2 run 3
# Program starting.
# Insert name: John
# Hello John!
# Program ending.

def askName() -> str:
    name = input("Insert name: ")
    return name

def greetUser(Pname) -> None:
    print(f"Hello {Pname}!")
    return None

def main() -> None:
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()