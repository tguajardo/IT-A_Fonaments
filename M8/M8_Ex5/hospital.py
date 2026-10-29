"""A més, s’implementarà un mètode anomenat calcularCostVigilancia() que mostrarà el que costa al mes contractar vigilants a cada edifici. Es considera que cada vigilant d’hotel o hospital pot vigilar 1000 m². Per tant, si un edifici té una superfície de 5500 m², necessitarem 6 vigilants. En canvi, els vigilants dels cinemes poden vigilar 3000 m². Contractar cada vigilant costa als propietaris de l’edifici 1.300 euros mensuals, però els vigilants d’hotels cobren un plus de perillositat de 500 euros mensuals.

A l’hospital es reparteix dinar pels malalts tres vegades al dia. Hi haurà un mètode repartirDinar() en el lloc adient que mostrarà, quan sigui cridat, el missatge “S’estan repartint xxx racions”. Aquest número pot variar al llarg del temps, i, per tant, s’haurà de permetre accedir a l’atribut corresponent, tant per llegir-lo com per modificar-lo, encara que no es faci directament.
"""

from edifici import Edifici
import math


class Hospital(Edifici):
    SECURITY_AREA: float = Edifici.getSecurityArea()
    SECURITY_SALARY: float = Edifici.getSecuritySalary()

    def __init__(self, name: str, floors: int, area: float, patients: int) -> None:
        super().__init__(name, floors, area)
        self.__patients: int = patients

    def getPatients(self) -> int:
        return self.__patients

    def setPatients(self, newValue: int) -> None:
        self.__patients = newValue

    def calcularCostVigilancia(self) -> tuple[int, float]:
        guards = math.ceil(self.getArea() / self.getSecurityArea())
        cost = guards * self.getSecuritySalary()
        return guards, cost

    def repartirDinar(self) -> str:
        return f"S’estan repartint {self.getPatients() * 3} racions"

    def __str__(self):
        guards, guardsCost = self.calcularCostVigilancia()
        return (
            f"{super().__str__()}\n"
            f"Pacientes actuales: {self.getPatients()}\n"
            f"Numero de vigilantes: {guards}\n"
            f"Coste vigilancia mensual: {guardsCost:.2f} EUR\n"
        )
