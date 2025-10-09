# A4_T4 Repetitive prompt
# Make a program, which prompts user to insert words. Program must stop prompting words if user inserts empty word. After stopping the repetitive prompt, print the amount of words and characters that the user inserted.

print("Program starting")
print("")
WordCount = 0
CharCount = 0

Word = input("insert word (empty stops): ")
while Word != '':
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("")
print("You inserted: ")
print(f"- {WordCount} words")
print(f"- {CharCount} characters")
print("")
print("Program ending")




# Example program run:
# run 1 run 2 run 3
# Program starting.
# Insert word (empty stops): Close
# Insert word (empty stops): the
# Insert word (empty stops): loop
# Insert word (empty stops): 
# You inserted:
# - 3 words
# - 12 characters
# Program ending.