"""
L'organització d'un campionat de cotxes vol gestionar escuderies, bòlids,
pilots i mecànics. L'aplicació permet donar d'alta, de baixa i veure pilots i
mecànics, i veure escuderies i bòlids (aquests últims introduïts en el codi).
"""

from helper import Helper
from escuderia import Escuderia
from cotxe import Cotxe
from treballador import Treballador
from pilots import Pilots
from mecanic import Mecanic


# ---------- Datos introducidos directamente en el código ----------
def crearEscuderias() -> list[Escuderia]:
    ferrari = Escuderia("Ferrari", 450000000.0, "Italia")
    ferrari.addCotxe(Cotxe("SF-24", 1000, 340.0, "Rojo", 15000000.0))
    ferrari.addCotxe(Cotxe("SF-23", 980, 335.0, "Rojo", 12000000.0))

    mercedes = Escuderia("Mercedes", 400000000.0, "Alemania")
    mercedes.addCotxe(Cotxe("W15", 1000, 342.0, "Plata", 14500000.0))

    redBull = Escuderia("Red Bull", 430000000.0, "Austria")
    redBull.addCotxe(Cotxe("RB20", 1050, 350.0, "Azul", 16000000.0))
    redBull.addCotxe(Cotxe("RB19", 1020, 345.0, "Azul", 13000000.0))

    return [ferrari, mercedes, redBull]


# ---------- Búsquedas auxiliares ----------
def buscarTreballador(
    escuderies: list[Escuderia], dni: str
) -> tuple[Treballador | None, Escuderia | None]:
    for escuderia in escuderies:
        treballador = escuderia.getTreballador(dni)
        if treballador is not None:
            return treballador, escuderia
    return None, None


# ---------- Menú ----------
def mostrarMenu() -> None:
    print("\n===== CAMPEONATO DE COCHES =====")
    print("1. Ver escuderías")
    print("2. Ver bólidos")
    print("3. Ver pilotos")
    print("4. Ver mecánicos")
    print("5. Alta de piloto")
    print("6. Alta de mecánico")
    print("7. Baja de trabajador")
    print("0. Salir")


# ---------- Opciones de visualización ----------
def verEscuderias(escuderies: list[Escuderia]) -> None:
    for escuderia in escuderies:
        print(escuderia)


def verBolidos(escuderies: list[Escuderia]) -> None:
    for escuderia in escuderies:
        for cotxe in escuderia.getCotxes():
            print(cotxe)


def verPilotos(escuderies: list[Escuderia]) -> None:
    hayPilotos: bool = False
    for escuderia in escuderies:
        for piloto in escuderia.getPilots():
            print(f"[{escuderia.getNombre()}] {piloto}")
            hayPilotos = True
    if not hayPilotos:
        print("No hay pilotos registrados.")


def verMecanicos(escuderies: list[Escuderia]) -> None:
    hayMecanicos: bool = False
    for escuderia in escuderies:
        for mecanico in escuderia.getMecanic():
            print(f"[{escuderia.getNombre()}] {mecanico}")
            hayMecanicos = True
    if not hayMecanicos:
        print("No hay mecánicos registrados.")


# ---------- Altas y bajas ----------
def pedirDatosComunes(
    escuderies: list[Escuderia],
) -> tuple[Escuderia, str, str, str, int, int] | None:
    """Pide los datos que comparten pilotos y mecánicos. Devuelve None si algún dato es inválido."""
    nombreEscuderia = Helper.requestText("Escudería")
    if nombreEscuderia is None:
        return None
    escuderia, _ = Helper.getByName(escuderies, nombreEscuderia)
    if escuderia is None:
        print(Helper.ERRORS["element_not_exists"])
        return None

    dni = Helper.requestText("DNI")
    if dni is None:
        return None
    dni = dni.upper()
    if not Helper.validateDni(dni):
        print(Helper.ERRORS["invalid_id_doc"])
        return None
    existente, _ = buscarTreballador(escuderies, dni)
    if existente is not None:
        print(Helper.ERRORS["element_exists"])
        return None

    nombre = Helper.requestText("Nombre")
    if nombre is None:
        return None
    apellido = Helper.requestText("Primer apellido")
    if apellido is None:
        return None

    edad = Helper.requestIntInRange("Edad (16-99): ", 16, 99)
    if edad is None:
        return None
    antiguedad = Helper.requestIntInRange(
        "Antigüedad en la escudería (años): ", 0, edad
    )
    if antiguedad is None:
        return None

    return escuderia, dni, nombre, apellido, edad, antiguedad


def altaPilot(escuderies: list[Escuderia]) -> None:
    datos = pedirDatosComunes(escuderies)
    if datos is None:
        return
    escuderia, dni, nombre, apellido, edad, antiguedad = datos

    altura = Helper.requestPosFloat("Altura (m): ")
    if altura is None:
        return
    peso = Helper.requestPosFloat("Peso (kg): ")
    if peso is None:
        return

    escuderia.addTreballador(
        Pilots(dni, nombre, apellido, edad, antiguedad, altura, peso)
    )
    print("Piloto dado de alta correctamente.")


def altaMecanic(escuderies: list[Escuderia]) -> None:
    datos = pedirDatosComunes(escuderies)
    if datos is None:
        return
    escuderia, dni, nombre, apellido, edad, antiguedad = datos

    estudios = Helper.requestYesNo("¿Tiene estudios superiores de mecánica? (S/N): ")
    if estudios is None:
        return

    escuderia.addTreballador(Mecanic(dni, nombre, apellido, edad, antiguedad, estudios))
    print("Mecánico dado de alta correctamente.")


def baixaTreballador(escuderies: list[Escuderia]) -> None:
    dni = Helper.requestText("DNI del trabajador a dar de baja")
    if dni is None:
        return
    dni = dni.upper()

    treballador, escuderia = buscarTreballador(escuderies, dni)
    if treballador is None or escuderia is None:
        print(Helper.ERRORS["element_not_exists"])
        return

    escuderia.delTreballador(treballador)
    print("Trabajador dado de baja correctamente.")


# ---------- Programa principal ----------
def main() -> None:
    escuderies: list[Escuderia] = crearEscuderias()
    opcion: int | None = -1

    while opcion != 0:
        mostrarMenu()
        opcion = Helper.requestInt("Elige una opción: ")

        if opcion == 1:
            verEscuderias(escuderies)
        elif opcion == 2:
            verBolidos(escuderies)
        elif opcion == 3:
            verPilotos(escuderies)
        elif opcion == 4:
            verMecanicos(escuderies)
        elif opcion == 5:
            altaPilot(escuderies)
        elif opcion == 6:
            altaMecanic(escuderies)
        elif opcion == 7:
            baixaTreballador(escuderies)
        elif opcion == 0:
            print("¡Hasta pronto!")
        elif opcion is not None:
            print(Helper.ERRORS["invalid_option"])


if __name__ == "__main__":
    main()
