"""
Escriu un programa que et permeti jugar pedra, paper o tisora ​​amb l'ordinador.
Per a això l'ordinador haurà de generar un nombre aleatori entre 1 i 3 que representi pedra, paper o tisora ​​respectivament, i l'usuari/ària haurà de respondre al seu torn amb un nombre entre l'1 i el 3 després de mostrar la següent pantalla:
Juguem a pedra, paper o tisora:

1. Pedra
2. Paper
3. Tisora
Tria (1-3):

Si l'usuari/ària indica algun nombre diferent del sol·licitat, haurà d'aparèixer el següent missatge:
«Entenc que no vols jugar. Adeu»
En cas contrari, indicar el guanyador/a de la següent manera:
Jo xxx i tu xxx. He guanyat!, o Has guanyat!
Segons sigui el cas.
Exemple:
«Jo paper i tu tisora. Has guanyat!»
"""

# Imports
import random

# Variables
mach_hand: int
mach_hand_text: str
hum_hand: int
hum_hand_text: str
winner: str
no_play: str = "«Entenc que no vols jugar. Adeu»"

# Data
mach_hand = random.randint(1, 3)
if mach_hand == 1:
    mach_hand_text = "pedra"
elif mach_hand == 2:
    mach_hand_text = "paper"
else:
    mach_hand_text = "tisora"

get_hum_hand: str = input("""Juguem a pedra, paper o tisora:

1. Pedra
2. Paper
3. Tisora
Tria (1-3): """)

if get_hum_hand.isdigit():
    hum_hand = int(get_hum_hand)
    if hum_hand < 1 or hum_hand > 3:
        print(no_play)
        exit()
else:
    print(no_play)
    exit()

if hum_hand == 1:
    hum_hand_text = "pedra"
elif hum_hand == 2:
    hum_hand_text = "paper"
else:
    hum_hand_text = "tisora"

# Cases (1 wins 3, 2 wins 1, 3 wins 2)
if (
    (mach_hand == 1 and hum_hand == 3)
    or (mach_hand == 2 and hum_hand == 1)
    or (mach_hand == 3 and hum_hand == 2)
):  # machine wins
    winner = "He guanyat!"
elif (
    (mach_hand == 3 and hum_hand == 1)
    or (mach_hand == 1 and hum_hand == 2)
    or (mach_hand == 2 and hum_hand == 3)
):  # human wins
    winner = "Has guanyat!"
else:  # draw
    winner = "Hem empatat!"

# output
message = f"Jo {mach_hand_text} i tu {hum_hand_text}. {winner}"

print(message)
