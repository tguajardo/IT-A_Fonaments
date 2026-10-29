"""
Comprovar si una frase introduïda per l’usuari/ària està formada només per minúscules, només per majúscules o per minúscules i majúscules.
"""


def contador_minusculas(string: str) -> int:
    minusculas: int = 0
    for char in string:
        if (
            char.islower()
        ):  # Cuenta solo minusculas, ignora numeros y signos de exclamacion
            minusculas += 1
    return minusculas


def contador_mayusculas(string: str) -> int:
    mayusculas: int = 0
    for char in string:
        if (
            char.isupper()
        ):  # Cuenta solo mayusculas, ignora numeros y signos de exclamacion
            mayusculas += 1
    return mayusculas


def main() -> None:
    frase_a_revisar: str = input("Introduzca la frase a revisar: ")
    minusculas: int = contador_minusculas(frase_a_revisar)
    mayusculas: int = contador_mayusculas(frase_a_revisar)
    if minusculas > 0 and mayusculas == 0:
        print("La frase solo tiene minusculas.")
    elif minusculas == 0 and mayusculas > 0:
        print("La frase solo tiene mayusculas.")
    elif minusculas > 0 and mayusculas > 0:
        print("La frase esta compuesta por mayusculas y minusculas.")
    else:
        print("La frase esta compuesta por caracteres no validos.")


main()
