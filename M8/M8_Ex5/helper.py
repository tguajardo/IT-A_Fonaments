# Archivo con funciones comunes y utiles (verificadores, mensajes comunes, etc...)

from edifici import Edifici


class Helper:
    ERRORS = {
        "empty_text": "ERROR: El valor debe ser un texto no vacío.",
        "negative_number": "ERROR: El número debe ser positivo.",
        "element_exists": "ERROR: El elemento ya existe.",
        "element_not_exists": "ERROR: El elemento no existe.",
        "invalid_int": "ERROR: Debes introducir un número entero.",
        "invalid_float": "ERROR: Debes introducir un número decimal.",
        "invalid_option": "ERROR: Opción invalida.",
        "invalid_id_doc": "ERROR: Nuumero de identificación invalido.",
        "out_of_bound": "ERROR: Valor fuera de rango valido.",
        "invalid_length": "ERROR: Longitud incorrecta.",
    }
    # Variable para verificar DNI
    LETRA_DNI: str = "TRWAGMYFPDXBNJZSQVHLCKE"

    # Validador DNI
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
        verificador = Helper.LETRA_DNI[numero % 23]
        return letra == verificador

    @staticmethod
    def requestPosInt(prompt: str | None) -> int | None:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                print(Helper.ERRORS["negative_number"])
                return None
            return value
        except ValueError:
            print(Helper.ERRORS["invalid_int"])
            return None

    @staticmethod
    def requestFloat(prompt: str | None) -> float | None:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print(Helper.ERRORS["invalid_float"])
            return None

    @staticmethod
    def requestInt(prompt: str | None) -> int | None:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print(Helper.ERRORS["invalid_int"])
            return None

    @staticmethod
    def notEmpty(text: str) -> bool:
        if text.strip() == "":
            print(Helper.ERRORS["empty_text"])
            return False
        return True

    @staticmethod
    def getPrompt(prompt: str) -> str | None:
        responsePrompt: str = input(f"{prompt}: ").strip().upper()
        if not Helper.notEmpty(responsePrompt):
            print(f"{Helper.ERRORS['empty_text']}")
            return None
        return responsePrompt

    # Los siguientes son metodos escritos de forma generica y deben modificarse una vez se conozca la estructura de los objetos
    @staticmethod
    def getByName(objectList, name: str):
        for index in range(len(objectList)):
            if objectList[index].getName() == name:
                return objectList[index], index
        return None, -1

    @staticmethod
    def getByValue(objectList, valueToFind: str):
        for index in range(objectList):
            for value in objectList[index].listValue():
                if value.getValue() == valueToFind:
                    return objectList[index], index
        return None, -1
