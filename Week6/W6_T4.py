# A6_T4 String analytics
# Datasets
# A6_T4_D1.txt
# A6_T4_D2.txt
# A6_T4_D3.txt
# Create a Python program which is able to analyse names listed in a text file (See dataset files):

# Analyse and specify following aspects from the file:

# The amount of names
# Shortest name
# Longest name
# Average name length.
# Let the user specify the filename for the analysis. Program reads the file and prints the results from the analysis. 
# Values must be presented like shown in the example program runs. 
# Average name length must be presented in 2 decimal precision. 
# Use Format Specification Mini-Language to achieving the required precision for the data presentation.

# Note! Given text files may contain empty rows and the program must be able to skip them if present.

# Other tips:

# Read text file line-by-line.
# Pay attention to the reading process (newline characters).
# Names can be stored into a single string variable.
# Consider separating names with a semicolon ;
# John;Doe;Jane
# Report can be stored into one string variable.
# Format Specification Mini-Language.
# E.g., "Value in 2 decimal precision {:.2f}".format(3.555)


def main(): 
    print("Program starting.")
    print("This program analyses a list of names from a file.")
    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')
    
    names = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            if name:  # Skip empty lines
                names.append(name)

    print("Analysing names...")
    name_count = len(names)
    shortest_name = min(names, key=len) if names else ""
    longest_name = max(names, key=len) if names else ""
    average_length = sum(len(name) for name in names) / name_count if name_count > 0 else 0.0
    print("Analysis complete!")

    print("#### REPORT BEGIN ####")
    print(f"Name count - {name_count}")
    print(f"Shortest name - {len(shortest_name)} chars")
    print(f"Longest name - {len(longest_name)} chars")
    print(f"Average name - {average_length:.2f} chars")
    print("#### REPORT END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()


# Example program runs
# run 1 run 2 run 3
# Program starting.
# This program analyses a list of names from a file.
# Insert filename to read: A6_T4_D1.txt
# Reading names from "A6_T4_D1.txt".
# Analysing names...
# Analysis complete!
# #### REPORT BEGIN ####
# Name count - 2
# Shortest name - 3 chars
# Longest name - 4 chars
# Average name - 3.50 chars
# #### REPORT END ####
# Program ending.

