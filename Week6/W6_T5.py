# A6_T5 Number analytics (TEST TASK)
# Datasets
# A6_T5_D1.txt
# A6_T5_D2.txt
# A6_T5_D3.txt
# Create a program which can analyse numbers in a text file.

# Required values in analysis:

# Total - integer - Sum of numbers
# Count - integer - Rows that contain values
# Greatest - integer - The greatest number of them all
# Average - decimal - The numbers average
# Think about the processes or “steps” of the analytics first. 
# A prosess which can be described with a name should be wrapped into a function. 
# This function then should only do the task, which belongs to it based on the name. 
# For example if the function name is “readValues”, then the function should read the values from a file. 
# If the function name is “analyseNumbers”, then it should not read a textfile.

# This can be difficult at first with the current know-how, 
# because return statement can only return one value and we have not looked into the datastructures yet. 
# But if you want, you can wrap the values into a string variable using separator in-between the values. 
# This way string can contain multiple values and can be returned as a single value from a function.

# Pseudo-example below:

# SEPARATOR = ";"

# def readValues() -> str:
#   # read operations...
#   Values: str = ""
#   Values += str(13) + SEPARATOR
#   Values += str(45) + SEPARATOR
#   Values += str(20)
#   return Values
# contain only things that the Divide the program structure based on the processes. 
# Define functions to handle the meaningful smaller parts of the program e.g., reading numbers from a given textfiles, 
# analysing numbers and displaying results. 
# Reading values from a file and then storing the values back into a string for the return will help to separate 
# value reading and analysis into their own functionalities.

# This task will not evaluate how well you have structured your code 
# or separated the processes into their own functionalities. 
# But definitely this is a good place to start to consider how robust code are you actually building.

# Present average result in 2 digit precision. Utilize the Format Specification Mini-Language.

# Syntax for 2 digit precision: '{:.2f}'

# Dataset details:

# These datasets contain only positive integer numbers.
# No empty lines. POSIX Line definition
# The results are displayed in CSV format in the example program runs. 
# The first row contains headers, followed by a single data row. 
# Both the column headers and the data values are separated by a semicolon (;). 
# The format is similar to how data is structured in Excel.

# Count	Sum	Greatest	Average
# 2	53	43	26.50

def main():
    print("Program starting.")
    print("This program analyses numbers from a file.")
    filename = input("Insert filename: ")
    print(f'Reading numbers from "{filename}".')

    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            number = line.strip()
            if number.isdigit():  # Ensure it's a valid positive integer
                numbers.append(int(number))

    print("Analysing numbers...")
    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers) if numbers else 0
    average = total / count if count > 0 else 0.0
    print("Analysis complete!")

    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(f"{count};{total};{greatest};{average:.2f}")
    print("#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()


# Example program runs
# run 1 run 2 run 3
# Program starting.
# Insert filename: A6_T5_D1.txt
# #### Number analysis - START ####
# File "A6_T5_D1.txt" results:
# Count;Sum;Greatest;Average
# 2;53;43;26.50
# #### Number analysis - END ####
# Program ending.
