"""Tots els edificis tindran certes dades comunes (nom, número de plantes, superfície (m²)) que es donaran en crear l’edifici i no es modificaran, però sí que s’haurà de poder accedir a elles per llegir-les.

Es crearà un mètode netejar() en la classe adient, la qual mostrarà per pantalla el temps que s’ha trigat a netejar l’edifici, tenint en compte que es triga a netejar un minut per cada 5 m². A més, si un edifici té més d’una planta, es triga a pujar mig minut d’una planta a una altra. Per tant, afegirem mig minut per cada planta addicional. Per cada minut de feina es pagarà un euro diari. A més, com que es neteja cada dia, per obtenir el cost mensual, haurem de multiplicar per 30 (aquest cost mensual també es mostrarà per pantalla)

A més, s’implementarà un mètode anomenat calcularCostVigilancia() que mostrarà el que costa al mes contractar vigilants a cada edifici. Es considera que cada vigilant d’hotel o hospital pot vigilar 1000 m². Per tant, si un edifici té una superfície de 5500 m², necessitarem 6 vigilants. En canvi, els vigilants dels cinemes poden vigilar 3000 m². Contractar cada vigilant costa als propietaris de l’edifici 1.300 euros mensuals, però els vigilants d’hotels cobren un plus de perillositat de 500 euros mensuals.
"""

from abc import ABC, abstractmethod


class Edifici(ABC):

    # Constants privades
    __AREA_X_MINUTE: float = 5.0  # m^2 / min
    __FLOOR_MOVE_TIME: float = 0.5  # min
    __PAY_X_MINUTE: float = 1.0  # EUR / min
    __SECURITY_AREA: float = 1000  # m^2
    __SECURITY_SALARY: float = 1300  # EUR
    __DANGER_BONUS: float = 500  # EUR

    def __init__(self, name: str, floors: int, area: float) -> None:
        self.__name = name
        self.__floors = floors
        self.__area = area

    # Getters propiedades
    def getName(self) -> str:
        return self.__name

    def getFloors(self) -> int:
        return self.__floors

    def getArea(self) -> float:
        return self.__area

    # Getters propiedades estaticas privadas de la clase
    @classmethod
    def getAreaXMinute(cls) -> float:
        return cls.__AREA_X_MINUTE

    @classmethod
    def getFloorMoveTime(cls) -> float:
        return cls.__FLOOR_MOVE_TIME

    @classmethod
    def getPayXMinute(cls) -> float:
        return cls.__PAY_X_MINUTE

    @classmethod
    def getSecurityArea(cls) -> float:
        return cls.__SECURITY_AREA

    @classmethod
    def getSecuritySalary(cls) -> float:
        return cls.__SECURITY_SALARY

    @classmethod
    def getDangerBonus(cls) -> float:
        return cls.__DANGER_BONUS

    # Función netejar() -> devuelve tiempo de limpieza diario y costo mensual limpieza
    def netejar(self) -> tuple[float, float]:
        dailyCleaningTime = self.getArea() / Edifici.getAreaXMinute()
        dailyCleaningTime += (self.getFloors() - 1) * Edifici.getFloorMoveTime()
        monthlyCleanCost = 30 * dailyCleaningTime * Edifici.getPayXMinute()
        return dailyCleaningTime, monthlyCleanCost

    # Función abstracta, existira en todas las clases hijas, pero se calcula de forma particular en cada una
    @abstractmethod
    def calcularCostVigilancia(self) -> tuple[int, float]:
        pass

    # toString()
    def __str__(self) -> str:
        time, cost = self.netejar()
        return (
            f"Nombre: {self.getName()}\n"
            f"Pisos: {self.getFloors()}\n"
            f"Superfície: {self.getArea():.2f} m²\n"
            f"Tiempo limpieza diaria: {time:.2f} min\n"
            f"Costo limpieza mensual: {cost:.2f} EUR"
        )
