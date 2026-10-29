"""
Calculadora arcaica. El programa demana a l’usuari/ària que introdueixi dos números i l’operació que desitja realitzar.

Cada operació (suma, resta, multiplicació, divisió i mòdul) estarà programada en una funció diferent.
"""

# Variables a usar
resultado: float


# Functions
def suma(num1: float, num2: float) -> float:
    return num1 + num2


def resta(num1: float, num2: float) -> float:
    return num1 - num2


def multiplicacion(num1: float, num2: float) -> float:
    return num1 * num2


def division(num1: float, num2: float) -> float:
    return num1 / num2


def modulo(num1: float, num2: float) -> float:
    return num1 % num2


def verificar_numero(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


# Inputs
text1: str = input("Introduzca el primer número: ")
if not verificar_numero(text1):
    print("No es un número valido.")
    exit()
num1: float = float(text1)

text2: str = input("Introduzca el primer número: ")
if not verificar_numero(text2):
    print("No es un número valido.")
    exit()
num2: float = float(text2)

operacion: str = input("Introduzca la operación (+, -, *, /, %): ")

# Select Function
if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    if num2 == 0:
        print("No se puede dividir por 0.")
        exit()
    else:
        resultado = division(num1, num2)
elif operacion == "%":
    resultado = modulo(num1, num2)
else:
    print("Operación no valida")
    exit()

# Mensaje salida
print(f"La operación {num1} {operacion} {num2} es igual a {resultado}")
