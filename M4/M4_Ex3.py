# Una escola d’idiomes concedeix beques a futurs estudiants si compleixen una sèrie de requisits.
# A l'alumne/a se li assigna una beca si és major d’edat i si té un títol universitari.
# O també se li assigna una beca si l’alumne/a està a l’atur.
# El programa demana les tres dades per pantalla i en finalitzar mostra si l’alumne/a té la beca o no.

edat: str = input("És major d'edat? (si/no): ")
titol: str = input("Té títol universitari? (si/no): ")
atur: str = input("Està al atur? (si/no): ")

major_edat: bool = False
te_titol: bool = False
esta_atur: bool = False

if edat == "si":
    major_edat = True

if titol == "si":
    te_titol = True

if atur == "si":
    esta_atur = True

# Alternativa
# major_edta: bool = bool(int(input("És major d'edat? (1 = sí, 0 = no): ")))
# te_titol: bool = bool(int(input("Té títol universitari? (1 = sí, 0 = no): ")))
# esta_atur: bool = bool(int(input("Està a l'atur? (1 = sí, 0 = no): ")))

# Condicio beca
te_beca: bool = major_edat and te_titol or esta_atur

# Missatge final
if te_beca:
    message: str = f"L'alumne te beca."
else:
    message: str = f"L'alumne no te beca."

print(message)
