"""
En nuestra aplicación, trabajaremos con una lista global de gimnasios. De cada Gym nos interesa guardar: name, city, capacity, openingTime, closingTime, su lista de empleados y su lista de socios.
Al crearse, el gimnasio debe inicializarse vacío, con 0 empleados y 0 miembros.
"""

from employee import Employee
from coach import Coach
from recepcionist import Recepcionist
from member import Member


class Gym:
    def __init__(
        self,
        name: str,
        city: str,
        capacity: int,
        openingTime: str,
        closingTime: str,
    ) -> None:
        self.__name: str = name
        self.__city: str = city
        self.__capacity: int = capacity
        self.__openingTime: str = openingTime
        self.__closingTime: str = closingTime
        self.__employees: list[Employee] = []
        self.__members: list[Member] = []

    def getName(self):
        return self.__name

    def getCity(self):
        return self.__city

    def getCapacity(self):
        return self.__capacity

    def getOpeningTime(self):
        return self.__openingTime

    def getClosingTime(self):
        return self.__closingTime

    def getEmployees(self):
        return list(self.__employees)

    def getMembers(self):
        return list(self.__members)

    def setName(self, newValue):
        self.__name = newValue

    def setCapacity(self, newValue):
        self.__capacity = newValue

    def setOpeningTime(self, newValue):
        self.__openingTime = newValue

    def setClosingTime(self, newValue):
        self.__closingTime = newValue

    def getMember(self, dni: str) -> Member | None:
        for index in range(len(self.__members)):
            if self.__members[index].getDni().casefold() == dni.strip().casefold():
                return self.__members[index]
        return None

    # Deberia hacer uso de la comprobación de arriba, pero se deja en Main()
    def addMember(self, newMember: Member):
        self.__members.append(newMember)

    # Metodos de empleados
    def getCoach(self) -> list[Coach]:
        coaches: list[Coach] = []
        for e in self.__employees:
            if isinstance(e, Coach):
                coaches.append(e)
        return coaches

    def getRecepcionist(self) -> list[Recepcionist]:
        recepcionists: list[Recepcionist] = []
        for e in self.__employees:
            if isinstance(e, Recepcionist):
                recepcionists.append(e)
        return recepcionists

    def getEmployee(self, dni: str) -> Employee | None:
        for index in range(len(self.__employees)):
            if self.__employees[index].getDni().casefold() == dni.strip().casefold():
                return self.__employees[index]
        return None

    # Deberia hacer uso de la comprobación de arriba, pero se deja en Main()
    def addEmployee(self, newEmployee: Employee) -> None:
        self.__employees.append(newEmployee)

    def delEmployee(self, notEmployee: Employee) -> None:
        self.__employees.remove(notEmployee)

    # toString()
    def __str__(self) -> str:
        # Información del gimnasio
        text = "\n--------------------------------------------------\n"
        text += f"Nombre Gimnasio: {self.__name}\n"
        text += f"Ciudad Gimnasio: {self.__city}\n"
        text += f"Capacidad Gimnasio: {self.__capacity}\n"
        text += f"Horario: {self.__openingTime} - {self.__closingTime}\n"
        # + Empleados (coachs y recepcionists)
        text += f"+++++++++\nEntrenadores\n"
        coachs = self.getCoach()
        if len(coachs) == 0:
            text += "(SIN ENTRENADORES)\n"
        for c in coachs:
            text += f"{c}\n"
        text += f"+++++++++\nRecepcionistas\n"
        recepcionists = self.getRecepcionist()
        if len(recepcionists) == 0:
            text += "(SIN Recepcionistas)\n"
        for r in recepcionists:
            text += f"{r}\n"
        text += f"+++++++++\nSocios\n"
        if len(self.__members) == 0:
            text += "SIN SOCIOS\n"
        for m in self.__members:
            text += f"{m}\n"
        text += "--------------------------------------------------\n"
        return text
