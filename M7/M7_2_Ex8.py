"""L’usuari/ària introdueix un nombre per teclat i el programa crida a un mètode que ha de mostrar la successió de Fibonacci.

Exemple:

Si l’usuari/ària introdueix el 10, el resultat ha de ser:

0,1,1,2,3,5,8,13,21,34

Fibonacci
F(n) = F(n-1) + F(n-2)
F(0) = 0
F(1) = 1
F(2) = F(1) + F(0) = 1 + 0 = 1
F(3) = F(2) + F(1) = 1 + 1 = 2
....

Formas de solucionar
Recursivo = Complejidad exponencial, se calcula de arriba hacia abajo, se hacen tantos calculos como sea necesario hasta llega a F(0) o F(1)
def fibonacci_recursivo(N):
    if N<=1:
        return N
    return fibonacci_recursivo(N - 1) + fibonacci_recursivo(N - 2)

Iterativo = Complejidad lineal, se construye de abajo hacia arriba, cada valor se calcula solo una vez
def fibonacci_iterativo(N):
    prev = 0
    current = 1
    lista = []
    for __ in range(N)
        lista.append(prev)

        next = current + prev
        prev = current
        current = next

"""

import time


def fibonacci_recursivo(N: int) -> int:
    if N <= 1:
        return N
    return fibonacci_recursivo(N - 1) + fibonacci_recursivo(N - 2)


def print_fibonacci_recursivo(N: int) -> None:
    lista_recursiva: list[str] = []
    for i in range(N):
        lista_recursiva.append(str(fibonacci_recursivo(i)))
    print(",".join(lista_recursiva))


def print_fibonacci_iterativo(N: int) -> None:
    lista_iterativa: list[str] = []
    previous_value: int = 0  # F[0]
    current_value: int = 1  # F[1]
    for _ in range(N):
        lista_iterativa.append(str(previous_value))
        current_value, previous_value = current_value + previous_value, current_value
    print(",".join(lista_iterativa))


def verificar_numero(num_text: str) -> bool:
    try:
        if int(num_text) > 0:
            return True
        return False
    except ValueError:
        return False


def main() -> None:
    num_fibonacci_text: str = input("Introduce cuantos números quieres calcular: ")
    if verificar_numero(num_fibonacci_text):
        num_fibonacci = int(num_fibonacci_text)
    else:
        print("El número debe ser un entero mayor a 0.")
        return

    print("Fibonacci recursivo")
    start_time: float = time.time()
    print_fibonacci_recursivo(num_fibonacci)
    end_time: float = time.time()
    print(f"Tiempo Fibonacci recursivo: {end_time - start_time:.6f} segundos")
    print()

    print("Fibonacci iterativo")
    start_time = time.time()
    print_fibonacci_iterativo(num_fibonacci)
    end_time = time.time()
    print(f"Tiempo Fibonacci iterativo: {end_time - start_time:.6f} segundos")


main()
