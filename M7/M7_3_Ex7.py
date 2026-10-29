"""Intersecció de dues llistes. Troba els elements comuns entre dues llistes i guarda'ls en una llista nova. La llista resultant no ha de tenir duplicats.

Exemple:

Per aquestes dues llistes: llista1 = [1, 2, 3, 3, 4, 5], llista2 = [3, 4, 6, 7, 5]

El resultat és: resultat = [3, 4, 5]"""

import random

LARGO_LISTA: int = 6
MIN_RAND: int = 1
MAX_RAND: int = 10


def lista_random(Largo: int, Inicio_rango: int, Fin_rango: int) -> list[int]:
    result: list[int] = []
    for _ in range(Largo):
        result.append(random.randint(Inicio_rango, Fin_rango))
    return result


LISTA1: list[int] = lista_random(LARGO_LISTA, MIN_RAND, MAX_RAND)
LISTA2: list[int] = lista_random(LARGO_LISTA, MIN_RAND, MAX_RAND)


def intersection(lista1: list[int], lista2: list[int]) -> list[int]:
    result: list[int] = []
    for element in lista1:
        if element in lista2 and element not in result:
            result.append(element)
    return result


def main() -> None:
    interseccion: list[int] = intersection(LISTA1, LISTA2)

    print(f"Lista 1 es: {LISTA1}")
    print(f"Lista 2 es: {LISTA2}")
    print(f"Y su interseccion es: {interseccion}")


main()
