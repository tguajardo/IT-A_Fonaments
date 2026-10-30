"""De les persones treballadores de les diferents escuderies volen saber el nom, el primer cognom, l’edat, el temps que porten a l’escuderia i el sou. El sou base és de 50.000 €. A més, dels/les pilots volen saber la seva alçada, el pes. El sou dels/les pilots és el sou base de les persones treballadores més 10.000 € per cada any d’antiguitat a l’escuderia, més 50.000 € de perillositat.

Dels/les mecànics volen saber si tenen estudis superiors de mecànica o no. I el seu sou es calcula sumant 10.000 € per cada any d’antiguitat a l’escuderia més el sou base.
"""

"""
Estructura Pilots
Pilots: Hereda de Treballador -> DNI, nombre, apellido, edad, antigüedad y sueldo base.
        Propias -> altura y peso.
        Sueldo = 50.000 + (10.000 × antigüedad) + 50.000 de peligrosidad.
"""

from treballador import Treballador


class Pilots(Treballador):
    PLUS_PELIGROSIDAD: float = 50000.0

    def __init__(
        self,
        dni: str,
        nombre: str,
        apellido: str,
        edad: int,
        antiguedad: int,
        altura: float,
        peso: float,
    ) -> None:
        super().__init__(dni, nombre, apellido, edad, antiguedad)
        self.__altura: float = altura  # en metros
        self.__peso: float = peso  # en kg

    # ---------- Getters ----------
    def getAltura(self) -> float:
        return self.__altura

    def getPeso(self) -> float:
        return self.__peso

    # ---------- Setters ----------
    def setAltura(self, altura: float) -> None:
        self.__altura = altura

    def setPeso(self, peso: float) -> None:
        self.__peso = peso

    # ---------- Sobrescritura de métodos ----------
    def calcularSueldo(self) -> float:
        return (
            Treballador.SUELDO_BASE
            + Treballador.PLUS_ANTIGUEDAD * self.getAntiguedad()
            + Pilots.PLUS_PELIGROSIDAD
        )

    def __str__(self) -> str:
        return (
            super().__str__()
            + f" | Altura: {self.__altura:.2f} m | Peso: {self.__peso:.1f} kg"
        )
