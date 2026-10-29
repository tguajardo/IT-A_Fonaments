"""En aquest programa l’usuari/ària ha d’introduir un string i, utilitzant un bucle for, el programa ha de mostrar l’string al revés."""


def backward_string(string: str) -> str:
    result: str = ""
    for index in range(len(string) - 1, -1, -1):
        result += string[index]
    return result


def main() -> None:
    print(backward_string(input("Introduce la palabra a girar: ")))


main()
