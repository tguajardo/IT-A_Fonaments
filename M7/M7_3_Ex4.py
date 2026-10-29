"""L’usuari/ària ha d’introduir un DNI i el programa ha de dir si la lletra és correcte o no amb el nombre de DNI. Si la lletra no és correcta, ha de dir quina lletra és la correcta.

Per calcular la lletra DNI has de prendre el número de DNI a verificar i dividir-lo entre 23. La resta es reemplaça per una lletra que ja està assignada a aquest nombre mitjançant la taula adjunta:
RESTO: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
LETRA: T R W A G M Y F P D  X  B  N  J  Z  S  Q  V  H  L  C  K  E
"""

# Se crea la lista LETRA donde el indice corresponde al RESTO de cada letra
LETRA: str = "TRWAGMYFPDXBNJZSQVHLCKE"


def verficar_DNI(dni: str) -> bool:
    dni = dni.strip().upper()

    # Revisar formato
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit():
        return False
    if not dni[-1].isalpha():
        return False
    numero: int = int(dni[:8])
    letra: str = dni[-1]
    return letra == LETRA[numero % 23]


def main() -> None:
    dni_a_verificar: str = input("Introduce el DNI a revisar: ")
    if verficar_DNI(dni_a_verificar):
        print("El DNI introducido es valido")
    else:
        print("El DNI introducido no es valido")


main()
