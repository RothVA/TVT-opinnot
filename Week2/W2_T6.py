# A2_T6 Hex Colors (TEST TASK)
# Write a Python program which asks user to insert hex color. 
print("Program starting.\n")
hex = input("Insert a hex color: ")

print("\nColors")
print(f"- Red {hex[1:3]}")
print(f"- Green {hex[3:5]}")
print(f"- Blue {hex[5:7]}\n")

# print(f"- Red {FirstTwo}")
# print(f"- Green {SecondTwo}")   
# print(f"- Blue {LastTwo}\n")
print("Program ending.")   


# In this case hex color is expected to be the 7 character representation 
# starting with # and followed by 6 0-F characters to represent RGB colors. 
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

# Slice the amount of red, green and blue from that inserted color 
# and display each color as shown below.