"""Fer un programa que li demani dos nombres enters a l’usuari/ària. Al final, el programa imprimeix per pantalla el següent missatge:

El resultat de la suma és: “valor”
El resultat de la resta és: “valor”
El resultat de la multiplicació és: “valor”
El resultat de la divisió és: “valor”."""

num1: int = int(input("Introdueix un primer nombre enter: "))
num2: int = int(input("Introdueix un secon nombre enter: "))

suma: int = num1 + num2
resta: int = num1 - num2
multiplicacio: int = num1 * num2
divisio: float = num1 / num2

message: str = f"""
El resultat de la suma es: {suma}
El resultat de la resta es: {resta}
El resultat de la multiplicacio es: {multiplicacio}
El resultat de la divisio es: {divisio}
"""

print(message)
