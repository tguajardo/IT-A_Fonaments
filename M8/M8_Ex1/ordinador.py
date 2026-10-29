"""Crea una classe en Python anomenada "Ordinador", en un fitxer anomenat ordinador.py

Aquesta classe tindrà com a atributs la marca, el model, el processador, la quantitat de memòria RAM i la capacitat del disc dur.

A més del constructor, ha de disposar dels següents mètodes:

Mètodes que permetin consultar cadascun dels atributs (getters).
Mètodes que permetin modificar el processador, la quantitat de memòria ram i la capacitat del disc dur. (setters).
Un mètode que rebrà un paràmetre i retornarà una frase que digui:
"En aquests moments s'està executant: 'X'" (X és el paràmetre rebut pel mètode i que normalment serà el nom d'un programa).
Exemple: "En aquests moments s'està executant: Chrome"
Un mètode que retornarà una descripció completa de l'ordinador (toString()).
"""


class Ordinador:
    def __init__(
        self, marca: str, model: str, procesador: str, ram: int, disco_duro: int
    ) -> None:
        self.__marca: str = marca
        self.__model: str = model
        # Estos objetos pasan por sus respectivos setters y por tanto por las validaciones
        self.proce = procesador
        self.ram = ram  # En GB
        self.disco_duro = disco_duro  # en GB

    # Getters
    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def model(self) -> str:
        return self.__model

    @property
    def proce(self) -> str:
        return self.__proce

    @property
    def ram(self) -> int:
        return self.__ram

    @property
    def disco_duro(self) -> int:
        return self.__disco_duro

    # Setters
    # Se agregan validaciones al setter
    @proce.setter
    def proce(self, procesador: str) -> None:
        if not isinstance(procesador, str) or procesador.strip() == "":
            raise ValueError("El procesador debe ser un texto no vacio.")
        self.__proce = procesador

    @ram.setter
    def ram(self, ram: int):
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("La RAM debe ser un número entero positivo.")
        self.__ram = ram

    @disco_duro.setter
    def disco_duro(self, disco_duro: int):
        if not isinstance(disco_duro, int) or disco_duro <= 0:
            raise ValueError("El disco duro debe ser un número entero positivo.")
        self.__disco_duro = disco_duro

    # Metodos generales
    def executar(self, programa: str):
        print(f"En aquests moments s'està executant: {programa}")

    def toString(self):
        return (
            f"El ordenar es un {self.__marca}, modelo {self.__model}\n"
            f"Procesador: {self.__proce}\n"
            f"RAM: {self.__ram} GB\n"
            f"Disco Duro: {self.__disco_duro} GB"
        )
