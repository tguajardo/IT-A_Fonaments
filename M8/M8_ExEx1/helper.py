# Archivo con funciones comunes y utiles (verificadores, mensajes comunes, etc...)


class Helper:
    ERRORS = {
        "empty_text": "ERROR: El valor debe ser un texto no vacío.",
        "negative_number": "ERROR: El número debe ser positivo.",
        "element_exists": "ERROR: El elemento ya existe.",
        "element_not_exists": "ERROR: El elemento no existe.",
        "invalid_int": "ERROR: Debes introducir un número entero.",
        "invalid_float": "ERROR: Debes introducir un número decimal.",
        "invalid_option": "ERROR: Opción invalida.",
        "invalid_id_doc": "ERROR: Número de identificación invalido.",
        "out_of_bound": "ERROR: Valor fuera de rango valido.",
        "invalid_length": "ERROR: Longitud incorrecta.",
    }
    # Variable para verificar DNI
    LETRA_DNI: str = "TRWAGMYFPDXBNJZSQVHLCKE"

    # ---------- Validadores ----------
    @staticmethod
    def validateDni(dni: str) -> bool:
        dni = dni.strip().upper()
        if len(dni) != 9:
            return False
        if not dni[:8].isdigit():
            return False
        if not dni[-1].isalpha():
            return False
        numero: int = int(dni[:8])
        letra: str = dni[-1]
        return letra == Helper.LETRA_DNI[numero % 23]

    @staticmethod
    def notEmpty(text: str) -> bool:
        if text.strip() == "":
            print(Helper.ERRORS["empty_text"])
            return False
        return True

    # ---------- Peticiones por teclado ----------
    # Todas devuelven None si el dato es inválido (y ya han mostrado el error).
    @staticmethod
    def requestText(prompt: str) -> str | None:
        text: str = input(f"{prompt}: ").strip()
        if not Helper.notEmpty(text):
            return None
        return text

    @staticmethod
    def requestInt(prompt: str) -> int | None:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print(Helper.ERRORS["invalid_int"])
            return None

    @staticmethod
    def requestIntInRange(prompt: str, minimo: int, maximo: int) -> int | None:
        value = Helper.requestInt(prompt)
        if value is None:
            return None
        if value < minimo or value > maximo:
            print(Helper.ERRORS["out_of_bound"])
            return None
        return value

    @staticmethod
    def requestPosFloat(prompt: str) -> float | None:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print(Helper.ERRORS["invalid_float"])
            return None
        if value <= 0:
            print(Helper.ERRORS["negative_number"])
            return None
        return value

    @staticmethod
    def requestYesNo(prompt: str) -> bool | None:
        answer: str = input(prompt).strip().upper()
        if answer == "S":
            return True
        if answer == "N":
            return False
        print(Helper.ERRORS["invalid_option"])
        return None

    # ---------- Búsquedas ----------
    # Devuelven (objeto, posición) o (None, -1) si no se encuentra.
    @staticmethod
    def getByName(objectList: list, name: str):
        for index in range(len(objectList)):
            if objectList[index].getNombre().upper() == name.strip().upper():
                return objectList[index], index
        return None, -1

    @staticmethod
    def getByDni(objectList: list, name: str):
        for index in range(len(objectList)):
            if objectList[index].getDni().upper() == name.strip().upper():
                return objectList[index], index
        return None, -1


# Búsqueda genérica en dos niveles: objeto -> lista de elementos -> valor.
# lista de elementos -> .listValue() -> cambiar por lista adecuada (ej, cuentas en usuario)
# valor -> .getValue() -> cambiar por valor a buscar (ej, saldo = 1000)
# recordar agregar clase al principio
"""
    @staticmethod
    def getByValue(objectList, valueToFind):
        for index in range(len(objectList)):
            for value in objectList[index].listValue():
                if value.getValue() == valueToFind:
                    return objectList[index], index
        return None, -1
"""
