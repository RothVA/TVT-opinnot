# A3_T1 If-statements
# Make Python program and implement if-statements in proper places.
# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:
# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check
# Sum is even.


print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if int1 == int2:
    print("Integers are the same.")
elif int1 > int2:
    print("First integer is greater.")
else:
    print("Second integer is greater.")

# print("Adding integers together")
total = int1 + int2
print(f"{int1} + {int2} = {total}")
# print("Checking the parity of the sum...")
Remainder = total % 2

if Remainder == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")






















# Example program run
# run 1 run 2 run 3
# Program starting.
# Insert two integers.
# Insert first integer: 5
# Insert second integer: 5
# Comparing inserted integers.
# Integers are the same
# Adding integers together
# 5 + 5 = 10
# Checking the parity of the sum...
# Sum is even.
# Program ending.