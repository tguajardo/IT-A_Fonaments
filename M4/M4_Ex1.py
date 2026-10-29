# recoger Datos
nom: str = input("Introdueixi el seu nom ")
cognom: str = input("Introdueixi el seu cognom ")
edat: int = int(input("Introdueixi la seva edat "))

if edat >= 18:
    message: str = f"{nom} {cognom}, ets MAJOR d'edat"
else:
    message: str = f"{nom} {cognom}, ets MENOR d'edat"

print(message)
