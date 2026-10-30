"""De les persones treballadores de les diferents escuderies volen saber el nom, el primer cognom, l’edat, el temps que porten a l’escuderia i el sou. El sou base és de 50.000 €. A més, dels/les pilots volen saber la seva alçada, el pes. El sou dels/les pilots és el sou base de les persones treballadores més 10.000 € per cada any d’antiguitat a l’escuderia, més 50.000 € de perillositat.

Dels/les mecànics volen saber si tenen estudis superiors de mecànica o no. I el seu sou es calcula sumant 10.000 € per cada any d’antiguitat a l’escuderia més el sou base.
"""

"""
Estructura Mecanic

Mecanic:Hereda de Treballador -> DNI, nombre, apellido, edad, antigüedad y sueldo base.
        Propias -> Estudios superiores
        Sueldo = 50.000 + (10.000 × antigüedad).
"""

from treballador import Treballador


class Mecanic(Treballador):
    def __init__(
        self,
        dni: str,
        nombre: str,
        apellido: str,
        edad: int,
        antiguedad: int,
        estudiosSuperiores: bool,
    ) -> None:
        super().__init__(dni, nombre, apellido, edad, antiguedad)
        self.__estudiosSuperiores: bool = estudiosSuperiores

    # ---------- Getters / Setters ----------
    def hasEstudiosSuperiores(self) -> bool:
        return self.__estudiosSuperiores

    def setEstudiosSuperiores(self, estudiosSuperiores: bool) -> None:
        self.__estudiosSuperiores = estudiosSuperiores

    # ---------- Sobrescritura de métodos ----------
    def calcularSueldo(self) -> float:
        return (
            Treballador.SUELDO_BASE + Treballador.PLUS_ANTIGUEDAD * self.getAntiguedad()
        )

    def __str__(self) -> str:
        estudios = "Sí" if self.__estudiosSuperiores else "No"
        return super().__str__() + f" | Estudios superiores: {estudios}"
