"""L’usuari/ària ha d’introduir una frase i el programa ha de dir si la frase és un palíndrom."""


def backward_string(string: str) -> str:
    result: str = ""
    for index in range(len(string) - 1, -1, -1):
        result += string[index]
    return result


def clean_string(frase: str) -> str:
    frase = frase.lower()
    resultat: str = ""
    for char in frase:
        if char.isalnum():  # Letras y números, se eliminan espacios
            if char == "á":  # Se eliminan acentos más comunes
                char = "a"
            if char == "é" or char == "è":
                char = "e"
            if char == "í":
                char = "i"
            if char == "ó" or char == "ò":
                char = "o"
            if char == "ú":
                char = "u"
            resultat += char
    return resultat


def main() -> None:
    frase_original: str = input("Frase a revisar: ").strip(" ")
    frase_limpia: str = clean_string(
        frase_original
    )  # un palindromo no considera espacios ni acentos
    posible_palindromo: str = backward_string(frase_limpia)
    print(posible_palindromo)
    if frase_limpia == posible_palindromo:
        print(f"Genial la frase {frase_original} es un palindromo")
    else:
        print("Esta frase no es un palindromo")


main()
