# print() # tämä on funktion kutsu
# print("Hello") # 'Hello' on funktion parametri
# len() # mitattava stringi/parametri

# # tämä on koodi blokki joka käydään vain kerran sen sisällä, kun siitä edetään alaspäin, ei tähän voi palata ilman funktiokutsua
# while True:
#     print("I can do this 4ver") 
# siisteydeksi funktiot tulee ekana koodissa, ja lopussa funktiokutsutaan toimintaan

# 1.
# def greet(name):
#     print(f"Hello {name}")


# print("Here i am")
# # name = "Ville"
# # greet = (name)
# greet("Ville") #funktion pitää pystyy ottaa tämä parametri vastaan, eli tarvii (name): + f" {name}"

# 2.
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Ville"))

# 3.
def greeting_airport(person, age):
    print(f"How do you do {person}")
    if age >= 18:
        print("Welcome to your flight")
    else:
        print(f"You need to wait for {18-age} years to flight solo")

# greeting_airport("Ville", 5) # funktion kutsut haetaan jäjestyksessä, mikäli niitä ei erikseen määritä
greeting_airport()

# Alkuluku = Prime number : alkuluku joka on suurempi kuin 1 ja sillä on kaksi positiivista jakajaa, esim.2,3,5,7,11,13,17,19,23..

Tee ohjelma, joka kysyy käyttäjältä kokonaislukua. Testaa funktiolla, onko se alkuluku (prime number) vai ei.
Kysy uutta lukua, kunnes käyttäjä pyytää lopettamaan kysymyksen.