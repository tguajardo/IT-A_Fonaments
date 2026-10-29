"""Un/a professor/a vol calcular les mitges de les notes de tota la classe. Crea una aplicació on l'usuari/ària introduirà un número per pantalla (el número correspon al nombre de notes que vol introduir) i el programa li demanarà que introdueixi les notes de tots els/les alumnes.

Un cop les notes han sigut introduïdes, el programa retorna el següent:

Si la nota mitjana és menor que 5: "La nota mitjana de la classe està suspesa. Els/les alumnes haurien de preguntar els seus dubtes i treballar més".

Si la nota és inferior a 7: "La nota mitjana de la classe és bona, però els/les alumnes haurien de millorar el treball personal".

Per la resta de casos, el missatge ha de ser: "Enhorabona! La nota mitjana de la classe es correspon amb l'esforç realitzat".
"""


# Functions
def verificar_numero(num_text: str) -> bool:
    try:
        int(num_text)
        return True
    except ValueError:
        return False


def verificar_nota(nota: int) -> bool:
    if nota < 0 or nota > 10:
        return False
    else:
        return True


def calcula_promedio(numero_notas: int) -> float:
    suma_notas: int = 0
    for i in range(numero_notas):
        while True:
            nota_text: str = input(f"Introdueix la nota {i + 1}: ")
            if verificar_numero(nota_text):
                nota = int(nota_text)
                if verificar_nota(nota):
                    suma_notas += nota
                    break
                else:
                    print("La nota ha d'estar entre 0 i 10.")
            else:
                print("La nota ha d'estar entre 0 i 10.")

    return suma_notas / numero_notas


def mensaje(promedio: float) -> None:
    if promedio < 5:
        print(
            "La nota mitjana de la classe està suspesa. Els/les alumnes haurien de preguntar els seus dubtes i treballar més."
        )
    elif promedio <= 7:
        print(
            "La nota mitjana de la classe és bona, però els/les alumnes haurien de millorar el treball personal"
        )
    else:
        print(
            "Enhorabona! La nota mitjana de la classe es correspon amb l'esforç realitzat"
        )


def main() -> None:
    print("Calculadora de la mitjana de notes\n")
    notas_text: str = input("Notes ha introduir: ")
    if verificar_numero(notas_text):
        notas_a_promediar: int = int(notas_text)
        if notas_a_promediar < 1:
            print("Número de notes te que ser major a 0.")
            exit()
    else:
        print("Has d'introduir un número vàlid.")
        exit()
    promedio: float = calcula_promedio(notas_a_promediar)
    print(f"La mitjana és: {promedio:.2f}")
    mensaje(promedio)


main()
