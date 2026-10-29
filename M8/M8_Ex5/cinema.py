"""A més, s’implementarà un mètode anomenat calcularCostVigilancia() que mostrarà el que costa al mes contractar vigilants a cada edifici. Es considera que cada vigilant d’hotel o hospital pot vigilar 1000 m². Per tant, si un edifici té una superfície de 5500 m², necessitarem 6 vigilants. En canvi, els vigilants dels cinemes poden vigilar 3000 m². Contractar cada vigilant costa als propietaris de l’edifici 1.300 euros mensuals, però els vigilants d’hotels cobren un plus de perillositat de 500 euros mensuals.

Al cinema es crearà la funció projectarSessio(), que mostrarà el missatge “S’han recaptat xxx.xx euros”, tenint en compte que, per calcular la recaptació, s’ha de multiplicar el preu d’una entrada pel número d’assistents a la sessió, que no podrà superar l’aforament màxim. Per tant, el mètode projectarSessió haurà de rebre com a paràmetres el número d’assistents i el preu de l’entrada per aquella sessió. El número d’assistents a la sessió no pot ser més gran que l’aforament total de la sala.
"""

from edifici import Edifici
import math


class Cinema(Edifici):
    __SECURITY_SALARY: float = Edifici.getSecuritySalary()
    __SECURITY_AREA: float = 3000  # m^2

    def __init__(self, name: str, floors: int, area: float, capacity: int) -> None:
        super().__init__(name, floors, area)
        self.__capacity: int = capacity

    def getCapacity(self) -> int:
        return self.__capacity

    # La capacidad no cambia (facilmente), pero es importante poder actualizarla en caso de renovaciones u otras obras.
    def setCapacity(self, newValue: int) -> None:
        self.__capacity = newValue

    # Getters propiedades estaticas privadas de la clase
    @classmethod
    def getSecurityArea(cls) -> float:
        return cls.__SECURITY_AREA

    @classmethod
    def getSecuritySalary(cls) -> float:
        return cls.__SECURITY_SALARY

    # Funciones clase
    def calcularCostVigilancia(self) -> tuple[int, float]:
        guards = math.ceil(self.getArea() / self.getSecurityArea())
        cost = guards * self.getSecuritySalary()
        return guards, cost

    def projectarSessio(self, ticketPrice: float, atendees: int) -> str:
        if atendees > self.getCapacity():
            return f"El número de asistentes ({atendees}) supera la capacidad de ({self.getCapacity()}) la sala."
        return f"S’han receptat {atendees*ticketPrice:.2f} EUR"

    # toString()
    def __str__(self) -> str:
        guards, guardsCost = self.calcularCostVigilancia()
        revenueSessio: str = self.projectarSessio(9.5, 10)
        return (
            f"{super().__str__()}\n"
            f"Capacidad sala: {self.getCapacity()}\n"
            f"Numero de vigilantes: {guards}\n"
            f"Coste vigilancia mensual: {guardsCost:.2f} EUR\n"
            f"{revenueSessio}"
        )
