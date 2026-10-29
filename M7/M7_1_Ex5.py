"""Mostra per pantalla els nombres parells compresos entre el 100 i el 0 en ordre descendent."""

"""Solución simple sin funciones
for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)
"""
# Variables
INICIO: int = 100
PASO: int = -1
FIN: int = 0


# Funciones
def es_par(num: int) -> bool:
    return not (num % 2)  # Alternativa return num % 2 == 0


def main() -> None:
    for num in range(INICIO, FIN - 1, PASO):
        if es_par(num):
            print(num)


main()
