# A6_T1 Read text file
# Datasets
# A6_T1_D1.txt
# A6_T1_D2.txt
# A6_T1_D3.txt
# Create a program that can read a text file and then print the file content. 
# User must be able to specify the file name. 
# Decorate the beginning and the end of the file with a decorative line.
# Decorative lines
# #### START "{filename}" ####
# #### END "{filename}" ####



def read (filename):
    with open(filename, 'r') as file:
        return file.read()


def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = (input("Insert filename: "))
    print(f"#### START \"{filename}\" ####")
    show = read(filename)
    print(show if "end:" not in show else show)
    if "end:" not in show:
        print(f"#### END \"{filename}\" ####")
    print("Program ending.")
    return None
    

if __name__ == "__main__":
    main()


# Example program runs
# run 1 run 2 run 3
# Program starting.
# This program can read a file.
# Insert filename: A6_T1_D1.txt
# #### START "A6_T1_D1.txt" ####
# Hello
# World
# #### END "A6_T1_D1.txt" ####
# Program ending.