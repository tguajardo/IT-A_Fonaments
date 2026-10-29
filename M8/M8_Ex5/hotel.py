"""A més, s’implementarà un mètode anomenat calcularCostVigilancia() que mostrarà el que costa al mes contractar vigilants a cada edifici. Es considera que cada vigilant d’hotel o hospital pot vigilar 1000 m². Per tant, si un edifici té una superfície de 5500 m², necessitarem 6 vigilants. En canvi, els vigilants dels cinemes poden vigilar 3000 m². Contractar cada vigilant costa als propietaris de l’edifici 1.300 euros mensuals, però els vigilants d’hotels cobren un plus de perillositat de 500 euros mensuals.

En els hotels cada dia passa el servei d’habitacions. Es calcula que cada membre del servei pot atendre 20 habitacions. Es crearà un mètode que calculi, i mostri per pantalla: a) Quantes persones són necessàries per atendre el servei d’habitacions l’hotel. b) Quin és el total necessari per als sous d’aquestes persones, tenint en compte que cada persona cobra 1.000 euros al mes.
"""

import math
from edifici import Edifici


class Hotel(Edifici):
    # A pesar que mantienen los valores de la clase Edifici, se dejan estipulados en la funcion para su facil modificacion futura
    __SECURITY_SALARY: float = Edifici.getSecuritySalary()
    __SECURITY_AREA: float = Edifici.getSecurityArea()
    __BONUS_DANGER: float = Edifici.getDangerBonus()

    def __init__(self, name: str, floors: int, area: float, rooms: int) -> None:
        super().__init__(name, floors, area)
        self.__rooms = rooms

    # Getters propiedades
    def getRooms(self) -> int:
        return self.__rooms

    # Se crea un setter pensando en que por reformas o trabajos, cambie el numero de cuartos del hotel
    def setRooms(self, newValue: int) -> None:
        self.__rooms = newValue

    # Getters propiedades estaticas privadas de la clase
    @classmethod
    def getSecurityArea(cls) -> float:
        return cls.__SECURITY_AREA

    @classmethod
    def getBonusDanger(cls) -> float:
        return cls.__BONUS_DANGER

    @classmethod
    def getSecuritySalary(cls) -> float:
        return cls.__SECURITY_SALARY

    def calcularCostVigilancia(self) -> tuple[int, float]:
        guards = math.ceil(self.getArea() / self.getSecurityArea())
        cost = guards * (self.getSecuritySalary() + self.getBonusDanger())
        return guards, cost

    # toString()
    def __str__(self) -> str:
        guards, cost = self.calcularCostVigilancia()
        return (
            f"{super().__str__()}\n"
            f"Habitaciones: {self.getRooms()}\n"
            f"Vigilantes necesarios: {guards}\n"
            f"Coste vigilancia mensual: {cost:.2f} EUR"
        )
