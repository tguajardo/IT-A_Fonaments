"""Volen saber de cada escuderia que participa en el campionat, el nom, el pressupost que tenen i el país d’origen. Cada escuderia pot tenir més d’un cotxe i de cadascun volen saber la potència, la velocitat màxima, el color i el preu de mercat."""

"""
Estructura Escuderia
Escuderia:  nombre, presupuesto y país de origen.
            Tiene varios coches y varios trabajadores.
"""

from cotxe import Cotxe
from treballador import Treballador
from pilots import Pilots
from mecanic import Mecanic
from helper import Helper


class Escuderia:
    def __init__(self, nombre: str, presupuesto: float, pais: str) -> None:
        self.__nombre: str = nombre
        self.__presupuesto: float = presupuesto
        self.__pais: str = pais
        self.__cotxes: list[Cotxe] = []
        self.__treballadores: list[Treballador] = []  # Lista unica de trabajadores

    # Getters
    def getNombre(self) -> str:
        return self.__nombre

    def getPresupuesto(self) -> float:
        return self.__presupuesto

    def getPais(self) -> str:
        return self.__pais

    def getCotxes(self) -> list[Cotxe]:
        return list(self.__cotxes)

    def getTreballadores(self) -> list[Treballador]:
        return list(self.__treballadores)

    # A partir de la lista unica recuperamos pilotos y mecanicos
    def getPilots(self) -> list[Pilots]:
        pilots: list[Pilots] = []
        for t in self.__treballadores:
            if isinstance(t, Pilots):
                pilots.append(t)
        return pilots

    def getMecanic(self) -> list[Mecanic]:
        mecanic: list[Mecanic] = []
        for t in self.__treballadores:
            if isinstance(t, Mecanic):
                mecanic.append(t)
        return mecanic

    # Cotxe
    def addCotxe(self, cotxe: Cotxe) -> None:
        cotxe.setNombreEscuderia(self.__nombre)
        self.__cotxes.append(cotxe)

    # Treballadores
    def getTreballador(self, dni: str):
        treballador, _ = Helper.getByDni(self.__treballadores, dni)
        return treballador

    def addTreballador(self, newTreballador: Treballador) -> None:
        self.__treballadores.append(newTreballador)

    def delTreballador(self, notTreballador: Treballador) -> None:
        self.__treballadores.remove(notTreballador)

    # toString()
    def __str__(self) -> str:
        # Información de la escuderia
        text = "\n--------------------------------------------------\n"
        text += f"{self.__nombre} de {self.__pais} con presupuesto de {self.__presupuesto:.2f} Eur\n"
        # + cotxes de la escuderia
        text += f"+++++++++\nCoches\n"
        if len(self.__cotxes) == 0:
            text += "(SIN COCHES)\n"
        for c in self.__cotxes:
            text += f"{c}\n"
        # + treballadores de la escuderia (pilotos, mecanicos)
        text += f"+++++++++\nPilotos\n"
        pilots = self.getPilots()
        if len(pilots) == 0:
            text += "(SIN PILOTOS)\n"
        for p in pilots:
            text += f"{p}\n"
        text += f"+++++++++\nMecanicos\n"
        mecanics = self.getMecanic()
        if len(mecanics) == 0:
            text += "(SIN MECANICOS)\n"
        for m in mecanics:
            text += f"{m}\n"
        text += "--------------------------------------------------\n"
        return text
