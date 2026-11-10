"""
Por otra parte, cada Employee registrará su name, su dni y las contractHours. Sin embargo, no existen empleados genéricos: cada uno tendrá un rol en particular, lo que define cómo funciona su método calculateSalary(). Asumiremos un baseSalary de 1000 €.
Receptionist: Además del sueldo base. Guardará una propiedad overtimeHours con sus horas extra, por las que cobrará 30 € extra (cada una). Y si tiene más de 10 horas extra, se agregará un bono de 100 € más.
"""

from employee import Employee


class Recepcionist(Employee):
    OT_COST = 40  # EUR
    OT_BONUS = 100  # EUR

    def __init__(
        self, name: str, dni: str, contractHours: int, overtimeHours: int
    ) -> None:
        super().__init__(name, dni, contractHours)
        self.__overtimeHoures: int = overtimeHours

    def getOvertimeHours(self) -> int:
        return self.__overtimeHoures

    def setOvertimeHours(self, newValue) -> None:
        self.__overtimeHoures = newValue

    def calculateSalary(self) -> float:
        return (
            Employee.BASE_SALARY
            + self.getOvertimeHours() * self.OT_COST
            + (self.OT_BONUS if self.getOvertimeHours() > 10 else 0)
        )

    def __str__(self) -> str:
        return (
            super().__str__() + f"\nHoras Extras Mensuales: {self.getOvertimeHours()}"
        )
