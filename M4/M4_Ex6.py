# Fer un programa que demani a l’usuari/ària quin dia i quin mes va néixer, amb aquesta informació el programa mostra per pantalla, de quin signe del zodíac és.
"""Àries-Aries (21.03 — 19.04)
Taure-Tauro (20.04 — 20.05)
Bessons-Géminis (21.05 — 20.06)
Cranc-Cáncer (21.06 — 22.07)
Lleó-Leo (23.07 — 22.08)
Verge-Virgo (23.08 — 22.09)
Balança-Libra (23.09 — 22.10)
Escorpí-Escorpión (23.10 — 21.11)
Sagitari-Sagitario (22.11 — 21.12)
Capricorn-Capricornio (22.12 — 19.01)
Aquari-Acuario (20.01 — 18.02)
Peixos-Piscis (19.02 — 20.03)"""

# Variables
birth_day: int
birth_month: int
birth_sign: str
signe: str
message: str

# Data and check
day: str = input("Introdueix el teu dia de neixament (1-31): ")
if day.isdigit():
    birth_day = int(day)
    if birth_day == 0 or birth_day > 31:
        print("Dia no vàlid")
        exit()
else:
    print("Dia no vàlid")
    exit()

month: str = input("Introdueix el teu month de neixament (1-12): ")
if month.isdigit():
    birth_month = int(month)
else:
    print("Mes no vàlid")
    exit()

# Operation
match birth_month:
    case 1:
        if birth_day < 20:
            signe = "Capricorn"
        else:
            signe = "Aquari"
    case 2:
        if birth_day < 19:
            signe = "Aquari"
        else:
            signe = "Peixos"
    case 3:
        if birth_day < 21:
            signe = "Peixos"
        else:
            signe = "Àries"
    case 4:
        if birth_day < 20:
            signe = "Àries"
        else:
            signe = "Taure"
    case 5:
        if birth_day < 21:
            signe = "Taure"
        else:
            signe = "Bessons"
    case 6:
        if birth_day < 21:
            signe = "Bessons"
        else:
            signe = "Cranc"
    case 7:
        if birth_day < 23:
            signe = "Cranc"
        else:
            signe = "Lleó"
    case 8:
        if birth_day < 23:
            signe = "Lleó"
        else:
            signe = "Verge"
    case 9:
        if birth_day < 23:
            signe = "Verge"
        else:
            signe = "Balança"
    case 10:
        if birth_day < 23:
            signe = "Balança"
        else:
            signe = "Escorpí"
    case 11:
        if birth_day < 22:
            signe = "Escorpí"
        else:
            signe = "Sagitari"
    case 12:
        if birth_day < 22:
            signe = "Sagitari"
        else:
            signe = "Capricorn"
    case _:
        print("Mes no valid")
        exit()

# Output
message = f"Has nascut el {birth_day}/{birth_month} i el teu signe és {signe}."
print(message)
