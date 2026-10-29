"""L’usuari/ària ha d'introduir un número i el programa ha de mostrar per pantalla si el número és parell o imparell."""


def es_par(num: int) -> bool:
    return not (num % 2)  # Alternativa return num % 2 == 0


def verificar_numero(num_text: str) -> bool:
    try:
        int(num_text)
        return True
    except ValueError:
        return False


def main() -> None:
    num_text: str = input("Introducir número a revisar: ")
    if verificar_numero(num_text):
        num = int(num_text)
    else:
        print("Introducir un número entero valido.")
        exit()
    if es_par(num):
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")


main()
