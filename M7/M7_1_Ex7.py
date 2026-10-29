"""Fer un programa on l’usuari/ària introdueix per pantalla un caràcter i un número. El programa imprimeix per pantalla un quadrat amb la mida i el caràcter introduïts per l’usuari/ària."""


def verificar_numero(num_text: str) -> bool:
    try:
        if int(num_text) < 1:
            return False
        return True
    except ValueError:
        return False


def verificar_char(CHAR: str) -> bool:
    if len(CHAR) == 1:
        return True
    else:
        return False


def main() -> None:
    # Inputs
    char: str = input("Introduce el caracter a imprimir: ")
    if not verificar_char(char):
        print("Ingresar solo UN caracter.")
        return
    size_text: str = input("Introduce el lado del cuadrado: ")
    if verificar_numero(size_text):
        size: int = int(size_text)
    else:
        print("El lado debe ser un número entero mayor a 1.")
        return
    for __ in range(size):
        print(f"{char*size}")


main()
