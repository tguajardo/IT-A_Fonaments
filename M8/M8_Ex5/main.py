"""La ciutat de Barcelona, com qualsevol ciutat, està formada per un nombre molt gran d’edificis. Hi ha moltes classes d’edificis: edificis d’habitatges, hospitals, escoles, blocs d’apartaments, blocs d’oficines, hotels, cinemes, etc.

L’exercici proposat consistirà a crear una aplicació que contindrà una classe Edifici i diverses classes derivades. No s’instanciarà cap objecte de la classe Edifici, sinó que s’instanciaran objectes de les classes derivades d’aquesta.  Les classes derivades són: Hotel, Hospital i Cinema.

Tots els edificis tindran certes dades comunes (nom, número de plantes, superfície (m²)) que es donaran en crear l’edifici i no es modificaran, però sí que s’haurà de poder accedir a elles per llegir-les.

Es crearà un mètode netejar() en la classe adient, la qual mostrarà per pantalla el temps que s’ha trigat a netejar l’edifici, tenint en compte que es triga a netejar un minut per cada 5 m². A més, si un edifici té més d’una planta, es triga a pujar mig minut d’una planta a una altra. Per tant, afegirem mig minut per cada planta addicional. Per cada minut de feina es pagarà un euro diari. A més, com que es neteja cada dia, per obtenir el cost mensual, haurem de multiplicar per 30 (aquest cost mensual també es mostrarà per pantalla)

A més, s’implementarà un mètode anomenat calcularCostVigilancia() que mostrarà el que costa al mes contractar vigilants a cada edifici. Es considera que cada vigilant d’hotel o hospital pot vigilar 1000 m². Per tant, si un edifici té una superfície de 5500 m², necessitarem 6 vigilants. En canvi, els vigilants dels cinemes poden vigilar 3000 m². Contractar cada vigilant costa als propietaris de l’edifici 1.300 euros mensuals, però els vigilants d’hotels cobren un plus de perillositat de 500 euros mensuals.

A l’hospital es reparteix dinar pels malalts tres vegades al dia. Hi haurà un mètode repartirDinar() en el lloc adient que mostrarà, quan sigui cridat, el missatge “S’estan repartint xxx racions”. Aquest número pot variar al llarg del temps, i, per tant, s’haurà de permetre accedir a l’atribut corresponent, tant per llegir-lo com per modificar-lo, encara que no es faci directament.

Al cinema es crearà la funció projectarSessio(), que mostrarà el missatge “S’han recaptat xxx.xx euros”, tenint en compte que, per calcular la recaptació, s’ha de multiplicar el preu d’una entrada pel número d’assistents a la sessió, que no podrà superar l’aforament màxim. Per tant, el mètode projectarSessió haurà de rebre com a paràmetres el número d’assistents i el preu de l’entrada per aquella sessió. El número d’assistents a la sessió no pot ser més gran que l’aforament total de la sala.

En els hotels cada dia passa el servei d’habitacions. Es calcula que cada membre del servei pot atendre 20 habitacions. Es crearà un mètode que calculi, i mostri per pantalla: a) Quantes persones són necessàries per atendre el servei d’habitacions l’hotel. b) Quin és el total necessari per als sous d’aquestes persones, tenint en compte que cada persona cobra 1.000 euros al mes.

Exemples: L’”Hospital de Vilafranca”, de 1.950 m² i 2 plantes. En aquest moment té 26 malalts.  L’”Hospital General de Catalunya”, de 25.350 m² i 10 plantes. En aquest moment té 315 malalts.  El “Cinema Montecarlo”, de  3180 m² i 1 planta.  El “Cinema Principal”, de 12.450 m² i 2 plantes.  L’”Hotel Hilton”, de 73.858 m² i 22 plantes. Té 583 habitacions.  L’”Hotel Pepita”, de 593 m² i 3 plantes. Té 12 habitacions.

L'aplicació ha de ser capaç de donar d'alta, mostrar i eliminar edificis. Al cridar la funció mostrar, cridarem a tots els mètodes de l'edifici en qüestió per veure totes les seves dades per pantalla.
"""

from hospital import Hospital
from cinema import Cinema
from hotel import Hotel
from helper import Helper

# Listas de edificios
HOSPITALES: list[Hospital] = []
CINEMAS: list[Cinema] = []
HOTELES: list[Hotel] = []


def getEdificiData(prompt: str):
    print(prompt)
    nameEdifici: str | None = Helper.getPrompt("Nombre: ")
    floorsEdifici: int | None = Helper.requestInt("Pisos: ")
    areaEdifici: float | None = Helper.requestFloat("Area: ")
    if nameEdifici is None or floorsEdifici is None or areaEdifici is None:
        return None, None, None
    return nameEdifici, floorsEdifici, areaEdifici


# Funciones crear edificio
def createCinema() -> None:
    nameCinema, floorsCinema, areaCinema = getEdificiData(
        "\nInformación de Cinema a crear: "
    )
    capacityCinema: int | None = Helper.requestInt("Capacidad: ")
    # Revisar si algún atributo esta incorrecto
    if None in (nameCinema, floorsCinema, areaCinema, capacityCinema):
        print("Datos inválidos.\nNo se crea el edificio.")
        return
    else:
        # Revisar duplicados
        obj, idx = Helper.getByName(CINEMAS, nameCinema)  # type: ignore nameCinema es un str por if
        if obj is not None:
            print(f"{Helper.ERRORS["element_exists"]}\nNo se crea el edificio")
            return
    cine: Cinema = Cinema(nameCinema, floorsCinema, areaCinema, capacityCinema)  # type: ignore
    CINEMAS.append(cine)
    print("Cinema creado correctamente.")
    return


def createHospital() -> None:
    nameHospital, floorsHospital, areaHospital = getEdificiData(
        "\nInformación de Hospital a crear: "
    )
    patientsHospital: int | None = Helper.requestInt("Pacientes: ")
    if None in (nameHospital, floorsHospital, areaHospital, patientsHospital):
        print("Datos inválidos.\nNo se crea el edificio.")
        return
    else:
        # Revisar duplicados
        obj, idx = Helper.getByName(HOSPITALES, nameHospital)  # type: ignore nameHospital es un str por if
        if obj is not None:
            print(f"{Helper.ERRORS["element_exists"]}\nNo se crea el edificio")
            return
    hospital: Hospital = Hospital(
        nameHospital, floorsHospital, areaHospital, patientsHospital  # type: ignore
    )
    HOSPITALES.append(hospital)
    print("Hospital creado correctamente.")
    return


def createHotel():
    nameHotel, floorsHotel, areaHotel = getEdificiData(
        "\nInformación de Hotel a crear: "
    )
    roomsHotel: int | None = Helper.requestInt("Habitaciones: ")
    if None in (nameHotel, floorsHotel, areaHotel, roomsHotel):
        print("Datos inválidos.\nNo se crea el edificio.")
        return
    else:
        # Revisar duplicados
        obj, idx = Helper.getByName(HOTELES, nameHotel)  # type: ignore nameHotel es un str por if
        if obj is not None:
            print(f"{Helper.ERRORS["element_exists"]}\nNo se crea el edificio")
            return
    hotel: Hotel = Hotel(nameHotel, floorsHotel, areaHotel, roomsHotel)  # type: ignore
    HOTELES.append(hotel)
    print("Hotel creado correctamente.")
    return


def mostrarCinema():
    if CINEMAS == []:
        print("No hay cinemas creados.")
        return
    print("----Lista Cinemas----\n")
    for cine in CINEMAS:
        print(cine)
        print("--------------\n")
    return


def mostrarHospital():
    print("----Lista Hospitales----\n")
    for hospital in HOSPITALES:
        print(hospital)
        print("--------------\n")
    return


def mostrarHotel():
    print("----Lista Hoteles----\n")
    for hotel in HOTELES:
        print(hotel)
        print("---------------------")
    return


def deleteCinema() -> None:
    cinemaNameToDelete: str | None = Helper.getPrompt("Nombre del Cinema: ")
    if cinemaNameToDelete is None:
        return
    cinemaToDelete, _ = Helper.getByName(CINEMAS, cinemaNameToDelete)  # type: ignore
    if cinemaToDelete is None:
        print(Helper.ERRORS["element_not_exists"])
        return
    CINEMAS.remove(cinemaToDelete)
    print("Cinema eliminado correctamente.")
    return


def deleteHospital():
    hospitalNameToDelete: str | None = Helper.getPrompt("Nombre del Hospital: ")
    if hospitalNameToDelete is None:
        return
    hospitalToDelete, _ = Helper.getByName(HOSPITALES, hospitalNameToDelete)  # type: ignore
    if hospitalToDelete is None:
        print(Helper.ERRORS["element_not_exists"])
        return
    HOSPITALES.remove(hospitalToDelete)
    print("Hospital eliminado correctamente.")


def deleteHotel():
    hotelNameToDelete: str | None = Helper.getPrompt("Nombre del hotel: ")
    if hotelNameToDelete is None:
        return
    hotelToDelete, _ = Helper.getByName(Hoteles, hotelNameToDelete)  # type: ignore
    if hotelToDelete is None:
        print(Helper.ERRORS["element_not_exists"])
        return
    HOTELES.remove(hotelToDelete)
    print("Hotel eliminado correctamente.")


# Funciones menu
def createEdifici() -> None:
    # Menu que indica que tipo de edificio se va a crear
    buildType: str = ""
    while buildType != "0":
        print("\n----Tipo de edificio a crear----\n")
        print("1. Cinema.")
        print("2. Hospital.")
        print("3. Hotel.")
        print("0. Volver a menu principal.")
        print("--------------\n")
        buildType = input("Introduce la opción: ").strip()
        match buildType:
            case "1":
                createCinema()
            case "2":
                createHospital()
            case "3":
                createHotel()
            case "0":
                print("Volviendo al menu principal.")
            case _:
                print(f"{Helper.ERRORS['invalid_option']}")
    return


def mostrarEdifici():
    # Menu que indica que tipo de edificio se va a mostrar
    buildType: str = ""
    while buildType != "0":
        print("\n----Tipo de edificio a mostrar----\n")
        print("1. Cinema.")
        print("2. Hospital.")
        print("3. Hotel.")
        print("0. Volver a menu principal.")
        print("--------------\n")
        buildType = input("Introduce la opción: ").strip()
        match buildType:
            case "1":
                mostrarCinema()
            case "2":
                mostrarHospital()
            case "3":
                mostrarHotel()
            case "0":
                print("Volviendo al menu principal.")
            case _:
                print(f"{Helper.ERRORS['invalid_option']}")
    return


def deleteEdifici():
    # Menu que indica que tipo de edificio se va a eliminar
    buildType: str = ""
    while buildType != "0":
        print("\n----Tipo de edificio a eliminar----\n")
        print("1. Cinema.")
        print("2. Hospital.")
        print("3. Hotel.")
        print("0. Volver a menu principal.")
        print("--------------\n")
        buildType = input("Introduce la opción: ").strip()
        match buildType:
            case "1":
                deleteCinema()
            case "2":
                deleteHospital()
            case "3":
                deleteHotel()
            case "0":
                print("Volviendo al menu principal.")
            case _:
                print(f"{Helper.ERRORS['invalid_option']}")
    return


# Main menu
def main() -> None:
    flag: str = ""
    while flag != "0":
        print(f"\n-------Gestión de Edificios-------")
        print("-------Opciones-------\n")
        print("1. Crear Edificio.")
        print("2. Ver Edificios.")
        print("3. Eliminar Edificios.")
        print("0. Salir")
        print("--------------")
        flag = input("Introduce la opción: ").strip()
        match flag:
            case "1":
                createEdifici()
            case "2":
                mostrarEdifici()
            case "3":
                deleteEdifici()
            case "0":
                print("Saliendo del programa.")
            case _:
                print(f"{Helper.ERRORS['invalid_option']}")
        print("--------------\n")


if __name__ == "__main__":
    main()
