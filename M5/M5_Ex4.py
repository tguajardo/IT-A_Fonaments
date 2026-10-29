"""
Has de modificar el programa anterior per afegir una nova funcionalitat: establir un número màxim de 5 intents.

Si l’usuari/ària encerta el número escollit pel programa abans d'aquests 5 intents, el programa mostra el següent missatge per pantalla: “Enhorabona, el número és X i has necessitat Y intents per encertar-lo”.

Si no encerta el número abans de 5 intents, el programa mostra per pantalla: “Has utilitzat massa intents! El número és X”.
"""

# Imports
import random

# Variables
rand_num: int = random.randint(1, 10)
try_num: int
tries: int = 1

# input
print("He pensat un número de 1 a 10, endevina'l!")
while True:
    try_num_text: str = input("Introdueix un número: ")
    if try_num_text.isdigit():
        try_num = int(try_num_text)
    else:
        print("Has d'introduir un número enter entre 1 i 10.")
        continue
    if try_num < 1 or try_num > 10:
        print("El número ha d'estar entre 1 i 10.")
        continue
    # check
    if try_num == rand_num:
        print(
            f"Enhorabona, el número és {rand_num} i has necessitat {tries} intents per encertar-lo"
        )
        break
    else:
        tries += 1
        if tries > 5:
            print(f"Has utilitzat massa intents! El número és {rand_num}")
            break
        print("Número equivocat, prova una altre vegada")
