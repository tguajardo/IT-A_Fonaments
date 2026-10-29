"""Realitzar un programa on l’usuari/ària introdueix un número i el programa crida a un mètode que retorna el factorial del número introduït.

El factorial d'un nombre n (enter, no negatiu) és el producte de tots els nombres enters positius inferiors o iguals a n.
"""


def factorial(num: int) -> int:
    result: int = 1
    for i in range(num):
        result = result * (i + 1)
    return result


def verify_number(num_text: str) -> bool:
    try:
        if int(num_text) >= 0:
            return True
        return False
    except ValueError:
        return False


def main() -> None:
    num_factorial: int
    num_factorial_text: str = input("Introduce el número a calcular factorial: ")
    if verify_number(num_factorial_text):
        num_factorial = int(num_factorial_text)
    else:
        print("Número no valido.")
        return
    print(f"El factorial de {num_factorial} es {factorial(num_factorial)}")


main()
