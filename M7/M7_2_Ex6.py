"""L’usuari/ària ha d’introduir números fins que introdueixi un nombre primer.

En el moment que l’usuari/ària introdueixi un nombre primer, el programa ha de treure per pantalla el següent missatge: “Exacte, el número “x” és primer!”
"""


def is_prime(number: int) -> bool:
    is_prime_number: bool = False
    divisor: int = 2

    if number > 1:  # Si es 0 o 1 es NO ES PRIMO
        is_prime_number = True  # Se cambia el valor para el bucle siguiente
    # El while verifica que no se haya encontrado otro divisor y que se prueben solo los divisores menores al número
    while is_prime_number and divisor < number:
        if number % divisor == 0:
            is_prime_number = False
        divisor += 1

    return is_prime_number


def verify_number(num_text: str) -> bool:
    try:
        if int(num_text) >= 0:
            return True
        return False
    except ValueError:
        return False


def main() -> None:
    prime_number: int
    number_to_check_text: str = input("Introdueix un número: ")
    while True:
        if verify_number(number_to_check_text):
            number_to_check = int(number_to_check_text)
        else:
            print("Introdueix un número enter positiu valid.")
            pass
        if is_prime(number_to_check):
            prime_number = number_to_check
            break
        else:
            number_to_check_text = input(
                f"{number_to_check} no és primer. Introdueix un altre número:   "
            )
    print(f"Exacte, el número {prime_number} és primer!")


main()
