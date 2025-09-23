# A2_T5 String length and slicing (TEST TASK)
# Make a Python program, which prompts for a compound word.
# Get following aspects from the word
# Length
# Reversed version e.g. “Suitcase” is reversed “esactiuS”
# Display the aspects using print commands.
# Prompt the user to take substring from the existing compound word.
# Slice the compound word to the user specified substring.
# Finally print the user specified substring.

print("Program starting.\n")
Compound_word = input ("Insert a closed compound word: ")
Length = len(Compound_word)
reverse = Compound_word[::-1]
print(f"The word you inserted is '{Compound_word}' and in reverse it is '{reverse}'.")
print(f"The inserted word length is {Length}")
lastchar = Compound_word[-1]
print(f"Last character is '{lastchar}'\n")
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
slicedword = Compound_word[start:end:step]
print(f"\nThe word '{Compound_word}' sliced to the defined substring is '{slicedword}'.")
print("Program ending.")