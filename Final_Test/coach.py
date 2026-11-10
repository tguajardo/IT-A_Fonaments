"""
Por otra parte, cada Employee registrará su name, su dni y las contractHours. Sin embargo, no existen empleados genéricos: cada uno tendrá un rol en particular, lo que define cómo funciona su método calculateSalary(). Asumiremos un baseSalary de 1000 €.
Coach: Además del sueldo base, guardará una propiedad monthlyClasses con la cantidad de clases que tiene al mes y recibirá un plus de 40 € por cada clase impartida.
"""

from employee import Employee


class Coach(Employee):
    CLASS_COST = 40  # EUR

    def __init__(
        self, name: str, dni: str, contractHours: int, monthlyClasses: int
    ) -> None:
        super().__init__(name, dni, contractHours)
        self.__monthlyClasses = monthlyClasses

    def getMonthlyClasses(self):
        return self.__monthlyClasses

    def setMonthlyClasses(self, newValue):
        self.__monthlyClasses = newValue

    def calculateSalary(self) -> float:
        return Employee.BASE_SALARY + self.getMonthlyClasses() * self.CLASS_COST

    def __str__(self) -> str:
        return super().__str__() + f"\nClases Mensuales: {self.getMonthlyClasses()}"
