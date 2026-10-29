"""
Realitza un programa que pinti la lletra L per pantalla feta amb asteriscs.

El programa demanarà l'altura.

El pal horitzontal de la L tindrà una longitud de la meitat (divisió entera entre 2) de l'altura més un.
"""

# Constants
PAINT_CHAR: str = "*"

# Input
alcada: int
base: int

alcada_text: str = input("Introduïu l'alçada de la L: ")
if alcada_text.isdigit():
    alcada = int(alcada_text)
else:
    print("Has d'introduir un número enter.")
    exit()

base = int(alcada / 2) + 1  # alcada // 2 + 1

for index in range(alcada - 1):
    print(PAINT_CHAR)
print(PAINT_CHAR * base)
