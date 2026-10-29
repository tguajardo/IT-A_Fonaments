# Escriu un programa en Python que llegeix un nombre (número) i mostra per pantalla el doble i el triple d'aquest número.

num1: float = float(input("Introdueix    un nombre: "))

doble: float = num1 * 2
triple: float = num1 * 3

message: str = f"""
El teu nombre es: {num1:.4f}
El doble del nombre es: {doble:.4f}
El triple del nombre es: {triple:.4f}
"""
print(message)
