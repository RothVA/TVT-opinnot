# A4_T3 While-loop
# Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.
# Note! the autograding tool will test that the correct structure has been applied.
# Example program runs
# run 1 run 2 run 3
# Program starting.
# Insert starting value: 1
# Insert stopping value: 10
# Starting while-loop:
# 1 2 3 4 5 6 7 8 9 10
# Program ending.

print("\nProgram starting.")
print("")
StartValue = int(input("Insert starting value: "))
StopValue = int(input("Insert stopping value: "))
print("")
print("Starting while-loop:")
thisData = StartValue
while thisData <= StopValue:
    print(thisData, end=" ")
    thisData += 1
    
print("")
print("\nProgram ending.")