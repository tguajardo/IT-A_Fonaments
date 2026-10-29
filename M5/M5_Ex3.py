# L’exercici consisteix a què l’usuari/ària ha d'endevinar el número escollit aleatòriament pel programa.
# El programa, demana números a l’usuari/ària fins que aquest encerti el número aleatori generat pel programa.
# Un cop l’usuari/ària ha endevinat el número, es mostrarà per pantalla el següent missatge: “Enhorabona, el número era X”.

# Imports
import random

# Variables
rand_num: int = random.randint(1, 10)
try_num: int

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
        print(f"Has endevinat, el número era {try_num}")
        break
    else:
        print("Número equivocat, prova una altre vegada")
