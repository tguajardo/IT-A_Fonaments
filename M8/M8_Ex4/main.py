"""En una biblioteca es vol desenvolupar una petita aplicació per gestionar el préstec de llibres als usuaris.

La biblioteca disposa d’una col·lecció de llibres i d’un registre d’usuaris.

Classe Llibre

La classe Llibre tindrà els atributs isbn, títol i si el llibre està disponible per ser prestat. A més, tindrà el constructor i els mètodes per poder-se prestar i retornar.

El mètode prestar posarà l'atribut disponible a False i el mètode retornar posarà l'atribut disponible a True.

Classe Usuari

La classe Usuari tindrà els atributs nom, cognom, DNI i una llista dels llibres que té prestats.
A més, tindrà el constructor i els mètodes de prestar i retornar.

El mètode prestar, afegirà el llibre a la seva llista de llibres prestats, i el mètode retornar, eliminarà el llibre de la seva llista de llibres prestats.

Diagrama classes Biblioteca

Funcionament del sistema

Un usuari pot tenir un o diversos llibres prestats
Un llibre només pot estar prestat a un únic usuari
Quan un llibre es presta:
deixa d’estar disponible
s’assigna a l’usuari
Quan un llibre es retorna:
torna a estar disponible
deixa d’estar assignat a l’usuari
Aplicació

Has de desenvolupar un programa en Python que permeti gestionar aquest sistema mitjançant un menú amb les següents opcions:

Crear un usuari
Eliminar un usuari
Registrar un llibre al sistema
Prestar un llibre a un usuari
Retornar un llibre
Regles importants

Quan es crea un usuari, inicialment no té cap llibre prestat
Quan es crea un llibre, el seu estat inicial és disponible = True
Un llibre només es pot prestar si està disponible
Un usuari pot tenir diversos llibres prestats:
Requisits tècnics

Has d’utilitzar classes (class) per representar Usuari i Llibre
Has d’utilitzar llistes per emmagatzemar usuaris i llibres
Les dades s’introduiran per teclat
El menú s’ha de repetir fins que l’usuari decideixi sortir"""

# Imports
from usuari import Usuari
from llibre import Llibre

# Variables globales
USERS: list[Usuari] = []
BOOKS: list[Llibre] = []

ERRORS = {
    "empty_text": "ERROR: El valor debe ser un texto no vacío.",
    "negative_number": "ERROR: El número debe ser positivo.",
    "element_exists": "ERROR: El elemento ya existe.",
    "element_not_exists": "ERROR: El elemento no existe.",
    "invalid_int": "ERROR: Debes introducir un número entero.",
    "invalid_float": "ERROR: Debes introducir un número decimal.",
    "invalid_option": "ERROR: Opción invalida.",
    "invalid_id_doc": "ERROR: N[umero de identificación invalido.",
    "out_of_bound": "ERROR: Valor fuera de rango valido.",
    "invalid_length": "ERROR: Longitud incorrecta.",
}
# Variable para verificar DNI
LETRA_DNI: str = "TRWAGMYFPDXBNJZSQVHLCKE"

# Datos de prueba
USER1: Usuari = Usuari("Tomas", "Guajardo", "12345678Z")
BOOK1: Llibre = Llibre("1234567890123", "Libro1")
USERS.append(USER1)
BOOKS.append(BOOK1)
USER1.prestar(BOOK1)
print(USERS[0])
print(BOOKS[0])


# Metodos generales
# Validador DNI
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
    verificador = LETRA_DNI[numero % 23]
    return letra == verificador


# Validador ISBN
def validateIsbn(isbn: str) -> bool:
    isbn = isbn.strip()
    if len(isbn) != 13:
        print(ERRORS["invalid_length"])
        return False
    try:
        int(isbn)
    except ValueError:
        print(ERRORS["invalid_int"])
    # Se excluye verificación de digito verificador (n1*1+n2*3+n3*1+...=mod 10)
    return True


# Buscador usuario en lista
def getUser(dni: str) -> None | Usuari:
    for user in USERS:
        if user.getDni().casefold() == dni.casefold():
            return user
    return None


# Solicitur de usuario para las distintas funciones
def requestUser(prompt: str) -> Usuari | None:
    print(prompt)
    dni: str = input("DNI: ").strip().upper()

    if not validateDni(dni):
        print(ERRORS["invalid_id_doc"])
        return None

    user: Usuari | None = getUser(dni)
    if user is None:
        print(ERRORS["element_not_exists"])
    return user


# Buscador libro en lista
def getBook(isbn: str) -> None | Llibre:
    for book in BOOKS:
        if book.getIsbn().casefold() == isbn.casefold():
            return book
    return None


# Solicitur de usuario para las distintas funciones
def requestBook(prompt: str) -> Llibre | None:
    print(prompt)
    isbn: str = input("ISBN: ").strip()

    if not validateIsbn(isbn):
        print(ERRORS["invalid_id_doc"])
        return None

    book: Llibre | None = getBook(isbn)
    if book is None:
        print(ERRORS["element_not_exists"])
    return book


# Metodos particulares
def createUser() -> None:
    print("\nInformación de Usuario a crear: ")
    nameUser: str = input("Nombre: ").strip().upper()
    lastNameUser: str = input("Apellido: ").strip().upper()
    if nameUser == "" or lastNameUser == "":
        print(f"{ERRORS['empty_text']}")
        return
    dniUser: str = input("DNI: ").strip().upper()
    if getUser(dniUser) != None:
        print(ERRORS["element_exists"])
        return

    createdUser: Usuari = Usuari(nameUser, lastNameUser, dniUser)
    USERS.append(createdUser)
    print(f"\nCliente creado correctamente")
    print(f"------Cliente------")
    print(f"{createdUser}\n")


def deleteUser() -> None:
    user = requestUser("\nDNI Usere a eliminar.")
    if user is None:
        return
    # Devolver todos los libros del usuario antes de elimarlo
    for book in user.getLlibres():
        user.retornar(book)
    USERS.remove(user)
    print("Usuario eliminado correctamente.")


def createBook() -> None:
    print("\nInformación de libro a crear: ")
    isbn: str = input("ISBN: ").strip()
    if not validateIsbn(isbn):
        return
    titol: str = input("Titulo: ").strip()
    if titol == "":
        print(ERRORS["empty_text"])
        return
    newBook: Llibre = Llibre(isbn, titol)
    BOOKS.append(newBook)
    print("Libro creado correctamente")
    return


def lendBook() -> None:
    book: Llibre | None = requestBook("ISBN Libro a prestar.")
    if book is None:
        return
    if not book.getDisponible():
        print("Libro no disponible.")
        return
    user: Usuari | None = requestUser("Usuario a prestar Libro.")
    if user is None:
        return
    user.prestar(book)
    print("Libro prestado correctamente.")
    return


def returnBook() -> None:
    book: Llibre | None = requestBook("ISBN Libro a devolver.")
    if book is None:
        return
    if book.getDisponible():
        print("Libro no ha sido prestado.")
        return
    for user in USERS:
        for lentBook in user.getLlibres():
            if book == lentBook:
                user.retornar(book)
    print("Libro devuelto correctamente.")
    return


# Main menu
def main() -> None:
    flag: str = ""
    while flag != "0":
        print(f"\n-------Gestión de biblioteca-------")
        print("-------Opciones-------\n")
        print("1. Crear Usuario.")
        print("2. Eliminar Usuario.")
        print("3. Crear Libro.")
        print("4. Prestar Libro.")
        print("5. Devolver Libro.")
        print("0. Salir")
        print("--------------")
        flag = input("Introduce la opción: ").strip()
        match flag:
            case "1":
                createUser()
            case "2":
                deleteUser()
            case "3":
                createBook()
            case "4":
                lendBook()
            case "5":
                returnBook()
            case "0":
                print("Saliendo del programa.")
            case _:
                print(f"{ERRORS['invalid_option']}")

        # Visualizador clientes y cuentas para revision.
        print("\n-----TEST-----")
        for user in USERS:
            print(user)
            for book in user.getLlibres():
                print(book)
            print("--------------")
        for book in BOOKS:
            print(book)
        print("--------------\n\n")


if __name__ == "__main__":
    main()
