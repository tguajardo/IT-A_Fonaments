"""
La aplicación debe contar con un menú interactivo en la terminal que mantenga el registro global de Gym. A través de la interfaz, el sistema debe permitir realizar estas 5 operativas:

Crear un Gym y agregarlo al sistema mediante una opción del menú. Aclaración: El sistema debe impedir que se registren dos gimnasios con el mismo nombre, mostrando un error si sucede (recuerda validar mayúsculas y minúsculas). Al crearse, el gimnasio debe inicializarse vacío, con 0 empleados y 0 miembros.

Mostrar La cantidad de empleados que hay en toda la plataforma (contando todos los gimnasios).

Calcular y mostrar El porcentaje de ocupación de un gimnasio concreto. El usuario introducirá el nombre de un gimnasio por pantalla para identificar cuál gimnasio corresponde, y se debe mostrar el porcentaje ocupado del gimnasio.

Mostrar por pantalla el nombre de los gimnasios que tengan capacidad para 200 o más personas. (Puedes mostrar una lista con los nombres)

Mostrar por pantalla el nombre de los Coach que hayan impartido al menos 20 clases. Si no hay, mostrar en pantalla: "Aún no hay profesores con +20 clases impartidas."
"""

from gym import Gym
from member import Member
from routine import Routine
from employee import Employee
from coach import Coach
from recepcionist import Recepcionist

ERRORS = {
    "empty_text": "ERROR: El valor debe ser un texto no vacío.",
    "negative_number": "ERROR: El número debe ser positivo.",
    "element_exists": "ERROR: El elemento ya existe.",
    "element_not_exists": "ERROR: El elemento no existe.",
    "invalid_int": "ERROR: Debes introducir un número entero.",
    "invalid_float": "ERROR: Debes introducir un número decimal.",
    "invalid_option": "ERROR: Opción invalida.",
    "invalid_id_doc": "ERROR: Número de identificación invalido.",
    "out_of_bound": "ERROR: Valor fuera de rango valido.",
    "invalid_length": "ERROR: Longitud incorrecta.",
}
# Variable para verificar DNI
LETRA_DNI: str = "TRWAGMYFPDXBNJZSQVHLCKE"
# DNIs Validos: 87654321X, 12345678Z, 43218765V, 56781234F, 11985806T, 88813715C


# ---------- Datos introducidos directamente en el código ----------
def crearGimnasios() -> list[Gym]:
    vivaGym = Gym("Viva Gym", "Barcelona", 300, "07:00", "23:00")
    vivaGym.addEmployee(Coach("Coach1", "12345678Z", 40, 25))
    vivaGym.addEmployee(Coach("Coach2", "11985806T", 40, 15))
    member1 = Member("43218765V", "1234567890", "name1@mail.com", 40, 1.75, 80)
    member1.addRoutine(Routine("Rutina1", 120, 6))
    vivaGym.addMember(member1)
    member2 = Member("56781234F", "0987654321", "name2@mail.com", 40, 1.75, 80)
    member2.addRoutine(Routine("Rutina2", 90, 4))
    vivaGym.addMember(member2)

    basicFit = Gym("Basic Fit", "L'Hospitalet de Llobregat", 190, "06:00", "22:00")
    basicFit.addEmployee(Recepcionist("Recepcionist1", "87654321X", 40, 12))

    return [vivaGym, basicFit]


GIMNASIOS = crearGimnasios()


# ---------- Validadores ----------
def validateDni(dni: str) -> bool:
    dni = dni.strip().upper()
    if len(dni) != 9:
        return False
    if not dni[:8].isdigit():
        return False
    if not dni[-1].isalpha():
        return False
    numero: int = int(dni[:8])
    letra: str = dni[-1]
    return letra == LETRA_DNI[numero % 23]


def notEmpty(text: str) -> bool:
    if text.strip() == "":
        print(ERRORS["empty_text"])
        return False
    return True


# ---------- Peticiones por teclado ----------
# Todas devuelven None si el dato es inválido (y ya han mostrado el error).
def requestText(prompt: str) -> str | None:
    text: str = input(f"{prompt}: ").strip()
    if not notEmpty(text):
        print(ERRORS["empty_text"])
        return None
    return text


def requestInt(prompt: str) -> int | None:
    try:
        return int(input(prompt).strip())
    except ValueError:
        print(ERRORS["invalid_int"])
        return None


def requestIntInRange(prompt: str, minimo: int, maximo: int) -> int | None:
    value = requestInt(prompt)
    if value is None:
        return None
    if value < minimo or value > maximo:
        print(ERRORS["out_of_bound"])
        return None
    return value


def requestPosFloat(prompt: str) -> float | None:
    try:
        value = float(input(prompt).strip())
    except ValueError:
        print(ERRORS["invalid_float"])
        return None
    if value <= 0:
        print(ERRORS["negative_number"])
        return None
    return value


# Busqueda de objeto
def getByName(objectList, name: str):
    for index in range(len(objectList)):
        if objectList[index].getName().strip().casefold() == name.strip().casefold():
            return objectList[index], index
    return None, -1


def getByDni(objectList: list, dni: str):
    for index in range(len(objectList)):
        if objectList[index].getDni().upper() == dni.strip().upper():
            return objectList[index], index
    return None, -1


def createGym():
    print("Datos del Gimnasio a crear\n")
    name = requestText("Nombre: ")
    city = requestText("Ciudad: ")
    capacity = requestInt("Capacidad: ")
    openingTime = requestText("Hora apertura: ")
    closingTime = requestText("Hora cierre: ")
    if None in (name, city, capacity, openingTime, closingTime):
        return
    gym, _ = getByName(GIMNASIOS, name)  # type: ignore
    if gym is not None:
        print(ERRORS["element_exists"])
        return
    print("Gimnasio creado correctamente\n")
    GIMNASIOS.append(Gym(name, city, capacity, openingTime, closingTime))  # type: ignore
    return


def showEmployees():
    print("\nEmpleados Gimnasios\n")
    for gimnasio in GIMNASIOS:
        for employee in gimnasio.getEmployees():
            print(employee)
            print()


def ocupationGym():
    name = requestText("Nombre: ")
    if name is None:
        return
    gimnasio, _ = getByName(GIMNASIOS, name)
    if gimnasio is None:
        print(ERRORS["element_exists"])
    ocupacion = len(gimnasio.getMembers()) / gimnasio.getCapacity()  # type: ignore
    print(f"\n{gimnasio.getName()} tiene una ocupacion de {ocupacion:.4f}%")  # type: ignore


def getGymOver200():
    gymsOver200 = []
    for gimnasios in GIMNASIOS:
        if gimnasios.getCapacity() >= 200:
            gymsOver200.append(gimnasios)
    print("\nGimnasios con capacidad mayor o igual a 200")
    for gym in gymsOver200:
        print(gym)


def getCoachOver20():
    print("\nEntrenadores con al menos 20 clases")
    for gimnasio in GIMNASIOS:
        for coach in gimnasio.getCoach():
            if coach.getMonthlyClasses() >= 20:
                print(coach)
                print()


def menuPrincipal():
    print("\n===== Programa Gimnasio =====")
    print("1. Crear Gimnasio")
    print("2. Mostrar Empleados")
    print("3. Ocupacion Gimnasio")
    print("4. Gimnasios con capacidad mayor a 200")
    print("5. Entrenadores con al menos 20 clases")
    print("0. Salir")


def main() -> None:
    flag = -1
    while flag != "0":
        menuPrincipal()
        flag = requestText("Introduce la opcion: ")
        match flag:
            case "1":
                createGym()
            case "2":
                showEmployees()
            case "3":
                ocupationGym()
            case "4":
                getGymOver200()
            case "5":
                getCoachOver20()
            case "0":
                print("Saliendo del programa.")
            case _:
                print(f"{ERRORS['invalid_option']}")
        print("--------------\n")


"""        # Print test
        for gimnasio in GIMNASIOS:
            print(gimnasio)"""


if __name__ == "__main__":
    main()
