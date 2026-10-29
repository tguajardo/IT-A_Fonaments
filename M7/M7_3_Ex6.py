"""Omple una llista amb 20 números random entre l'1 i el 50.

Quan estigui ple, mostra la suma de tots els seus nombres parells i la suma de tots els seus números imparells.
"""

import random

LARGO_LISTA: int = 20
MIN_RAND: int = 1
MAX_RAND: int = 50


def lista_random(Largo: int, Inicio_rango: int, Fin_rango: int) -> list[int]:
    result: list[int] = []
    for _ in range(Largo):
        result.append(random.randint(Inicio_rango, Fin_rango))
    return result


LISTA: list[int] = lista_random(LARGO_LISTA, MIN_RAND, MAX_RAND)


def suma(lista: list[int]) -> tuple[int, int]:
    pares: int = 0
    impares: int = 0
    for num in lista:
        if num % 2 == 0:
            pares += num
        else:
            impares += num
    return pares, impares


def main() -> None:
    pares, impares = suma(LISTA)
    print(f"La lista generada es {LISTA}")
    print(f"La suma de pares es: {pares}")
    print(f"La suma de impares es: {impares}")


main()
