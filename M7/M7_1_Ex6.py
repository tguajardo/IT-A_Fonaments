"""Taula de multiplicar.

L’usuari/ària introduirà un número (de l'1 al 10) per pantalla, i utilitzant un bucle, el programa li mostrarà la taula de multiplicar d’aquell número.
"""


# Functions
def verificar_numero(num_text: str) -> bool:
    try:
        num: int = int(num_text)
        return num > 0 and num < 10
    except ValueError:
        return False


def tabla(num: int) -> None:
    for i in range(10):
        print(f"{num} x {i + 1} = {num * (i + 1)}")
    return


def main() -> None:
    num_text: str = input("Introduce un número (1-10): ")

    if not verificar_numero(num_text):
        print("Debes introducir un número entre 1 y 10.")
        return

    num: int = int(num_text)
    tabla(num)


main()
