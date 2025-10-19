# A5_T6 Tally counter (TEST TASK)
# Make a menu-driven Python program which mimics Tally Counter.
# This menu-driven program must contain a maintainable program structure with the following requirements:
# main function which represents the main program logic including menu cycle.
# showOptions function which takes no arguments, shows the available options in the standard output and returns None.
# askChoice function which takes no arguments, prompts user to insert choice and returns an integer regardless of the user feed.
# In case user incorrectly inserts text as a choice, the program must output "Unknown option!". 
# For this, see the string method isnumeric() behaviour described in W3S or via Python documentation.
# See other requirements in the example program runs below.

# Example program runs
# run 1 run 2 run 3 run 4 run 5 run 6
# Program starting.
# Options:
# 1 - Show count
# 2 - Increase count
# 3 - Reset count
# 0 - Exit
# Your choice: 1
# Current count - 0
# Options:
# 1 - Show count
# 2 - Increase count
# 3 - Reset count
# 0 - Exit
# Your choice: 0
# Exiting program.
# Program ending.

def askChoice():
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        return print("Unknown option!\n")

def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    None

def main():
    print("Program starting. ")
    count = 0
    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}\n")
        elif choice == 2:
            count += 1
            print("Count increased!\n")
        elif choice == 3:
            count = 0
            print("Cleared count!\n")
        elif choice == 0:
            print("Exiting program.\n")
            break
        elif choice:
            print("Unknown option!\n")
        
    print("Program ending.")

main()
