"""
De cada Member queremos guardar su dni, creditCard, email, age, height y weight. El dni se podrá leer, pero no modificar directamente desde fuera de la clase. El creditCard, en cambio, se podrá modificar, pero al leerla, solo se deben mostrar los ultimos 4 numeros. También tendrá una rutina principal. De cada Routine se guardara un title, su duration y la cantidad de exercises.
"""

from routine import Routine


class Member:
    def __init__(
        self,
        dni: str,
        creditCard: str,
        email: str,
        age: int,
        height: float,
        weight: float,
    ) -> None:
        self.__dni = dni
        self.__creditCard = creditCard
        self.__email = email
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__routine: Routine

    def getDni(self):
        return self.__dni

    def getCreditCard(self):
        creditCardToShow = self.__creditCard[-4:]
        return creditCardToShow

    def getEmail(self):
        return self.__email

    def getAge(self):
        return self.__age

    def getHeight(self):
        return self.__height

    def getWeight(self):
        return self.__weight

    def getRoutine(self):
        return self.__routine

    def setCreditCard(self, newValue):
        self.__creditCard = newValue

    def setEmail(self, newValue):
        self.__email = newValue

    def setAge(self, newValue):
        self.__age = newValue

    def setHeight(self, newValue):
        self.__height = newValue

    def setWeight(self, newValue):
        self.__weight = newValue

    def addRoutine(self, newRoutine: Routine):
        self.__routine = newRoutine

    def __str__(self) -> str:
        return (
            f"DNI Socio: {self.__dni} | Tarjeta: {self.getCreditCard()} | Correo: {self.__email}\n"
            f"Edad: {self.__age} | Estatura: {self.__height} m | Peso: {self.__weight} kg\n"
            f"{self.__routine}"
        )
