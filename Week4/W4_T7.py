# A4_T7 Multiplicative persistency (TEST TASK)
# Create program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.
# In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.
# The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.
# Example program runs
# run 1 run 2 run 3 run 4
# Program starting.
# Check multiplicative persistence.
# Insert an integer: 277777788888899
# 2 * 7 * 7 * 7 * 7 * 7 * 7 * 8 * 8 * 8 * 8 * 8 * 8 * 9 * 9 = 4996238671872
# 4 * 9 * 9 * 6 * 2 * 3 * 8 * 6 * 7 * 1 * 8 * 7 * 2 = 438939648
# 4 * 3 * 8 * 9 * 3 * 9 * 6 * 4 * 8 = 4478976
# 4 * 4 * 7 * 8 * 9 * 7 * 6 = 338688
# 3 * 3 * 8 * 6 * 8 * 8 = 27648
# 2 * 7 * 6 * 4 * 8 = 2688
# 2 * 6 * 8 * 8 = 768
# 7 * 6 * 8 = 336
# 3 * 3 * 6 = 54
# 5 * 4 = 20
# 2 * 0 = 0
# No more steps.
# This program took 11 step(s)
# Program ending.

# Pyydä arvo ja muuta se integeriksi
# Alusta muuttuja, joka laskee kierroksia
#     Tee While loop, joka looppaa niin kauan kuin arvo ei ole 0
#     Muuta arvo integeriksi, jotta saamme yksittäiset numerot esiin
#     Tee for loop, joka käy läpi jokaisen luvun
#         Testaa, onko numero viimeinen
#         Tee myös laskutoimitus
#     printtaa kertolaskun tulos
#     Muuta arvoksi edellisen kierroksen kertolaskun tulos
#     Jos arvo on nolla, printtaa No more steps
#     Lisää kierroslaskuriin +1
# printtaa kierrokset



print("Program starting.\n")

print("Check multiplicative persistence.")
arvo = input("Insert an integer: ")
x = int(arvo)

def per(number):
    steps = 0

    while number >= 10:                                           # jatkuu kunnes alle 10 numeroinen jäljellä
        digits = [int(d) for d in str(number)]                    # digien valinta string numerosta
        laskujono = " * ".join(str(d) for d in digits)            # välimerkki, string jono, digits:in string listaus

        result = 1
        for digit in digits:
            result *= digit

        print (f"{laskujono} = {result}")                         # useita tuloksia
        
        number = result
        steps += 1
    print("No more steps.\n")
    print(f"This program took {steps} step(s)")
per(x)

print("\nProgram ending.")