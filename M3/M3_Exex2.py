# Escriu un programa que calculi els litres de pintura necessaris per a pintar una paret rectangular.
# Un litre de pintura cobreix aproximadament, 12 m² en una sola mà.
# Crear una constant, Cobertura a Litros (recordar les convencions de noms) per a guardar la dada de cobertura de la pintura (12 m²).
# Hauràs de demanar a l'usuari/ària:
# L'alt i ample de la paret (multiplicant sabràs l'àrea de la mateixa).
# El nombre de mans a aplicar.
# Mostra en pantalla els litres de pintura a utilitzar.

COBERTURA_LITRES: float = 12.00  # m2 x litre

# Dades
alt: float = float(input("Introdueix l'alt de la paret en metres: "))
ample: float = float(input("Introdueix l'ample de la paret en metres: "))
mans: int = int(input("Introdueix el nombre de mas de pintura: "))

# Calculs
area: float = alt * ample
litres: float = (area * mans) / COBERTURA_LITRES

# Response
message: str = (
    f"Per pintar una paret de {area:.2f} m2 amb {mans} mans de pintura, necessites {litres} litres de pintura"
)

print(message)
