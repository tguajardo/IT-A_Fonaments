# Fes un programa que pregunti a l'usuari/ària dos nombres enters al qual anomenaràs dividend i divisor respectivament.
# El divisor haurà d'estar comprès entre 2 i 7.
# En cas contrari, el programa haurà de mostrar un missatge d'error.
# Si el divisor és correcte (2-7) mostra en pantalla si el dividend és múltiple del divisor, o no.

# Variables
dividend: int
divisor: int
message: str

# Get Data
text_dividend: str = input("Introdueix el dividend (nombre enter positiu): ")
if text_dividend.isdigit():
    dividend = int(text_dividend)
else:
    print("Error: el dividend no és un nombre enter.")
    exit()

text_divisor: str = input("Introdueix el divisor (nombre enter positiu entre [2,7]): ")
if text_divisor.isdigit():
    divisor = int(text_divisor)
    if divisor < 2 or divisor > 7:  # check range
        print("Error: el divisor ha d'estar entre 2 i 7.")
        exit()
else:
    print("Error: el divisor no és un nombre enter.")
    exit()

# check multiple
if dividend % divisor == 0:
    message = f"{dividend} és múltiple de {divisor}."
else:
    message = f"{dividend} no és múltiple de {divisor}."

# Output
print(message)
