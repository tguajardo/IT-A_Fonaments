"""
Volen saber de cada escuderia que participa en el campionat, el nom, el pressupost que tenen i el país d’origen. Cada escuderia pot tenir més d’un cotxe i de cadascun volen saber la potència, la velocitat màxima, el color i el preu de mercat.
"""

"""
Estructura Cotxe
Cotxe:  modelo, potencia, velocidad máxima, color y precio de mercado.
        Debe estar asociado a una escuderia.
"""


class Cotxe:
    def __init__(
        self,
        modelo: str,
        potencia: int,
        velocidadMaxima: float,
        color: str,
        precioMercado: float,
    ) -> None:
        self.__modelo: str = modelo
        self.__potencia: int = potencia  # en HP
        self.__velocidadMaxima: float = velocidadMaxima  # en km/h
        self.__color: str = color
        self.__precioMercado: float = precioMercado  # en EUR
        # Asociación con la escuderia: la asigna Escuderia.addCotxe()
        self.__nombreEscuderia: str = ""

    # Getters
    def getModelo(self) -> str:
        return self.__modelo

    def getPotencia(self) -> int:
        return self.__potencia

    def getVelocidadMaxima(self) -> float:
        return self.__velocidadMaxima

    def getColor(self) -> str:
        return self.__color

    def getPrecioMercado(self) -> float:
        return self.__precioMercado

    def getNombreEscuderia(self) -> str:
        return self.__nombreEscuderia

    # Setters (Potencia, modelo y velocidad son propias del auto y no se deben poder cambiar)
    def setColor(self, color: str) -> None:
        self.__color = color

    def setPrecioMercado(self, precioMercado: float) -> None:
        self.__precioMercado = precioMercado

    def setNombreEscuderia(self, nombreEscuderia: str) -> None:
        self.__nombreEscuderia = nombreEscuderia

    # toString()
    def __str__(self) -> str:
        return (
            f"{self.__modelo} | {self.__nombreEscuderia} | "
            f"Potencia: {self.__potencia} HP | Vel. Max.: {self.__velocidadMaxima} Km/h |"
            f"Color: {self.__color} | Precio: {self.__precioMercado} EUR"
        )
