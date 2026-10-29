"""
Fes un programa amb 3 funcions. El programa ha de cridar a les 3 funcions e interactuar amb elles de la següent manera:

a. Crea una funció sense paràmetres i sense retorn que imprimeixi per consola “sóc una funció”.
Sortida: sóc una funció

b. Crea una funció que rebi una llista de números com a paràmetre, imprimeixi el número més gran per pantalla i retorni l’índex d'on es troba el número més petit. Crea una llista de 5 números i crida a la funció que acabes de crear per imprimir el número més petit de l’array.
Sortida (amb aquests números dintre de l’array “8, 12, 5, 22, 6”:
                Número més gran 22 (això ho imprimeix el propi mètode)
                Número més petit 5  (això ho imprimeix on s'ha fet la crida a la funció)

c. Crea una funció que rebi dos números com a paràmetres i retorni una llista amb tots els números compresos entre ells.
Crida a la funció que acabes de crear amb els dos números que vulguis i imprimeix la llista que et retorna.
               Sortida (amb el núm 2 i 10):
               Els números compresos entre 2 i 10 són: 3, 4, 5, 6, 7, 8, 9"""

# Variables

lista_a_revisar: list[int] = [8, 12, 5, 22, 6]
num1: int = 2
num2: int = 10


def funcion_simple() -> None:
    print("sóc una funció")  # Imprimir mensaje simple


def revisar_lista(lista: list[int]) -> int:
    mayor: int = max(lista)
    menor: int = min(lista)
    indice_menor: int = lista.index(menor)
    print(f"Número més gran {mayor}")
    return indice_menor


def entre_dos_tierras(primer_num: int, segundo_num: int) -> list[int]:
    if primer_num > segundo_num:
        primer_num, segundo_num = segundo_num, primer_num
    return list(range(primer_num + 1, segundo_num))


def lista_to_text(lista: list[int]) -> str:
    texto_lista: str = str(lista[0])
    for num in lista[1:]:
        texto_lista += " ," + str(num)
    return texto_lista


print("Ejecución de funciones.")
print("Primera función.")
print()
funcion_simple()
print()
print("Segunda función.")
print()
indice: int = revisar_lista(lista_a_revisar)
print(f"Número més petit {lista_a_revisar[indice]}")
print()
print("Tercera función.")
print()
print(f"Sortida (amb el núm {num1} i {num2}):")
lista: list[int] = entre_dos_tierras(num1, num2)
print(f"Els números compresos entre {num1} i {num2} son : {lista_to_text(lista)}")
print()
print(f"Els números compresos entre {num1} i {num2} son : {lista}")
