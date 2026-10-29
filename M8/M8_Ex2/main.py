"""Ens demanen crear una aplicació per donar d’alta, modificar, veure i eliminar hotels.

La classe hotel haurà de tenir els següents atributs: nom, nombre d’habitacions, nombre de plantes i superfície total de l’hotel. Com a mètodes només haurà de tenir els getters i setters propis de la classe i un mètode anomenat calcularManteniment(). Aquest mètode ha de tenir en compte que cada persona del servei pot atendre 20 habitacions i haurà de mostrar quantes persones són necessàries per atendre el servei d’habitacions de l’hotel i quin és el cost total destinat al servei sabent que aquestes persones cobren 1.500 € al mes.
"""

# Importar clase necesaria
from hotel import Hotel

# Crear constantes
HOTELES: list[Hotel] = []  # Lista de los distintos objetos Hotel
ERRORS = {
    "empty_text": "ERROR: El valor debe ser un texto no vacío.",
    "negative_number": "ERROR: El número debe ser positivo.",
    "element_exists": "ERROR: El elemento ya existe.",
    "element_not_exists": "ERROR: El elemento no existe.",
    "invalid_int": "ERROR: Debes introducir un número entero.",
    "invalid_float": "ERROR: Debes introducir un número decimal.",
    "invalid_option": "ERROR: Opción invalida.",
}
# Hoteles de prueba
HOTELES.append(Hotel("Ritz", 60, 8, 4000.0))
HOTELES.append(Hotel("Tudor", 100, 15, 40000.0))
HOTELES.append(Hotel("5Stars", 20, 20, 20000.0))


# Metodos generales
# Verificar si hotel existe en la lista
def hotel_exists(hotel_to_check: str) -> bool:
    for hotel in HOTELES:
        if hotel_to_check.casefold() == hotel.name.casefold():
            return True
    return False


# Obtener la posición de un hotel en la lista
def get_hotel(hotel_to_pos: str) -> Hotel | None:
    for hotel in HOTELES:
        if hotel_to_pos.casefold() == hotel.name.casefold():
            return hotel
    return None


def get_valid_int(message: str) -> int:
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print(ERRORS["negative_number"])
        except ValueError:
            print(ERRORS["invalid_int"])


def get_valid_float(message: str) -> float:
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print(ERRORS["negative_number"])
        except ValueError:
            print(ERRORS["invalid_float"])


"""La funció crearHotel() haurà de demanar a l’usuari/a que introdueixi per pantalla les dades de nom, nombre d’habitacions, nombre de plantes i superfície total de l’hotel (o haurà de rebre aquestes dades per paràmetre). Un cop hagi demanat totes aquestes dades, s’ha d’instanciar l’objecte de la classe i afegir-lo a un array d’hotels.
"""


def crearHotel() -> None:
    # Solicitar variables
    print("\n-------Crear Hotel-------")
    name: str = input("Nombre: ").strip()
    if name == "":
        print(f"{ERRORS["empty_text"]}\n")
        return
    if hotel_exists(name):
        print(f"{ERRORS['element_exists']}\n")
        return

    rooms: int = get_valid_int("Habitaciones: ")
    floors: int = get_valid_int("Pisos: ")
    area: float = get_valid_float("Superficie (m^2): ")

    HOTELES.append(Hotel(name, rooms, floors, area))
    print(f"\nHotel creado correctamente.\n")
    print(HOTELES[-1])


""" #Prueba funcion crearHotel()
crearHotel()
crearHotel()
for hotel in HOTELES:
    print("--------------------------")
    print(hotel)
"""

"""La funció donarDeBaixaHotel() haurà de rebre el nom de l'hotel que es vol donar de baixa. L’usuari/ària introduirà el nom de l’hotel i si l’hotel està dintre de l’array, l’eliminarem i mostrarem un missatge per pantalla informant l’usuari/ària que hem eliminat l’hotel. Si no hem trobat l’hotel dintre de l’array, avisarem l’usuari/ària dient que l’hotel no estava dintre de la nostra aplicació.
"""


def donarDeBaixaHotel() -> None:
    hotel_to_delete_name: str = input("Introduce el nombre del hotel a eliminar: ")
    hotel_to_delete = get_hotel(hotel_to_delete_name)

    if hotel_to_delete == None:
        print(f"\n{ERRORS['element_not_exists']}\n")
        return

    # print(f"Hotel Encontrado\n")
    # print(f"{hotel_to_delete}\n")
    HOTELES.remove(hotel_to_delete)
    print(f"Hotel Borrado\n")


""" # Prueba funcion donarDeBaixaHotel()
donarDeBaixaHotel()

for hotel in HOTELES:
    print(f"{hotel}\n")
"""

"""La funció veureHotel() haurà de rebre el nom de l'hotel que vol que mostrem per pantalla, si l’hotel està a la nostra aplicació, li mostrarem l’hotel, si no hi és, informarem l’usuari/ària dient que l’hotel que ens ha demanat no està dintre de la nostra aplicació.
Quan mostrem l’hotel, a més, de mostrar el nombre d’habitacions, nombre de plantes i superfície total de l’hotel també es cridarà al mètode calcularManteniment().
"""


def veureHotel() -> None:
    hotel_to_see_name: str = input("Introduce el nombre del hotel a ver: ")
    hotel_to_see = get_hotel(hotel_to_see_name)

    if hotel_to_see == None:
        print(f"\n{ERRORS['element_not_exists']}\n")
        return

    print(f"Hotel Encontrado\n")
    print(f"{hotel_to_see}\n")


# veureHotel()


"""
La funció modificarHotel() haurà de rebre el nom de l'hotel que volem modificar. L’usuari/ària introduirà el nom de l’hotel. Si el tenim a l’aplicació, li demanarem si vol modificar el nombre d’habitacions, el nombre de plantes o la superfície total de l’hotel. Farem la modificació pertinent i avisarem a l’usuari/ària que la modificació s’ha realitzat.
"""


def modificarHotel() -> None:
    hotel_to_modify_name: str = input("Introduce el nombre del hotel a modificar: ")
    hotel_to_modify = get_hotel(hotel_to_modify_name)
    print(f"\n{hotel_to_modify}\n")
    if hotel_to_modify == None:
        print(f"\n{ERRORS['element_not_exists']}\n")
        return
    flag: str = ""
    while flag != "0":
        print(f"\n-------Modificar {hotel_to_modify.name}-------")
        print("-------Opciones-------\n")
        print("1. Número de habitaciones.")
        print("2. Número de pisos.")
        print("3. Superficie hotel m^2.")
        print("0. Salir")
        print("--------------")
        flag = input("Introduce la opción: ").strip()
        match flag:
            case "1":
                print(f"Valor actual: {hotel_to_modify.rooms}")
                hotel_to_modify.rooms = int(input("Ingresar nuevo valor: "))
            case "2":
                print(f"Valor actual: {hotel_to_modify.floors}")
                hotel_to_modify.floors = int(input("Ingresar nuevo valor: "))
            case "3":
                print(f"Valor actual: {hotel_to_modify.area}")
                hotel_to_modify.area = float(input("Ingresar nuevo valor: "))
            case "0":
                print("Saliendo menu modificar.")
            case _:
                print(f"{ERRORS['invalid_option']}")
    print("Valor modificado.\n")
    print(hotel_to_modify)


# modificarHotel()


def main() -> None:
    flag: str = ""
    while flag != "0":
        print(f"\n-------Gestión de hoteles-------")
        print("-------Opciones-------\n")
        print("1. Crear Hotel.")
        print("2. Eliminar Hotel")
        print("3. Ver Hotel")
        print("4. Modificar Hotel")
        print("0. Salir")
        print("--------------")
        flag = input("Introduce la opción: ").strip()
        match flag:
            case "1":
                crearHotel()
            case "2":
                donarDeBaixaHotel()
            case "3":
                veureHotel()
            case "4":
                modificarHotel()
            case "0":
                print("Saliendo del programa.")
            case _:
                print(f"{ERRORS['invalid_option']}")


main()
