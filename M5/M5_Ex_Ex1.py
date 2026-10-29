"""
Realitzar un joc per endevinar un nombre aleatori N, entre 1 i 500.

Si la distància entre el nombre a endevinar i el de l'usuari/ària és de 50 o més, el programa haurà de dir:

“Fred, fred: el teu número és més gran “ o “Fred, fred: el teu número és més petit “

Si la distància entre el nombre a endevinar i el de l'usuari/ària està entre 15 i 50, el programa haurà de dir:

“Tebi, Tebi: el teu número és més gran “ o “Tebi, Tebi: el teu número és més petit “

I si la distància entre el nombre a endevinar i el de l'usuari/ària i si la distància és menor a 15, el programa haurà de dir:

“Calent, calent: el teu número és més gran “ o “Calent, calent: el teu número és més petit “

El procés acaba quan l'usuari/ària encerta.
"""

# Imports
import random

# Constants
MESSAGE_FRED_GRAN: str = "Fred, fred: el teu número és més gran"
MESSAGE_FRED_PETIT: str = "Fred, fred: el teu número és més petit"

MESSAGE_TEBI_GRAN: str = "Tebi, tebi: el teu número és més gran"
MESSAGE_TEBI_PETIT: str = "Tebi, tebi: el teu número és més petit"

MESSAGE_CALENT_GRAN: str = "Calent, Calent: el teu número és més gran"
MESSAGE_CALENT_PETIT: str = "Calent, Calent: el teu número és més petit"

# Variables
rand_num: int = random.randint(1, 500)
try_num: int

# input
print("He pensat un número de 1 a 500, endevina'l!")
while True:
    try_num_text: str = input("Introdueix un número: ")
    if try_num_text.isdigit():
        try_num = int(try_num_text)
    else:
        print("Has d'introduir un número enter entre 1 i 500.")
        continue
    if try_num < 1 or try_num > 500:
        print("El número ha d'estar entre 1 i 500.")
        continue

    # Check number
    if (rand_num - try_num) >= 50:
        print(MESSAGE_FRED_GRAN)
    elif (rand_num - try_num) <= -50:
        print(MESSAGE_FRED_PETIT)
    elif (rand_num - try_num) >= 15:
        print(MESSAGE_TEBI_GRAN)
    elif (rand_num - try_num) <= -15:
        print(MESSAGE_TEBI_PETIT)
    elif rand_num > try_num:
        print(MESSAGE_CALENT_GRAN)
    elif rand_num < try_num:
        print(MESSAGE_CALENT_PETIT)
    else:
        print("Has acertat, FELICITATS!!!!")
        break

"""
Alternative check number

if rand_num == try_num:
    print("Has acertat, FELICITATS!!!!")
    break
# Distance
distancia: int = abs(rand_num - try_num)
# Check Fred, Tibi i Calent
if distancia >= 50:
    if try_num < rand_num:
        print(MESSAGE_FRED_GRAN)
    else:
        print(MESSAGE_FRED_PETIT)
elif distancia >= 15:
    if try_num < rand_num:
        print(MESSAGE_TEBI_GRAN)
    else:
        print(MESSAGE_TEBI_PETIT)
else:
    if try_num < rand_num:
        print(MESSAGE_CALENT_GRAN)
    else:
        print(MESSAGE_CALENT_PETIT)
"""
