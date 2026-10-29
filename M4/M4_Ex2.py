# Aquest programa li demana l’edat a l’usuari/ària, en funció d’aquesta, mostrarem un dels següents missatges per pantalla:

# Si té 5 anys o menys: preescolar.
# Si té entre 6 i 11 anys: primària.
# Si té entre 12 i 15: ESO.
# Si té entre 16 i 17: Batxillerat.
# Si és major d'edat: FP o Universitat.

# Dades
edat: int = int(input("Introdueixi la seva edat "))

# Operacions
if edat <= 5:
    message: str = f"Si té 5 anys o menys: preescolar."
elif edat <= 11:
    message: str = f"Si té entre 6 i 11 anys: primària."
elif edat <= 15:
    message: str = f"Si té entre 12 i 15: ESO."
elif edat <= 17:
    message: str = f"Si té entre 16 i 17: Batxillerat."
else:
    message: str = f"Si és major d'edat: FP o Universitat."
print(message)
