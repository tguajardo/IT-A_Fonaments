"""Crea un programa on l’usuari/ària introdueix tres notes i el programa calculi la mitja.

Si la mitja és inferior a 5 ha de mostrar el següent missatge per pantalla: “No has superat el curs. Has de recuperar”.

Si la mitja està entre 5 i 7 ha de mostrar: “Enhorabona! Has aprovat, però hauries de continuar practicant”.

Si la mitja és superior a 7 ha de mostrar: "Enhorabona! Has superat el curs! Passa ja al següent nivell!"
"""

# Variables
NOTAS_A_PEDIR: int = 3


def verificar_numero(num_text: str) -> bool:
    try:
        int(num_text)
        return True
    except ValueError:
        return False


def verificar_nota(nota: int) -> bool:
    if nota < 1 or nota > 10:
        return False
    else:
        return True


def calcula_promedio() -> float:
    suma_notas: int = 0
    for i in range(NOTAS_A_PEDIR):
        while True:
            nota_text: str = input(f"Introdueix la nota {i + 1}: ")
            if verificar_numero(nota_text):
                nota = int(nota_text)
                if verificar_nota(nota):
                    suma_notas += nota
                    break
                else:
                    print("La nota ha d'estar entre 1 i 10.")
            else:
                print("La nota ha d'estar entre 1 i 10.")

    return suma_notas / NOTAS_A_PEDIR


def mensaje(promedio: float) -> None:
    if promedio < 5:
        print("No has superat el curs. Has de recuperar.")
    elif promedio <= 7:
        print("Enhorabona! Has aprovat, però hauries de continuar practicant")
    else:
        print("Enhorabona! Has superat el curs! Passa ja al següent nivell!")


def main() -> None:
    print("Calculadora de la mitjana de tres notes\n")
    promedio: float = calcula_promedio()
    print(f"La mitjana és: {promedio:.2f}")
    mensaje(promedio)


main()
