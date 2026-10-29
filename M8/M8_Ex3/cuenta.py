class Cuenta:
    def __init__(self, numCuenta: int) -> None:
        self.__numCuenta: int = numCuenta
        self.__saldo: int = 0

    def getNumCuenta(self) -> int:
        return self.__numCuenta

    def getSaldo(self) -> int:
        return self.__saldo

    def ingresar(self, amount: int) -> bool:
        if amount <= 0:
            return False
        self.__saldo += amount
        return True

    def retirar(self, amount: int) -> bool:
        if amount > self.__saldo or amount <= 0:
            return False
        self.__saldo -= amount
        return True

    def __str__(self):
        return f"Cuenta n°: {self.__numCuenta}\n" f"Saldo: {self.__saldo} EUR"
