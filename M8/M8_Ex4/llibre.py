class Llibre:
    def __init__(self, isbn: str, titol: str) -> None:
        # Se asume que solo existe un libro por ISBN
        self.__isbn: str = isbn
        self.__titol: str = titol
        self.__disponible: bool = True  # Libro se crea disponible

    def getIsbn(self) -> str:
        return self.__isbn

    def getTitol(self) -> str:
        return self.__titol

    def getDisponible(self) -> bool:
        return self.__disponible

    def prestar(self) -> None:
        self.__disponible = False

    def retornar(self) -> None:
        self.__disponible = True

    def __str__(self) -> str:
        state: str = "Disponible" if self.__disponible else "No disponible"
        return f"{self.__isbn} - {self.__titol}: {state}"
