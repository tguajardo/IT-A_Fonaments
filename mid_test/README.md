# Examen Parcial: Fonaments PY

**Fecha:** 06/10/2026

## Instrucciones generales

- El examen consta de 3 ejercicios. Dispones de **3 horas** para resolverlo.
- **IMPORTANTE:** Los ejercicios 1 y 2 trabajan sobre el mismo conjunto de datos. Asegúrate de generar el array aleatorio una sola vez y de usarlo en todas las funciones. Utiliza la función proporcionada **`array_generator()`** para crear un array y guárdalo en una variable global.
- Si te atascas con la lógica de algún ejercicio, deja comentado en el código cómo planeabas resolverlo (pseudocódigo). Eso suma puntos. Es preferible explicar tu razonamiento a dejar el ejercicio en blanco.

## Contexto

Trabajas para una aerolínea low-cost, que necesita un pequeño programa para registrar reservas, asignar asientos y mostrar listados. Tu tarea es programarlo con Python.

## Ejercicios

### 1. Verificador de asientos de vuelo

Antes de empezar tu turno, el sistema ha generado automáticamente la lista oficial de asientos disponibles para asignar. Ese será tu array global. La reserva de un asiento cuesta 5 euros.

Deberás crear la función `assign-seat()`, que tendrá como objetivo:

- Pedir un número (fila-posición) de asiento deseado.
- Comprobar si el asiento deseado está dentro de la lista de asientos disponibles.
- Actualizar la lista según el caso (Explicado a continuación).
- Registrar el dinero recaudado por la reserva de asientos.
- Mostrar un mensaje de respuesta al usuario.

Casos particulares:

- **Si el asiento no está libre:** muestra un mensaje de error claro y vuelve a pedir el siguiente asiento. No se cobra el intento.
- **Si el asiento está disponible:** elimina ese valor de la lista de disponibles y lo añade a una segunda lista de asientos asignados. También registra el cobro de la reserva en el dinero acumulado de la empresa.

Este proceso se debe repetir hasta que el usuario ingrese la palabra `"salir"` o hasta que no queden más asientos disponibles.

Cuando termine, muestra un informe con:

- Los asientos que han sido asignados.
- La cantidad de asientos que siguen disponibles.
- El **dinero recaudado total** por reservas de asientos.


> - **TIP:** Puedes hacer `print()` del array global para ayudarte a probar tu programa.

---

### 2. Contador de asientos de ventanilla

Crea una función llamada **`window_seats()`**, que servirá a la empresa para medir la tendencia de los pasajeros a sentarse en ventanilla o en pasillo.

Al ejecutarla, la función debe recorrer el array de asientos asignados generado anteriormente e imprimir en pantalla cuántos asientos corresponden a un asiento de ventanilla, cuantos a pasillo, y cual de los dos es la preferencia. En un avión de seis asientos por fila, los asientos de ventanilla terminan con la letra A o F, y los de pasillo con C o D.

> **TIP:** Si no has completado el ejercicio anterior, puedes crear un array de ejemplo con el que probar esta función (por ejemplo: `["15-A", "20-C", "35-D", "42-B"]`) y usarlo en ella.

---

### 3. Pasajeros en salida de emergencia

A partir del array **`PASSENGERS`** (que tiene una estructura plana intercalando nombres y filas asignadas: `["pasajero", fila, "pasajero", fila...]`), genera la función **`emergency_exit()`** para que un usuario pulse un botón y obtenga una lista ordenada alfabéticamente con los nombres de las personas que se ubiquen en salidas de emergencia, que son las filas 2, 11 y 18.

Esta lista se debe mostrar por pantalla con los nombres separados por punto y coma (`;`) y en MAYÚSCULAS.

- Para filtrar los nombres, deberás crear una función auxiliar que reciba el array **`PASSENGERS`** por parámetro y devuelva un nuevo array solo con los nombres que cumplan la condición.

---

### Código base

Copia y pega este código en tu archivo Python. No modifiques las funciones generadoras ni los datos base.

```python
import random


def array_generator() -> list[str]:
    available_seats = []
    seats = ["A", "B", "C", "D", "E", "F"]

    for row in range(1, 21):
        random_seat_1 = random.randrange(len(seats))
        random_seat_2 = random.randrange(len(seats))

        available_seats.append(f"{row}-{seats[random_seat_1]}")
        if random_seat_1 != random_seat_2:
            available_seats.append(f"{row}-{seats[random_seat_2]}")

    return available_seats


PASSENGERS: list[str | int] = [
  "Aina",
  1,
  "Bruno",
  18,
  "Carla",
  3,
  "Diego",
  6,
  "Elisa",
  4,
  "Ferran",
  2,
  "Gina",
  11,
  "Hugo",
  17,
  "Irene",
  1,
  "Joan",
  18,
  "Karla",
  3,
  "Luis",
  6,
  "Marta",
  4,
  "Nico",
  12,
  "Olga",
  5,
  "Pau",
  7,
  "Quim",
  11,
  "Rosa",
  8,
  "Sergi",
  2,
  "Tania",
  4,
]
```
