Children = 3
Hometown = "Lahti"

# Lista pyhtonissa
TownsInFinland = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

RandomInformation = ["Mira", 48, True, Children, Hometown]

print(TownsInFinland[0])
TownsInFinland.append("Rovaniemi")
print(TownsInFinland)

NumOfTown = len(TownsInFinland) #vastaus: 6kpl // len alkaa 1:stä
print(TownsInFinland[NumOfTown-1]) #elementin haussa lähetään 0 liikkeelle

Municipalities = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Oulu", "Tampere"]

MunicipalityAndTowns =  [Municipalities, Towns]

print(MunicipalityAndTowns[1][-2]) #ensimmäinen hakasulku = kumpi valitaan / toinen haka = kuinka mones perästäpäin 

Towns.sort()
print(Towns)

Teacher = {
    'name' : 'Juha',
    'age' : 50,
    'city' : 'Lahti'
}

print(Teacher["name"])

Teacher['email'] = 'juha.hyytainen@lab.fi'

print(Teacher)

# näitä tietoja voidaan luupata

for key in Teacher: 
    print(key, end=' ') #for loop = esim listojen läpi käymiseen  // loppuun lisätty välilyönti
    print(Teacher[key]) # käy läpi kaikki läpi käydyt tiedot 

# Dictionary {} List []
# kirjasto // voi sisältää listoja 
Student = [
    {'name': 'Mikko', 'age': 25, 'city': 'Tampere'},
    {'name': 'Maija', 'age': 30, 'city': 'Espoo'},
    {'name': 'Seppo', 'age': 35, 'city': 'Helsinki'}
    ] 
print(Student[0])

# Listat // voi sisältää kirjastoja
Cities = {
    'Finland': ['Tampere', 'Espoo', 'Helsinki'],
    'Sweden': ['Stockholm', 'Malmö']
}

print(Cities['Finland'][0])

# listat loopissa
for town in Towns:
    print(f"The town of {town}")
print(f"All the towns {Towns}")

# for loop kierrosnumero tallessa i sisällä toistuva merkintä eri koodi kielissä = iteration number
for i in range(1,10):
    print(i)

for i in range(1,10):
    print(i, end=' ')  # end=' '  älä vaihda riviä

print("") # vaihda rivi
for i in range(1, 10, 3):
    print(i)

print("")
Total = 0
for i in range(1,101):
    Total +=i 
    print(Total)
# total on  aina total + edellisen numeronkierros numero
print(Total)

# käyttö mahdollisuus erillaisiin lasku toimituksiin

#yhdeksän kierrosta
for i in range(9):
    if (i == 3):
        continue
    print(i)

# Opiskele loopit -for ja -while, sekä niihin liittyvät komennot -continue ja -break

# while 1 < 10:
#    print("Do not try me at home xD")

i = 0 # lähtee nollast liikkeelle
while i < 10:
    print(f"Iteration number: {i}")
    i += 1
    # i = i + i edeltävä rivi selkeytys

continueLoop = True
while continueLoop == True:
    if input("Do you want to continue? ") != "yes":
        continueLoop = False

while True:
    if input("Do you want to continue? ") != "yes":
        break
    else:
        continue
    