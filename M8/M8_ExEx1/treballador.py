"""De les persones treballadores de les diferents escuderies volen saber el nom, el primer cognom, l’edat, el temps que porten a l’escuderia i el sou. El sou base és de 50.000 €. A més, dels/les pilots volen saber la seva alçada, el pes. El sou dels/les pilots és el sou base de les persones treballadores més 10.000 € per cada any d’antiguitat a l’escuderia, més 50.000 € de perillositat.

Dels/les mecànics volen saber si tenen estudis superiors de mecànica o no. I el seu sou es calcula sumant 10.000 € per cada any d’antiguitat a l’escuderia més el sou base.
"""

"""
Estructura Treballador
Treballador: clase madre abstracta.
            DNI, nombre, apellido, edad, antigüedad y sueldo base.

No se crean trabajadores genéricos: cada trabajador debe ser Piloto o Mecánico.
"""

from abc import ABC, abstractmethod


class Treballador(ABC):
    # Constantes de clase (equivalen a "public static final" en Java)
    SUELDO_BASE: float = 50000.0
    PLUS_ANTIGUEDAD: float = 10000.0

    def __init__(
        self, dni: str, nombre: str, apellido: str, edad: int, antiguedad: int
    ) -> None:
        self.__dni: str = dni
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__edad: int = edad
        self.__antiguedad: int = antiguedad

    # ---------- Getters ----------
    def getDni(self) -> str:
        return self.__dni

    def getNombre(self) -> str:
        return self.__nombre

    def getApellido(self) -> str:
        return self.__apellido

    def getEdad(self) -> int:
        return self.__edad

    def getAntiguedad(self) -> int:
        return self.__antiguedad

    # ---------- Setters ----------
    # No hay setDni: el DNI identifica al trabajador y no debe cambiar.
    def setNombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def setApellido(self, apellido: str) -> None:
        self.__apellido = apellido

    def setEdad(self, edad: int) -> None:
        self.__edad = edad

    def setAntiguedad(self, antiguedad: int) -> None:
        self.__antiguedad = antiguedad

    # ---------- Métodos abstractos ----------
    # Cada subclase calcula su sueldo de forma distinta.
    @abstractmethod
    def calcularSueldo(self) -> float:
        pass

    # ---------- toString ----------
    def __str__(self) -> str:
        return (
            f"DNI: {self.__dni} | {self.__nombre} {self.__apellido} | "
            f"Edad: {self.__edad} | Antigüedad: {self.__antiguedad} años | "
            f"Sueldo: {self.calcularSueldo():,.2f} €"
        )
