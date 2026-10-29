"""Crea un programa on l’usuari/ària introdueixi una temperatura en °C i es mostri per pantalla la conversió en ° Fahrenheit.

K = 32;

Fórmula
(0 °C × 9 / 5) + K = 32 °F
"""


def celsius_a_farenheit(CELSIUS: float) -> float:
    return (CELSIUS * 9 / 5) + 32


def verificar_numero(num_text: str) -> bool:
    try:
        float(num_text)
        return True
    except ValueError:
        return False


def main() -> None:
    celsius_text: str = input("Introduce la temperatura en grados celius: ")
    if not verificar_numero(celsius_text):
        print("Debes ingresar un número.")
        return
    celsius: float = float(celsius_text)
    farenheit = celsius_a_farenheit(celsius)
    print(f"{celsius_text}°C corresponden a {farenheit:.2f}°F")


main()
