# El programa demana dos nombres enters i llavors calcula la suma dels valors compresos entre els dos números, inclosos.
# Exemple: 4 i 6  --> resultat = 4 + 5 + 6 = 15

# Variables
ini: int = 0
fin: int = 0
resultat: int = 0
message: str = ""

# get data
in_ini: str = input("Introdueix el primer nombre enter: ")
if in_ini[0] == "-":
    if in_ini[1:].isdigit():
        ini = -int(in_ini[1:])
elif in_ini.isdigit():
    ini = int(in_ini)
else:
    print("Té que introduxier un nombre enter.")
    exit()

in_fin: str = input("Introdueix el segon nombre enter: ")
if in_fin[0] == "-":
    if in_fin[1:].isdigit():
        fin = -int(in_fin[1:])
elif in_fin.isdigit():
    fin = int(in_fin)
else:
    print("Té que introduxier un nombre enter.")
    exit()

# Operations
if ini > fin:
    temp: int = ini
    ini = fin
    fin = temp

for num in range(ini, fin + 1):
    if num == ini:
        message = f"{ini}"
    else:
        message = f"{message} + {num}"
    resultat += num
message = f"{message} = {resultat}"
# Output
message = f"{ini} i {fin} --> resultat: {message}"

print(message)
