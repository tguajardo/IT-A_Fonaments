"""Fes una funció que donades dues llistes d'elements qualsevol. Retorni una tercera llista amb els elements de les dues llistes, sense duplicats.

Per finalitzar mostra la llista resultant per pantalla.

Exemple:

llista1 = [1, 1, 2, 4, 3]

llista2 = [3, 4, 5]

resultat = [1, 2, 3, 4, 5]
"""

import random


# Testing Variables creator
def list_creator(elements_list: int, max_rand: int) -> list[int]:
    list_to_return: list[int] = []
    for __ in range(elements_list):
        list_to_return.append(random.randint(0, max_rand))
    return list_to_return


def combine(list1: list[int], list2: list[int]) -> list[int]:
    result: list[int] = []
    for element in list1:
        if element not in result:
            result.append(element)
    for element in list2:
        if element not in result:
            result.append(element)
    return result


def main():
    # Testing Variables
    # llista1: list[int] = [1, 1, 2, 4, 3]
    # llista2: list[int] = [3, 4, 5]
    # Lists created to test
    llista1: list[int] = list_creator(10, 8)
    llista2: list[int] = list_creator(15, 10)

    result: list[int] = combine(llista1, llista2)
    print(f"La lista 1 es: {llista1}")
    print(f"La lista 2 es: {llista2}")
    print(
        f"La lista resultante es: {sorted(result)}"
    )  # se agrega sorted para visualizar mejor


main()
