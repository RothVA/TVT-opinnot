# A4_T1 For-loop 1
# Create a Python program which prompts user to insert two integers. 
# Use these integers together with the “for-loop” structure to create behaviour like in 
# the example program example run below.
# Note! the autograding tool will test that the correct structure has been applied.


print("Program staring")
print("")
StartValue = int(input("Insert starting value: "))
StopValue = int(input("Insert stopping value: "))
print("")
print("Starting for-loop:")
for i in range(StartValue, StopValue + 1):
    print(i)
print("")
print("Program ending.")


# Example program runs
# run 1 run 2 run 3
# Program starting.
# Insert starting value: 1
# Insert stopping value: 10
# Starting for-loop:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Program ending.