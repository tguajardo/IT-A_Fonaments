# Una escola d’idiomes concedeix beques a futurs estudiants si compleixen una sèrie de requisits.
# A l'alumne/a se li assigna una beca si és major d’edat i si té un títol universitari.
# O també se li assigna una beca si l’alumne/a està a l’atur.
# El programa demana les tres dades per pantalla i en finalitzar mostra si l’alumne/a té la beca o no.
"""
Has de modificar el programa de les beques (ara el programa només ha de poder donar 5 beques).

El programa anirà demanant les dades dels/les alumnes fins que es donin aquestes 5 beques. Un cop el programa hagi assignat les 5 beques s’ha de mostrar per pantalla els noms dels/les 5 alumnes que tenen beca.
"""

# Constants
MAX_BEQUES: int = 5

# Llista d'alumnes acceptats
acceptats: list[str] = []

print("Programa de beques (només es poden donar 5 beques).")

while len(acceptats) < MAX_BEQUES:

    # Inputs
    nom: str = input("Nom de l'alumne/a: ")

    edat: str = input("És major d'edat? (si/no): ")
    titol: str = input("Té títol universitari? (si/no): ")
    atur: str = input("Està a l'atur? (si/no): ")

    # Check
    major_edat: bool = edat.lower() == "si"
    te_titol: bool = titol.lower() == "si"
    esta_atur: bool = atur.lower() == "si"

    # Alternativa
    # major_edta: bool = bool(int(input("És major d'edat? (1 = sí, 0 = no): ")))
    # te_titol: bool = bool(int(input("Té títol universitari? (1 = sí, 0 = no): ")))
    # esta_atur: bool = bool(int(input("Està a l'atur? (1 = sí, 0 = no): ")))

    # Condició de beca
    te_beca: bool = (major_edat and te_titol) or esta_atur

    # Resultat
    if te_beca:
        print(f"{nom} té beca.")
        acceptats.append(nom)
    else:
        print(f"{nom} no té beca.")

print("Beques completades!")
print("Els alumnes que tenen beca són:")
for alumne in acceptats:
    print(f"- {alumne}")
