# A2_T5 String length and slicing (TEST TASK)
# Make a Python program, which prompts for a compound word.
print("Program starting.")
# Get following aspects from the word
Compound_word = input ("Insert a closed compound word: ")
# Length
Length = len (Compound_word)
# First character
reversedCharacter = reversed = Compound_word[::-1]
FirstChar_reversed = reversedCharacter[0]
# Reversed version e.g. “Suitcase” is reversed “esactiuS”

print(f"The word you inserted is '{Compound_word}' and reversed it is '{reversedCharacter}'.")
print(f"The inserted word length is '{Length}'")
print(f"Last character is '{FirstChar_reversed}")
# Display the aspects using print commands.
print("Take substring from the inserted word by inserting...")
# Prompt the user to take substring from the existing compound word.
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
# Slice the compound word to the user specified substring.
CompoundWord = Compound_word[start:end:step]

# Finally print the user specified substring.
print(f"The word '{Compound_word}' sliced to the defined substring is '{CompoundWord}'.")
print("Program ending.")