from cuenta import Cuenta


class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str) -> None:
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__dni: str = dni
        self.__accounts: list[Cuenta] = []

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getDni(self):
        return self.__dni

    def getAccounts(self):
        return self.__accounts

    def setNombre(self, newValue: str):
        self.__nombre = newValue

    def setApellido(self, newValue: str):
        self.__apellido = newValue

    def setDni(self, newValue: str):
        self.__dni = newValue

    def addAccount(self, newAccount: Cuenta):
        self.__accounts.append(newAccount)

    def __str__(self) -> str:
        return (
            f"Nombre: {self.__nombre}\n"
            f"Apellido: {self.__apellido}\n"
            f"DNI: {self.__dni}\n"
            f"Cuentas: {len(self.__accounts)}"
        )
