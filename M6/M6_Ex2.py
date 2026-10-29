"""
Aquest programa calcula l'edat mitjana d'un número de persones introduït per teclat.

S'ha de crear una funció que s'encarregui de demanar les edats a l'usuari/ària i de calcular l'edat mitjana.


La funció rebrà per paràmetre el núm. de persones a qui ha de demanar l'edat.
L'edat de les persones només serà vàlida si està compresa entre 0 i 120 anys.
La mitjana de les edats introduïdes s'ha de retornar per la funció (return).
"""


def calcula_promedio(personas: int) -> float:
    suma_edades: int = 0
    for i in range(personas):
        while True:
            edad_text: str = input(f"Introducir la edad de la persona {i +1}: ")
            if verifica_numero(edad_text):
                edad: int = int(edad_text)
                if verifica_edad(edad):
                    suma_edades += edad
                    break
                else:
                    print("La edad debe estar entre 0 y 120.")
            else:
                print("La edad debe ser un número entero entre 0 y 120")
    return suma_edades / personas


def verifica_numero(text_num: str) -> bool:
    try:
        int(text_num)
        return True
    except ValueError:
        return False


def verifica_edad(edad: int) -> bool:
    if edad >= 0 and edad <= 120:
        return True
    else:
        return False


# Programa principal
# Input
personas_text: str = input("Número de personas a calcular el promedio: ")

# Validación
if verifica_numero(personas_text):
    personas: int = int(personas_text)
else:
    print("Introducir un número entero")
    exit()
if personas < 1:
    print("El número de personas debe ser un número positivo")
    exit()

# Calculo y mensaje
promedio: float = calcula_promedio(personas)
print(f"La edad promedio es: {promedio}")
