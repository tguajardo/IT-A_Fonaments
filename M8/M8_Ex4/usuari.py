from llibre import Llibre


class Usuari:
    def __init__(self, nom: str, cognom: str, dni: str):
        self.__nom: str = nom
        self.__cognom: str = cognom
        self.__dni: str = dni
        self.__llibres: list[Llibre] = []

    def getNom(self) -> str:
        return self.__nom

    def getCognom(self) -> str:
        return self.__cognom

    def getDni(self) -> str:
        return self.__dni

    def getLlibres(self) -> list[Llibre]:
        return self.__llibres

    def setNom(self, newValue: str) -> None:
        self.__nom = newValue

    def setCognom(self, newValue: str) -> None:
        self.__cognom = newValue

    def setDNI(self, newValue: str) -> None:
        self.__dni = newValue

    def prestar(self, llibre: Llibre):
        if not llibre.getDisponible():
            raise ValueError("El libro no esta disponible.")
        self.__llibres.append(llibre)  # Se agrega libro a la lista del usuario
        llibre.prestar()  # Se cambia el estado del libro (False)

    def retornar(self, llibre: Llibre):
        if llibre not in self.__llibres:
            raise ValueError("El usuario no tiene prestado el libro.")
        self.__llibres.remove(llibre)  # Se remueve libre de la lista del usuario
        llibre.retornar()  # Se cambia el estado del libre (True)

    def __str__(self):
        return (
            f"Usuario: {self.__nom} {self.__cognom} - {self.__dni}\n"
            f"Tiene {len(self.__llibres)} libros"
        )
