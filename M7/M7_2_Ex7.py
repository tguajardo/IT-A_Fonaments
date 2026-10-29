"""L’usuari/ària introdueix un any “a” per teclat
i el programa crida a una funció que indiqui si l’any és de traspàs o no."""


def is_leap(year: int) -> bool:
    result: bool = False
    if year % 400 == 0:
        result = True
    elif year % 4 == 0 and year % 100 != 0:
        result = True

    return result


def verify_year(year_text: str) -> bool:
    try:
        if int(year_text) > 0:
            return True
        return False
    except ValueError:
        return False


def main():
    year_text: str = input("Introduce un año a verificar: ")
    if verify_year(year_text):
        if is_leap(int(year_text)):
            print(f"El año {year_text} es bisiesto")
        else:
            print(f"El año {year_text} no es bisiesto")
    else:
        print("El año introducido no es valido.")
        return


main()
