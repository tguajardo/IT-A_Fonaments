"""En un altre fitxer anomenat main.py, crea la funció crearOrdinadors().

Demana a l'usuari/ària les dades de dos ordinadors.

Un cop introduïdes les dades dels dos ordinadors, crida als mètodes de la classe Ordinador per comprovar que funcionen correctament.
"""

from ordinador import Ordinador


def get_number(message: str) -> int:
    # En este caso se ocupa para RAM y Disco duro (enteros positivos)
    while True:
        try:
            valor: int = int(input(message))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor a 0")
        except ValueError:
            print("El valor debe ser un número entero")


def get_ordinador(num: int) -> Ordinador:
    print(f"\nA continuación ingresa las caracteristicas del ordenador[{num}]")
    marca: str = input("Marca: ")
    model: str = input("Model: ")
    proce: str = input("Procesador: ")
    ram: int = get_number("RAM (en GB): ")
    disco_duro: int = get_number("Disco duro (en GB, 1TB = 1000GB): ")
    return Ordinador(marca, model, proce, ram, disco_duro)


def main() -> None:
    # crear ordenadores
    ordenadores: list[Ordinador] = [get_ordinador(i + 1) for i in range(2)]
    for ordinador in ordenadores:
        print("------------------------------\n")
        print("Revisando Getters\n")
        print(f"Marca: {ordinador.marca}")
        print(f"Model: {ordinador.model}")
        print(f"Procesador: {ordinador.proce}")
        print(f"RAM: {ordinador.ram}GB")
        print(f"Disco Duro: {ordinador.disco_duro}GB")
        print("------------------------------\n")
        print("Revisando funcion 'executar'\n")
        ordinador.executar("Internet Explorer 4.0")
        print("------------------------------\n")
        print("Ejecutando Setters\n")
        ordinador.proce = "Intel Core i9"
        ordinador.ram = 32
        ordinador.disco_duro = 2000
        print("------------------------------\n")
        print("Ejecutando toString\n")
        print(ordinador.toString())


main()
