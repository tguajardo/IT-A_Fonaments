"""
Programa una aplicació que tingui 5 opcions:

1.- Crear client/a.
2.- Eliminar client/a.
3.- Crear compta d'un client/a.
4.- Ingressar euros en un compte d'un client/a.
5.- Retirar euros en un compte d'un client/a.
A tenir en compte:
- El saldo inicial de totes les comptes, ha de ser 0 €.
- En crear un client, no haurà de tenir cap compte “associada”.
"""

from cliente import Cliente
from cuenta import Cuenta

# Variables Globales
CLIENTS: list[Cliente] = []
ERRORS = {
    "empty_text": "ERROR: El valor debe ser un texto no vacío.",
    "negative_number": "ERROR: El número debe ser positivo.",
    "element_exists": "ERROR: El elemento ya existe.",
    "element_not_exists": "ERROR: El elemento no existe.",
    "invalid_int": "ERROR: Debes introducir un número entero.",
    "invalid_float": "ERROR: Debes introducir un número decimal.",
    "invalid_option": "ERROR: Opción invalida.",
    "invalid_id_doc": "ERROR: Documento de identificación invalido.",
    "out_of_bound": "ERROR: Valor fuera de rango valido.",
}
# Variable para verificar DNI
LETRA_DNI: str = "TRWAGMYFPDXBNJZSQVHLCKE"


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


# Buscador cliente en lista
def getClient(dni: str) -> None | Cliente:
    for client in CLIENTS:
        if client.getDni().casefold() == dni.casefold():
            return client
    return None


def requestClient(prompt: str) -> Cliente | None:
    print(prompt)
    dni: str = input("DNI: ").strip().upper()

    if not validateDni(dni):
        print(ERRORS["invalid_id_doc"])
        return None

    client: Cliente | None = getClient(dni)
    if client is None:
        print(ERRORS["element_not_exists"])
    return client


def requestPosInt(prompt: str) -> int | None:
    try:
        value = int(input(prompt).strip())
        if value < 0:
            print(ERRORS["negative_number"])
            return None
        return value
    except ValueError:
        print(ERRORS["invalid_int"])
        return None


def requestAmount() -> int | None:
    amount = requestPosInt("Monto: ")
    if amount is None:
        return None
    return amount


def showAccounts(client: Cliente) -> None:
    for i in range(len(client.getAccounts())):
        print(client.getAccounts()[i])
    return


def selectAccount() -> Cuenta | None:
    client = requestClient("DNI del cliente.")
    if client is None:
        return None
    if len(client.getAccounts()) == 0:
        print(ERRORS["element_not_exists"])
        return None
    showAccounts(client)
    number = requestPosInt("Número de cuenta: ")
    if number is None:
        return None
    if number > len(client.getAccounts()):
        print(ERRORS["out_of_bound"])
        return None
    account = client.getAccounts()[number - 1]
    return account


# Metodos Solicitados
def createClient():
    print("\nInformación de cliente a crear: ")
    nameClient: str = input("Nombre: ").strip().upper()
    lastNameClient: str = input("Apellido: ").strip().upper()
    if nameClient == "" or lastNameClient == "":
        print(f"{ERRORS['empty_text']}")
        return
    dniClient: str = input("DNI: ").strip().upper()
    if not validateDni(dniClient):
        print(f"{ERRORS['invalid_id_doc']}")
        return
    clientExists = getClient(dniClient)
    if clientExists != None:
        print(f"{ERRORS['element_exists']}")
        return
    createdClient: Cliente = Cliente(nameClient, lastNameClient, dniClient)
    CLIENTS.append(createdClient)
    print(f"Cliente creado correctamente")
    print(f"\n------Cliente------")
    print(f"{createdClient}\n")


def deleteClient() -> None:
    client = requestClient("\nDNI cliente a eliminar.")
    if client is None:
        return
    CLIENTS.remove(client)
    print("Cliente eliminado correctamente.")


def createAccount() -> None:
    client = requestClient("DNI cliente a agregar cuenta.")
    if client is None:
        return
    accountNumber = len(client.getAccounts()) + 1
    client.addAccount(Cuenta(accountNumber))
    print(f"Cuenta {accountNumber} agregada exitosamente")


def addMoney() -> None:
    account = selectAccount()
    if account is None:
        return
    amount = requestAmount()
    if amount is None:
        return
    account.ingresar(amount)
    print(f"Nuevo saldo: {account.getSaldo()} EUR")


def withdrawMoney() -> None:
    account = selectAccount()
    if account is None:
        return
    amount = requestAmount()
    if amount is None:
        return
    if account.retirar(amount):
        print(f"Nuevo saldo: {account.getSaldo()} EUR")
    else:
        print("Saldo insuficiente.")


# Main
def main() -> None:
    flag: str = ""
    while flag != "0":
        print(f"\n-------Gestión de clientes-------")
        print("-------Opciones-------\n")
        print("1. Crear Cliente.")
        print("2. Eliminar Cliente.")
        print("3. Crear Cuenta Cliente.")
        print("4. Ingresar monto.")
        print("5. Retirar monto.")
        print("0. Salir")
        print("--------------")
        flag = input("Introduce la opción: ").strip()
        match flag:
            case "1":
                createClient()
            case "2":
                deleteClient()
            case "3":
                createAccount()
            case "4":
                addMoney()
            case "5":
                withdrawMoney()
            case "0":
                print("Saliendo del programa.")
            case _:
                print(f"{ERRORS['invalid_option']}")

        # Visualizador clientes y cuentas para analisis
        print("-----TEST-----")
        for client in CLIENTS:
            print(client)
            for account in client.getAccounts():
                print(account)
            print("--------------")


if __name__ == "__main__":
    main()
