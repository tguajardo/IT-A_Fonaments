"""Ens demanen crear una aplicació per donar d’alta, modificar, veure i eliminar hotels.

La classe hotel haurà de tenir els següents atributs: nom, nombre d’habitacions, nombre de plantes i superfície total de l’hotel. Com a mètodes només haurà de tenir els getters i setters propis de la classe i un mètode anomenat calcularManteniment(). Aquest mètode ha de tenir en compte que cada persona del servei pot atendre 20 habitacions i haurà de mostrar quantes persones són necessàries per atendre el servei d’habitacions de l’hotel i quin és el cost total destinat al servei sabent que aquestes persones cobren 1.500 € al mes.

La funció crearHotel() haurà de demanar a l’usuari/a que introdueixi per pantalla les dades de nom, nombre d’habitacions, nombre de plantes i superfície total de l’hotel (o haurà de rebre aquestes dades per paràmetre). Un cop hagi demanat totes aquestes dades, s’ha d’instanciar l’objecte de la classe i afegir-lo a un array d’hotels.

La funció donarDeBaixaHotel() haurà de rebre el nom de l'hotel que es vol donar de baixa. L’usuari/ària introduirà el nom de l’hotel i si l’hotel està dintre de l’array, l’eliminarem i mostrarem un missatge per pantalla informant l’usuari/ària que hem eliminat l’hotel. Si no hem trobat l’hotel dintre de l’array, avisarem l’usuari/ària dient que l’hotel no estava dintre de la nostra aplicació.

La funció veureHotel() haurà de rebre el nom de l'hotel que vol que mostrem per pantalla, si l’hotel està a la nostra aplicació, li mostrarem l’hotel, si no hi és, informarem l’usuari/ària dient que l’hotel que ens ha demanat no està dintre de la nostra aplicació.
Quan mostrem l’hotel, a més, de mostrar el nombre d’habitacions, nombre de plantes i superfície total de l’hotel també es cridarà al mètode calcularManteniment().

La funció modificarHotel() haurà de rebre el nom de l'hotel que volem modificar. L’usuari/ària introduirà el nom de l’hotel. Si el tenim a l’aplicació, li demanarem si vol modificar el nombre d’habitacions, el nombre de plantes o la superfície total de l’hotel. Farem la modificació pertinent i avisarem a l’usuari/ària que la modificació s’ha realitzat.
"""


class Hotel:
    def __init__(self, name: str, rooms: int, floors: int, area: float) -> None:
        # El __init__ llama a los setter de cada atributo
        self.name = name
        self.rooms = rooms
        self.floors = floors
        self.area = area

    # Getters y Setters
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name_to_be: str) -> None:
        if not isinstance(name_to_be, str) or name_to_be.strip() == "":
            raise ValueError("El nombre debe ser un texto no vacio.")
        self.__name = name_to_be

    @property
    def rooms(self) -> int:
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms_to_be: int) -> None:
        if not isinstance(rooms_to_be, int) or rooms_to_be <= 0:
            raise ValueError("Los cuartos deben ser un número entero positivo.")
        self.__rooms = rooms_to_be

    @property
    def floors(self) -> int:
        return self.__floors

    @floors.setter
    def floors(self, floors_to_be: int) -> None:
        if not isinstance(floors_to_be, int) or floors_to_be <= 0:
            raise ValueError("Los pisos deben ser un número entero positivo.")
        self.__floors = floors_to_be

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, area_to_be: float) -> None:
        if not isinstance(area_to_be, float) or area_to_be <= 0:
            raise ValueError("El area debe ser un número mayor a 0.")
        self.__area = area_to_be

    # Metodo general
    def calcularManteniment(self) -> tuple[int, float]:
        personel: int = (self.__rooms + 19) // 20
        cost: float = 1500.00 * personel
        return (personel, cost)

    def __str__(self):
        personal, costos = self.calcularManteniment()
        return (
            f"Nombre hotel: {self.__name}\n"
            f"con {self.__rooms} cuartos\n"
            f"en {self.__floors} pisos\n"
            f"y un area de {self.__area} m^2\n"
            f"Para funcionar necesita {personal} trabajadores\n"
            f"Con un costo de {costos} euros al mes"
        )
