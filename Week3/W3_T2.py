# A3_T2 String comparisons
# Make Python program which does the following steps:
# Prompt user to insert
# A word
# A character
# Find if the character exists in the word. Possible prints below.
# Word "{WordFirst}" contains character "{Character}"
# Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# Both inserted words are the same alphabetically, "{WordFirst}"


print("Program starting.")
print("String comparisons")
word1 = input("Insert first word: ")
char = input("Insert a character: ")   
if (char in word1):
    print(f"Word \"{word1}\" contains character \"{char}\"")
else:    
    print(f"Word \"{word1}\" doesn't contain character \"{char}\"")

word2 = input("Insert second word: ")
if word1 < word2:
    print(f"The first word \"{word1}\" is before the second word \"{word2}\" alphabetically.")
elif word1 > word2:
    print(f"The second word \"{word2}\" is before the first word \"{word1}\" alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically, \"{word1}\"")
print("Program ending.")











# Example program run
# run 1 run 2 run 3
# Program starting.
# String comparisons
# Insert first word: beans
# Insert a character: n
# Word "beans" contains character "n"
# Insert second word: banana
# The second word "banana" is before the first word "beans" alphabetically.
# Program ending.