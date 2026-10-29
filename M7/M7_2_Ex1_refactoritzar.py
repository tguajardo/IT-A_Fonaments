"""Descripció
Sabries dir que fa el programa adjunt?

Per fer-ho segurament hauries de posar algun punt de trencament (breakpoint) i avaluar el valor de les variables on es prenen decisions.
----------------------------------------------------------
Código verifica si un número es primo o no
"""


def ip():
    p = False  # Se considera por defecto que el resultado es False (NO PRIMO)
    n = int(input("escoge un número: "))  # Se pide un número

    if n > 1:  # Se analizan los casos n > 1, ya que 0 y 1 NO SON PRIMOS
        p = ep(n)  # Se cambia el resultado de acuerdo a la función ep()
    print(p)  # Muestra si el número es PRIMO (True) o NO (False)


def ep(n):
    p = True  # Se considera por defecto que el numero ES PRIMO (True)
    i = 2  # Divisor a comprobar, comenzamos en 2

    # Se revisa si el número es divisible por un número distinto a 1 y si mismo
    while p and i < n:
        if (
            n % i == 0
        ):  # Resto igual a 0, se puede dividir por otro número distinto de si mismo y 1.
            p = False  # El número NO ES PRIMO, se sale del bucle.
        i += 1  # Se cambia el divisor hasta llegar al (número - 1)
    return p  # Se indica si ES PRIMO o NO


# Se llama funcion ip()
ip()


# ----------------  REFACTORIZACIÓN----------
# Mejoramos funciones y declaración de variables


def is_prime(number: int) -> bool:
    is_prime_number: bool = False
    divisor: int = 2

    if number > 1:  # Si es 0 o 1 es NO ES PRIMO
        is_prime_number = True

    while is_prime_number and divisor < number:
        if number % divisor == 0:
            is_prime_number = False
        divisor += 1

    return is_prime_number


def main() -> None:
    numero = int(input("escoge un número: "))
    prime: bool = is_prime(numero)
    if prime:
        print(f"El número {numero} es primo.")
    else:
        print(f"El {numero} no es primo.")
    # Usando ternario
    # print(f"El númerno {numero} {"es" if prime else "no es"} primo")


main()
