"""Fes un programa que mostri el següent per pantalla:

* * * * * *

* * * * *

* * * *

* * *

* *

*

El nombre de línies formades per “*” vindrà donat per un número que l’usuari/ària introduirà per consola.
"""

# Constants
CHAR_TO_PRINT: str = "*"


def print_lines(lines: int) -> None:
    for line in range(lines, 0, -1):
        print(CHAR_TO_PRINT * (line))


def verificar_numero(NUM_TEXT: str) -> bool:
    try:
        if int(NUM_TEXT) > 0:
            return True
        return False
    except ValueError:
        return False


def main() -> None:
    # Input
    lines_to_print_text: str = input("Introduce la cantidad de lineas a imprimir: ")
    if verificar_numero(lines_to_print_text):
        lines_to_print: int = int(lines_to_print_text)
    else:
        print("Ingresar un número entero mayor a 0.")
        return
    print_lines(lines_to_print)


main()
