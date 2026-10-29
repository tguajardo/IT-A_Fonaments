import random


def array_generator() -> list[str]:
    available_seats = []
    seats = ["A", "B", "C", "D", "E", "F"]

    for row in range(1, 21):
        random_seat_1 = random.randrange(len(seats))
        random_seat_2 = random.randrange(len(seats))

        available_seats.append(f"{row}-{seats[random_seat_1]}")
        if random_seat_1 != random_seat_2:
            available_seats.append(f"{row}-{seats[random_seat_2]}")

    return available_seats


PASSENGERS: list[str | int] = [
    "Aina",
    1,
    "Bruno",
    18,
    "Carla",
    3,
    "Diego",
    6,
    "Elisa",
    4,
    "Ferran",
    2,
    "Gina",
    11,
    "Hugo",
    17,
    "Irene",
    1,
    "Joan",
    18,
    "Karla",
    3,
    "Luis",
    6,
    "Marta",
    4,
    "Nico",
    12,
    "Olga",
    5,
    "Pau",
    7,
    "Quim",
    11,
    "Rosa",
    8,
    "Sergi",
    2,
    "Tania",
    4,
]

# CONSTANTS
DEBUG: bool = True  # Cambiar a False, para eliminar mensajes de ayuda
AVAILABLE_SEATS: list[str] = array_generator()
MAX_FILAS: str = "20"
POSICION: list[str] = ["A", "B", "C", "D", "E", "F"]
VALOR_RESERVAR: int = 5
FILAS_EMERGENCIA: list[int] = [2, 11, 18]
if DEBUG:
    print(AVAILABLE_SEATS)

"""Deberás crear la función `assign-seat()`, que tendrá como objetivo:

- Pedir un número (fila-posición) de asiento deseado.
- Comprobar si el asiento deseado está dentro de la lista de asientos disponibles.
- Actualizar la lista según el caso (Explicado a continuación).
- Registrar el dinero recaudado por la reserva de asientos.
- Mostrar un mensaje de respuesta al usuario."""


def assign_seat(lista_disponibles: list[str]) -> list[str]:
    print("Programa para asignar asientos disponibles")
    print()
    disponibles = lista_disponibles
    asignados: list[str] = []
    recaudacion: int = 0
    while True:
        if len(disponibles) == 0:
            break
        asiento_a_reservar: str = obtener_asiento()
        if asiento_a_reservar == "salir":
            break
        if asiento_a_reservar in disponibles:
            disponibles.remove(asiento_a_reservar)
            asignados.append(asiento_a_reservar)
            recaudacion += VALOR_RESERVAR
        else:
            print(f"El asiento {asiento_a_reservar} no esta disponible.")
            continue
    print()
    print(f"Los asientos reservados son: {asignados}")
    print()
    print(f"Los asientos disponibles son: {disponibles}")
    print()
    print(f"El dinero recaudado es ${recaudacion}")
    return asignados


def verificar_asiento(fila: str) -> bool:
    try:
        return int(fila) <= 21 and int(fila) > 0
    except ValueError:
        return False


def verificar_posicion(posicion: str) -> bool:
    if posicion in POSICION:
        return True
    return False


def obtener_asiento() -> str:
    while True:
        asiento: str = input(
            f'Ingresar asiento (Escribir "salir" para terminar el programa): '
        ).upper()
        if asiento.lower() == "salir":
            return "salir"
        fila_posicion: list[str] = asiento.split("-")
        if not verificar_asiento(fila_posicion[0]) or not verificar_posicion(
            fila_posicion[1]
        ):
            print("El asiento se debe ingresar en formato NUMERO-POSICIÓN")
            print(
                f"NUMERO es un valor entre [1, {MAX_FILAS}] y POSICIÓN una letra {POSICION}"
            )
            continue
        return asiento


def windows_seats(asientos_usados: list[str]) -> None:
    asientos_ventanilla: int = 0
    asientos_pasillo: int = 0
    for asiento in asientos_usados:
        if asiento[2] == "A" or asiento[2] == "F":
            asientos_ventanilla += 1
        elif asiento[2] == "C" or asiento[2] == "D":
            asientos_pasillo += 1
    print(f"Se asignaron {asientos_ventanilla} asientos de ventanilla.")
    print(f"Se asignaron {asientos_pasillo} asientos de pasillo")
    if asientos_pasillo < asientos_ventanilla:
        print("Se prefieren los asientos en ventanilla")
    elif asientos_pasillo > asientos_ventanilla:
        print("se prefieren los asientos en pasillo")
    else:
        print("No existe preferencia")


def emergency_exit(lista_pasajeros: list[str | int]) -> None:
    pasajeros_en_ee: list[str] = obtener_pasajeros_ee(lista_pasajeros)
    pasajeros_en_ee.sort()
    pasajeros_en_ee_mayus: list[str] = []
    for pasajero in pasajeros_en_ee:
        pasajeros_en_ee_mayus.append(pasajero.upper())
    print(f"{";".join(pasajeros_en_ee_mayus)}")


def obtener_pasajeros_ee(lista_pasajeros: list[str | int]) -> list[str]:
    result: list[str] = []
    for index in range(0, len(lista_pasajeros), 2):

        nombre: str = lista_pasajeros[index]  # type: ignore
        fila: int = lista_pasajeros[index + 1]  # type: ignore
        if fila in FILAS_EMERGENCIA:
            result.append(nombre)
    return result


def main() -> None:
    print("Bienvenidos a aerolineas IT Academy")
    print()
    if DEBUG:
        print("Problema 1")
        print()
    asientos_reservados: list[str] = assign_seat(AVAILABLE_SEATS)
    print()
    if DEBUG:
        print("Problema 2")
        print()
    windows_seats(asientos_reservados)
    print()
    if DEBUG:
        print("Problema 3")
        print()
    emergency_exit(PASSENGERS)


main()
