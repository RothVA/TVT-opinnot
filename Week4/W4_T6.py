# A4_T6 Collatz Conjecture (TEST TASK)
# youtube + wikipedia linkit
# Collatz Conjecture 1 - 10
# Create a program which prompts the user to insert an integer and then display 
# the collatz conjecture as shown in the examples below.
# run 1 run 2 run 3 run 4
# Program starting.
# Insert a positive integer: 10
# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Sequence had 6 total steps.
# Program ending.

# Tee muuttuja , joka laskee kierrokset
# Muuta annettu arvo integeriksi
# Arvo muuttuu loopin aikana
# Tee while -loop, joka looppaa niin kauan, kuin luku ei ole 1
#     printtaa alkuperäinen luku ja lisää loppuun ->
#     testaa onko luku parillinen
#         jaa arvo kahdella
#     muussa tapauksessa
#         kerro arvo kolmella ja lisää yksi
#     lisää kierroksiin +1
# printtaa kierrokset

print("Program starting.")
Kierroslaskuri = int(input("Insert a positive integer: "))

def TotalSteps (arvo): # valittu parametri "arvo" jota pyörittää def funktionin sisällä / huom. funtiota ei kutsuta tässä vielä, kertoo pythonille mitä funktio tekee
    steps = 0          # kierrosten lasku aloitettu omalla variablella
    while arvo != 1:
        print(f"{arvo} -> ", end="")
        if arvo % 2 == 0:              # parillisuuden testaus % 2 == 0: 
            arvo = arvo // 2           # jaetaan kahdella // 2
        else:
            arvo = arvo * 3 + 1        # ei parillinen kerrotaan kolmella + 1
        steps += 1                     # ensimmäisen kierroksen kirjaus
    print("1")                                  # viimeinen step ykköseksi
    print(f"Sequence had {steps} total steps.") # stepit ylös
TotalSteps(Kierroslaskuri)                      # kutsutaan TotalSteps funktio ja int variable Kierroslaskuri

print("\nProgram ending.")



# def TotalSteps(n): ... = writing the recipe.
# TotalSteps(Kierroslaskuri) = cooking the recipe (using the ingredients you got from the user input).