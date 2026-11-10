# EXAMEN FINAL: Programación Orientada a Objetos

## Información importante

- Dispones de **3 horas** para realizar el examen.
- Todas las búsquedas, sumas y recorridos deben programarse **a mano** usando bucles clásicos:
  - `for`
  - `while`
- Al finalizar, entrega todo en **una única carpeta comprimida** por mensaje de Discord al mentor.
- Puedes consultar internet, apuntes y ejercicios previos del curso.
- Si te trabas con la lógica de algún ejercicio, deja comentado en el código cómo planeabas resolverlo (pseudocódigo).  
  **Esto suma puntos**: es mejor mostrar razonamiento que dejarlo en blanco.

## Enunciado

Una importante cadena de franquicias de gimnasios necesita una aplicación para administrar la información de sus centros, los socios que se apuntan y los empleados que mantienen todo funcionando.

En nuestra aplicación, trabajaremos con una lista global de gimnasios. De cada **Gym** nos interesa guardar: `name`, `city`, `capacity`, `openingTime`, `closingTime`, su lista de empleados y su lista de socios.

De cada **Member** queremos guardar su `dni`, `creditCard`, `email`, `age`, `height` y `weight`. El `dni` se podrá leer, pero no modificar directamente desde fuera de la clase. El `creditCard`, en cambio, se podrá modificar, pero al leerla, solo se deben mostrar los ultimos 4 numeros. También tendrá una rutina principal. De cada **Routine** se guardara un `title`, su `duration` y la cantidad de `exercises`.

Por otra parte, cada **Employee** registrará su `name`, su `dni` y las `contractHours`. Sin embargo, no existen empleados genéricos: cada uno tendrá un rol en particular, lo que define cómo funciona su método `calculateSalary()`. Asumiremos un `baseSalary` de **1000 €**.

* **Coach:** Además del sueldo base, guardará una propiedad `monthlyClasses` con la cantidad de clases que tiene al mes y recibirá un plus de **40 €** por cada clase impartida.

* **Receptionist:** Además del sueldo base. Guardará una propiedad `overtimeHours` con sus horas extra, por las que cobrará **30 €** extra (cada una). Y si tiene más de 10 horas extra, se agregará un bono de **100 €** más.

---

## Aplicación (`main.py`)

La aplicación debe contar con un menú interactivo en la terminal que mantenga el registro global de `Gym`. A través de la interfaz, el sistema debe permitir realizar estas 5 operativas:

1. **Crear un `Gym`** y agregarlo al sistema mediante una opción del menú. 
   **Aclaración:** _El sistema debe impedir que se registren dos gimnasios con el mismo nombre, mostrando un error si sucede (recuerda validar mayúsculas y minúsculas). Al crearse, el gimnasio debe inicializarse vacío, con 0 empleados y 0 miembros._

2. **Mostrar** La cantidad de empleados que hay en toda la plataforma (contando todos los gimnasios).

3. **Calcular y mostrar** El porcentaje de ocupación de un gimnasio concreto. El usuario introducirá el nombre de un gimnasio por pantalla para identificar cuál gimnasio corresponde, y se debe mostrar el porcentaje ocupado del gimnasio.

4. **Mostrar por pantalla** el nombre de los gimnasios que tengan capacidad para **200 o más** personas. (Puedes mostrar una lista con los nombres)

5. **Mostrar por pantalla** el nombre de los **Coach** que hayan impartido al menos **20 clases**. Si no hay, mostrar en pantalla: `"Aún no hay profesores con +20 clases impartidas."`
---
**Tip: Puedes crear una lista de gimnasios de ejemplo para trabajar con esos datos y ahorrar tiempo.**