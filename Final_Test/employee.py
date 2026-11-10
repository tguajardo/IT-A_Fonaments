"""
Por otra parte, cada Employee registrará su name, su dni y las contractHours. Sin embargo, no existen empleados genéricos: cada uno tendrá un rol en particular, lo que define cómo funciona su método calculateSalary(). Asumiremos un baseSalary de 1000 €.
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    BASE_SALARY = 1000  # EUR

    def __init__(self, name: str, dni: str, contractHours: int) -> None:
        self.__name: str = name
        self.__dni: str = dni
        self.__contractHours: int = contractHours

    def getDni(self):
        return self.__dni

    def getName(self):
        return self.__name

    def getContractHours(self):
        return self.__contractHours

    def setName(self, newValue):
        self.__name = newValue

    def setContractHours(self, newValue):
        self.__contractHours = newValue

    @abstractmethod
    def calculateSalary(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"DNI: {self.__dni}\n"
            f"Nombre: {self.__name}\n"
            f"Horas contratadas: {self.__contractHours}\n"
            f"Sueldo: {self.calculateSalary():.2f}"
        )
