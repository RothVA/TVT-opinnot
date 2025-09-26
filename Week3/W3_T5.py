# A3_T5 Temperature converter (TEST TASK)
# Create a temperature unit conversion program.
# Start the program by listing options for the user:
# Celsius to Fahrenheit
# Fahrenheit to Celsius
# Exit
# Prompt user to insert choice. After the decision to convert, 
# ask the amount of current temperature (use the floating point datatype). 
# Lastly show the converted value to the user.
# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8
# Data representation examples:
# 50.0 °F
# 10.0 °C
# Use 1 decimal precision to round the converted value.

print("Program starting.\n")
print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))
if (choice == 1):
    celsius = float(input("Insert the amount of Celsius: "))
    Fahrenheit = (celsius * 1.8) + 32
    print(f"{celsius:.1f} °C equals to {Fahrenheit:.1f} °F")
elif (choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (Fahrenheit - 32) / 1.8
    print(f"{Fahrenheit:.1f} °F equals to {celsius:.1f} °C")
elif (choice == 0):
    print("Exiting...")

print("\nProgram ending.")










# Example program runs
# run 1 run 2 run 3
# Program starting.
# Options:
# 1 - Celsius to Fahrenheit
# 2 - Fahrenheit to Celsius
# 0 - Exit
# Your choice: 1
# Insert the amount of Celsius: 23
# 23.0 °C equals to 73.4 °F
# Program ending.