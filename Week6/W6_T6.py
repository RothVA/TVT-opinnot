# A6_T6 Cipher messages (TEST TASK)
# In this exercise, get familiar with the Caesar cipher and specificly on the ROT13 implementation.

# Caesar Cipher explained (3 minutes): youtu.be/sMOZf4GN3oc

# Video Thumbnail
# Click to play in YouTube

# ROT13 Converter

# Plain text
# Type here...
# Ciphered text
# Glcr urer...
# Create a Python program which collects plain text rows from user till the user inserts an empty row. 
# ipher all rows and then ask user to choose between showing the ciphered text or saving it.

# A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
# N	O	P	Q	R	S	T	U	V	W	X	Y	Z	A	B	C	D	E	F	G	H	I	J	K	L	M
# Program must be able to cipher following lowercase and uppercase alphabets. 
# Other characters remains same during ciphering operation.

# # English alphabets (2 x 26)
# LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
# UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")
    plain_rows = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        plain_rows.append(row)

    LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
    UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphered_rows = []
    for row in plain_rows:
        ciphered_row = ""
        for char in row:
            if char in LOWER_ALPHABETS:
                index = LOWER_ALPHABETS.index(char)
                ciphered_char = LOWER_ALPHABETS[(index + 13) % 26]
                ciphered_row += ciphered_char
            elif char in UPPER_ALPHABETS:
                index = UPPER_ALPHABETS.index(char)
                ciphered_char = UPPER_ALPHABETS[(index + 13) % 26]
                ciphered_row += ciphered_char
            else:
                ciphered_row += char
        ciphered_rows.append(ciphered_row)

    print("#### Ciphered text ####")
    for c_row in ciphered_rows:
        print(c_row)
    print("#### Ciphered text ####")

    choice = input("Insert filename to save: ")
    with open(choice, "w", encoding="utf-8") as file:
        for c_row in ciphered_rows:
            file.write(c_row + "\n")
    print("Ciphered text saved!")
    print("Program ending.")
    return None




if __name__ == "__main__":
    main()

# Example program runs:
# run 1 run 2 run 3 run 4
# Program starting.
# Collecting plain text rows for ciphering.
# Insert row(empty stops): Hello
# Insert row(empty stops): World
# Insert row(empty stops): 
# #### Ciphered text ####
# Uryyb
# Jbeyq
# #### Ciphered text ####
# Insert filename to save: A6_T6_F1.txt
# Ciphered text saved!
# Program ending.
