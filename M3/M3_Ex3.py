# El programa demana a l'usuari/ària que introdueixi 3 notes i el programa mostra la mitjana de les 3 notes per pantalla.

nota1: float = float(input("introduix la primera nota: "))
nota2: float = float(input("introduix la segona nota: "))
nota3: float = float(input("introduix la tercera nota: "))

mitjana: float = (nota1 + nota2 + nota3) / 3

message: str = f"La mitjana de les tres notes es: {mitjana:.2f}"
print(message)
