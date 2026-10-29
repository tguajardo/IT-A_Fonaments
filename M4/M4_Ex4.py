# L’usuari/ària introdueix un número de mes per pantalla i mitjançant un match amb els 12 mesos de l’any, el programa calcula els dies del mes i mostra el següent:
# Exemple: Si el número introduït és 1, llavors ha d'aparèixer per pantalla: “El mes de gener té 31 dies”
# Variables
mes_nom: str
mes_dies: int = 0
message: str

# Data
mes: int = int(input("Introdueix un mes com a nombre.(1-12)"))

# Operation
match mes:
    case 1:
        mes_nom = "gener"
        mes_dies = 31
    case 2:
        mes_nom = "febrer"
        mes_dies = 28
    case 3:
        mes_nom = "març"
        mes_dies = 31
    case 4:
        mes_nom = "abril"
        mes_dies = 30
    case 5:
        mes_nom = "maig"
        mes_dies = 31
    case 6:
        mes_nom = "juny"
        mes_dies = 30
    case 7:
        mes_nom = "juliol"
        mes_dies = 31
    case 8:
        mes_nom = "agost"
        mes_dies = 31
    case 9:
        mes_nom = "setembre"
        mes_dies = 30
    case 10:
        mes_nom = "octubre"
        mes_dies = 31
    case 11:
        mes_nom = "novembre"
        mes_dies = 30
    case 12:
        mes_nom = "desembre"
        mes_dies = 31
    case _:
        mes_nom = "mes no valid"

if mes_dies == 0:
    message = f"{mes_nom}"
else:
    message = f"El mes de {mes_nom} té {mes_dies} dies."

# Output
print(message)
