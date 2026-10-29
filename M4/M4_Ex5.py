# Fer un programa que demani dos números i un operador(+,-,*,/).
# Al final, el programa ha d'imprimir per pantalla el resultat de fer l’operació que contingui la variable operador.

# Variables
number_1: float
number_2: float
operation: str
message: str

# Data (for div is necessary float, check if number and operation are correct)
number_uno: str = input("Introdueix un valor: ")
try:
    number_1 = float(number_uno)
except ValueError:
    print("No és un nombre.")
    exit()

number_two: str = input("Introdueix un valor: ")
try:
    number_2 = float(number_two)
except ValueError:
    print("No és un nombre.")
    exit()

operation = input("Introdueix una operació (+, -, *, /): ")

# Operation
match operation:
    case "+":
        message = f"{number_1} + {number_2} = {number_1 + number_2}"
    case "-":
        message = f"{number_1} - {number_2} = {number_1 - number_2}"
    case "*":
        message = f"{number_1} * {number_2} = {number_1 * number_2}"
    case "/":
        if number_2 == 0:
            message = "Error: no es pot dividir per zero."
        else:
            message = f"{number_1} / {number_2} = {number_1 / number_2}"
    case _:
        message = "Operatio no valid."

# Output
print(message)
