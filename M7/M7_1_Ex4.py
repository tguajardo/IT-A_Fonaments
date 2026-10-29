"""L’usuari/ària ha d’introduir dos números, el programa retornarà “Un dels dos números és negatiu”, només si un dels dos números és negatiu."""

# Funciones


def verificar_numero(num_text: str) -> bool:
    try:
        float(num_text)
        return True
    except ValueError:
        return False


def numero_negativo(num1: float, num2: float):
    return num1 < 0 or num2 < 0


def main() -> None:
    num1_text: str = input("Introduce el primer número: ")
    num2_text: str = input("Introduce el segundo número: ")
    if not verificar_numero(num1_text) or not verificar_numero(num2_text):
        print("Debes introducir números.")
        return
    num1: float = float(num1_text)
    num2: float = float(num2_text)
    if numero_negativo(num1, num2):
        print("Uno de los números es negativo.")
    else:
        print("Ninguno de los números es negativo.")


main()
