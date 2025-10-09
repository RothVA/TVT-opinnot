# A4_T5 Break and continue
# Make a program, which prompts user to insert three integers:

# Starting point
# Stopping point
# Inspection point
# Test the points with following rules(Note! testing order matters):
# Starting point must be less than stopping point
# "Starting point value must be less than the stopping point value."
# The inspection point must be within the range of the start and stop points.
# "Inspection value must be within the range of start and stop."
# If any rule above is broken, print the violation message(s) to the user and then skip the next part till the "Program ending." 
# print.# Run two for-loops like shown in the example program runs if none of the rules above are broken. Inside the loops, 
# compare the inspection point to the current iteration. Use break and continue commands if the current iteration is same as 
# the inspection point. Otherwise print the current iteration on the same line.
# Note! There must be no trailing space character at the end of any row.

print("Program starting.")
print("")
Feed = input("Insert starting point: ")
PointStart = int(Feed)
Feed = input("Insert stopping point: ")
PointStop = int(Feed)
Feed = input("Insert inspection point: ")
PointInspect = int(Feed)
print("")

Run = True
if (PointStart >= PointStop) or (PointStart > PointInspect < PointStop):
    print("Starting point value must be less than the stopping point value.")
    print("Inspection value must be within the range of start and stop.")
    Run = False
if ((PointStart > PointInspect) or (PointInspect > PointStop)):
    print("\nThe inspection point must be within the range of the start and stop points.")
    Run = False
if (Run):
    print("\nFirst loop - inspection with break:")
    for i in range(PointStart, PointStop):
        if(i == PointInspect):
            break
        else: 
            print(i, end=' ')
    print("")
    print("\nSecond loop - inspection with continue:")
    for i in range(PointStart, PointStop-1):
        if(i == PointInspect):
            continue
        else: 
            if(i == (PointStop)):
                print(i)
            else:
                print(i, end=' ')
print("")
print("\nProgram ending.")










# Example program runs

# run 1 run 2 run 3 run 4 run 5 run 6
# Program starting.

# Insert starting point: 3
# Insert stopping point: 8
# Insert inspection point: 5

# First loop - inspection with break:
# 3 4
# Second loop - inspection with continue:
# 3 4 6 7

# Program ending.
