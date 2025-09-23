# A2_T7 Fahrenheit to Celcius
# Create a Python program to convert Fahrenheit to Celcius. 
# Round the Celsius to 1 decimal precision.

# Formula to calculate Celcius from Fahrenheit is (Fahrenheit - 32) / 1.8

print("Program starting.")
Farenheit = float(input("Insert fahrenheits: "))
Celcius = round((Farenheit - 32) / 1.8, 1)
print(f"{Farenheit}F is {Celcius}C")
print("Program ending.")