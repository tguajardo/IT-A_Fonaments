"""Realitzar un programa que tingui un menú on se li mostraran 4 opcions a l’usuari/ària per pantalla:

1.- Quadrat (costat*costat)

2.- Triangle (base*altura/2)

3.- Rectangle (alto*amplada)

4.- Cercle (radi*radi*pi())

0.- Sortir del programa

Segons l’opció escollida haurà d’introduir unes dades o altres perquè el programa mostri per pantalla l’àrea (el valor) del polígon escollit.
"""

import math


def verificar_medida(num_text: str) -> bool:
    try:
        return float(num_text) > 0
    except ValueError:
        return False


def area_quadrat(costat: float) -> float:
    return costat * costat


def area_triangle(base: float, altura: float) -> float:
    return base * altura / 2


def area_rectangle(amplada: float, altura: float) -> float:
    return amplada * altura


def area_cercle(radi: float) -> float:
    return radi * radi * math.pi


def menu() -> None:
    print("\n-----------------------")
    print("Menu Opciones")
    print("1.- Quadrat")
    print("2.- Triangle")
    print("3.- Rectangle")
    print("4.- Cercle")
    print("0.- Sortir del programa")
    print("-----------------------\n")


def main() -> None:
    while True:
        menu()
        option: str = input("Escull una opcio: ")
        match option:
            case "0":
                print("Sortint del programa. Adeu!!")
                break

            case "1":
                side_text: str = input("Introdueix la longitud del costat: ")
                if not verificar_medida(side_text):
                    print("La longitud ha de ser un número positiu.")
                    continue
                print(f"Area del quadrat: {area_quadrat(float(side_text)):.2f}")

            case "2":
                base_text: str = input("Introdueix la base del triangle: ")
                altura_text: str = input("Introdueix l'altura del triangle: ")
                if not (verificar_medida(base_text) and verificar_medida(altura_text)):
                    print("Les mesures han de ser un número positiu.")
                    continue
                print(
                    f"Area del triangle: {area_triangle(float(base_text),float(altura_text)):.2f}"
                )

            case "3":
                amplada_text = input("Introdueix l'amplada del rectangle: ")
                altura_text = input("Introdueix l'altura del rectangle: ")
                if not (
                    verificar_medida(amplada_text) and verificar_medida(altura_text)
                ):
                    print("Les mesures han de ser un número positiu.")
                    continue
                print(
                    f"Area del rectangle: {area_rectangle(float(amplada_text),float(altura_text)):.2f}"
                )

            case "4":
                radi_text = input("Introdueix el radi del cercle: ")
                if not (verificar_medida(radi_text)):
                    print("El radi ha de ser un número positiu.")
                    continue
                print(f"Area del cercle: {area_cercle(float(radi_text)):.2f}")

            case _:
                print("Opcio no valida. Torna-ho a intentar.")


main()
