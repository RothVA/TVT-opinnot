#Tehtävä:
# Jos käyttäjätunnus = OmaNimi ja ikä >= 18 ja käyttäjä on admin => avataan admin-sivu
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 >= avataan käyttäjäsivu
# Jos ikä < 18 => kerrotaan  käyttäjälle: Ikä ei riitä
# Jos käyttäjätunnus != omaNimi => Pääsykielletty

# Admin tunnuksilla valikko: 1. lisää uusi käyttäjä, 2. tarkista laitteen toiminta, 3. exit
# Käyttäjäsivulla valikko: 1. Tarkista omat tiedot, 2. exit

# ilman while loop käyttöä / viikko 3 harjoite

print("Turn back now.")
name = input("If you think you belong here, state your name:  ")
age = int(input("Only a fool of a took thinks it's wise enough, state your age: "))

Gandalf = "OmaNimi"
Frodo = "omaNimi"

if name == Gandalf:
    if age >= 18:
        print("Welcome to Shire")   # admin sivu
        print("Valikko:\n1. Lisää uusi käyttäjä\n2. Tarkista laitteen toiminta\n3. Exit")
        choice = input("Valitse toiminto (1-3): ")
        if choice == "1":
            print("Lisää uusi ystävä...")
        elif choice == "2":
            print("Tarkistetaan laitteen toiminta...")
        elif choice == "3":
            print("Leaving Shire.")
        else:
            print("There are other forces in the world, and some are not for you to command")
    else:
        print("Worry not, there's still time for you to grow")
    

if name == Frodo:
    if age >= 18:
        print("Welcome friend")     # käyttäjä sivu
        print("Valikko:\n1. Tarkista omat tiedot\n2. Exit")
        choice = input("Valitse toiminto (1-2): ")
        if choice == "1":
            print(f"Nimi: {name}, Ikä: {age}")
        elif choice == "2":
            print("Leaving so soon friend.")
        else:
            print("There are other forces in the world, and some are not for you to command")
    else:
        print("Not to day young one")


if name != Gandalf:
    if name != Frodo:
        print("You shall not PASS!")

print("The End.")

        




