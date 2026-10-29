# Conceptes de la Programació Orientada a Objectes (POO) en Python

## Enunciat (corregit)

> Defineix i explica els següents conceptes de la Programació Orientada a Objectes en Python, amb exemples de codi en Markdown:
>
> - Classe
> - Objecte
> - `new`
> - Encapsulació
> - _Getters_ i _setters_
> - Sobrecàrrega
> - Herència
> - Herència múltiple
> - Abstracció
> - Polimorfisme
> - `this` i `super`
> - `static`
> - `final`
> - Interfície

> **Nota:** tots els exemples utilitzen **anotacions de tipus** (_type hints_) i requereixen Python 3.10 o superior.

---

## Índex

1. [Classe](#1-classe)
2. [Objecte](#2-objecte)
3. [`new`](#3-new)
4. [Encapsulació](#4-encapsulació)
5. [_Getters_ i _setters_](#5-getters-i-setters)
6. [Sobrecàrrega](#6-sobrecàrrega)
7. [Herència](#7-herència)
8. [Herència múltiple](#8-herència-múltiple)
9. [Abstracció](#9-abstracció)
10. [Polimorfisme](#10-polimorfisme)
11. [`this` i `super`](#11-this-i-super)
12. [`static`](#12-static)
13. [`final`](#13-final)
14. [Interfície](#14-interfície)
15. [Taula resum](#taula-resum)

---

## 1. Classe

Una **classe** és una plantilla (o «plànol») que defineix els **atributs** (dades) i els **mètodes** (comportament) dels objectes que se'n creïn.

```python
class Cotxe:
    def __init__(self, marca: str, model: str) -> None:
        self.marca: str = marca    # atribut
        self.model: str = model    # atribut

    def arrencar(self) -> None:    # mètode
        print(f"El {self.marca} {self.model} arrenca.")
```

---

## 2. Objecte

Un **objecte** és una **instància** concreta d'una classe. Cada objecte té el seu propi estat.

```python
cotxe1: Cotxe = Cotxe("Seat", "Ibiza")
cotxe2: Cotxe = Cotxe("Toyota", "Yaris")

cotxe1.arrencar()   # El Seat Ibiza arrenca.
cotxe2.arrencar()   # El Toyota Yaris arrenca.

print(cotxe1 is cotxe2)  # False: són objectes diferents
```

---

## 3. `new`

A Python **no existeix** la paraula clau `new` (com a Java o C++). Per crear un objecte, simplement **es crida la classe** com si fos una funció.

Internament, Python executa dos mètodes especials:

- `__new__(cls, ...)`: **crea** l'objecte (reserva memòria).
- `__init__(self, ...)`: **inicialitza** l'objecte ja creat.

```python
from typing import Any


class Persona:
    def __new__(cls, *args: Any, **kwargs: Any) -> "Persona":
        print("1. __new__: creant l'objecte")
        return super().__new__(cls)

    def __init__(self, nom: str) -> None:
        print("2. __init__: inicialitzant l'objecte")
        self.nom: str = nom


p: Persona = Persona("Anna")   # No cal «new»
# 1. __new__: creant l'objecte
# 2. __init__: inicialitzant l'objecte
```

---

## 4. Encapsulació

Consisteix a **amagar l'estat intern** d'un objecte i a controlar-ne l'accés. Python no té modificadors estrictes (`private`, `public`), sinó **convencions**:

| Sintaxi     | Significat                                         |
| ----------- | -------------------------------------------------- |
| `atribut`   | Públic                                             |
| `_atribut`  | Protegit (convenció: ús intern i per a subclasses) |
| `__atribut` | Privat (Python aplica _name mangling_)             |

```python
class CompteBancari:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular: str = titular        # públic
        self._iban: str = "ES00..."        # protegit (convenció)
        self.__saldo: float = saldo        # privat

    def ingressar(self, quantitat: float) -> None:
        if quantitat > 0:
            self.__saldo += quantitat

    def consultar_saldo(self) -> float:
        return self.__saldo


compte: CompteBancari = CompteBancari("Joan", 1000)
compte.ingressar(500)
print(compte.consultar_saldo())        # 1500

# print(compte.__saldo)                # AttributeError
print(compte._CompteBancari__saldo)    # 1500 (name mangling; no recomanable)
```

---

## 5. _Getters_ i _setters_

Els **getters** i **setters** permeten llegir i modificar atributs privats de manera controlada. A Python es fan amb el decorador **`@property`** (la forma _pythonica_).

```python
class Persona:
    def __init__(self, nom: str, edat: int) -> None:
        self.__nom: str = nom
        self.__edat: int = edat

    # GETTER
    @property
    def edat(self) -> int:
        return self.__edat

    # SETTER amb validació
    @edat.setter
    def edat(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("L'edat no pot ser negativa")
        self.__edat = valor


p: Persona = Persona("Marta", 30)
print(p.edat)    # 30 (crida al getter)
p.edat = 31      # crida al setter
# p.edat = -5    # ValueError
```

---

## 6. Sobrecàrrega

Python **no admet la sobrecàrrega de mètodes** clàssica (mateix nom amb signatures diferents): si es defineix un mètode dos cops, l'últim sobreescriu l'anterior. S'emula de diverses maneres.

### a) `*args` i paràmetres per defecte

```python
class Calculadora:
    def sumar(self, *args: float) -> float:
        return sum(args)


c: Calculadora = Calculadora()
print(c.sumar(1, 2))         # 3
print(c.sumar(1, 2, 3, 4))   # 10
```

### b) `@overload` (només per a l'analitzador de tipus)

```python
from typing import overload


class Saludador:
    @overload
    def saludar(self, nom: str) -> str: ...
    @overload
    def saludar(self, nom: str, cognom: str) -> str: ...

    def saludar(self, nom: str, cognom: str | None = None) -> str:
        if cognom is None:
            return f"Hola, {nom}!"
        return f"Hola, {nom} {cognom}!"
```

> `@overload` només serveix per documentar les signatures i per a eines com _mypy_; l'execució real la fa l'única implementació final.

### c) `functools.singledispatchmethod` (segons el tipus)

```python
from functools import singledispatchmethod
from typing import Any


class Processador:
    @singledispatchmethod
    def processar(self, valor: Any) -> None:
        raise NotImplementedError("Tipus no suportat")

    @processar.register
    def _(self, valor: int) -> None:
        print(f"Enter: {valor * 2}")

    @processar.register
    def _(self, valor: str) -> None:
        print(f"Text: {valor.upper()}")


proc: Processador = Processador()
proc.processar(5)        # Enter: 10
proc.processar("hola")   # Text: HOLA
```

### d) Sobrecàrrega d'operadors (mètodes màgics)

```python
from __future__ import annotations


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __add__(self, altre: Vector) -> Vector:
        return Vector(self.x + altre.x, self.y + altre.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


print(Vector(1, 2) + Vector(3, 4))   # (4, 6)
```

---

## 7. Herència

Permet que una classe (**filla**) hereti atributs i mètodes d'una altra (**pare**), cosa que afavoreix la reutilització de codi.

```python
class Animal:
    def __init__(self, nom: str) -> None:
        self.nom: str = nom

    def menjar(self) -> None:
        print(f"{self.nom} està menjant.")


class Gos(Animal):             # Gos hereta d'Animal
    def bordar(self) -> None:
        print(f"{self.nom} diu: Guau!")


g: Gos = Gos("Rex")
g.menjar()   # heretat d'Animal
g.bordar()   # propi de Gos
```

---

## 8. Herència múltiple

Una classe pot heretar de **més d'una classe pare**. Python resol l'ordre de cerca amb el **MRO** (_Method Resolution Order_, algorisme C3).

```python
class Volador:
    def moure(self) -> None:
        print("Vola pel cel")


class Nedador:
    def moure(self) -> None:
        print("Neda per l'aigua")


class Anec(Volador, Nedador):
    pass


a: Anec = Anec()
a.moure()                 # Vola pel cel (Volador va primer)
print(Anec.__mro__)
# (<class 'Anec'>, <class 'Volador'>, <class 'Nedador'>, <class 'object'>)
```

---

## 9. Abstracció

Consisteix a **mostrar només el que és essencial** i amagar els detalls d'implementació. A Python s'implementa amb el mòdul **`abc`** (_Abstract Base Classes_). Una classe abstracta **no es pot instanciar** i obliga les classes filles a implementar els mètodes abstractes.

```python
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    def descripcio(self) -> None:      # mètode concret
        print(f"Àrea: {self.area()}")


class Cercle(Figura):
    def __init__(self, radi: float) -> None:
        self.radi: float = radi

    def area(self) -> float:
        return 3.1416 * self.radi ** 2


# f = Figura()        # TypeError: no es pot instanciar
c: Cercle = Cercle(2)
c.descripcio()        # Àrea: 12.5664
```

---

## 10. Polimorfisme

És la capacitat que **objectes de classes diferents responguin al mateix mètode** de maneres diferents.

### a) _Duck typing_

```python
class Gat:
    def so(self) -> str:
        return "Mèu"


class Gos:
    def so(self) -> str:
        return "Guau"


class Vaca:
    def so(self) -> str:
        return "Muuu"


animals: list[Gat | Gos | Vaca] = [Gat(), Gos(), Vaca()]

for animal in animals:
    print(animal.so())   # Cada objecte respon a la seva manera
```

Python utilitza **_duck typing_**: «si camina com un ànec i fa quac com un ànec, és un ànec». No cal una herència comuna.

### b) Sobreescriptura (_override_)

```python
class Animal:
    def so(self) -> str:
        return "..."


class Gos(Animal):
    def so(self) -> str:       # sobreescriu el mètode del pare
        return "Guau"


animal: Animal = Gos()
print(animal.so())             # Guau
```

---

## 11. `this` i `super`

### `this` → `self`

Python no té `this`; l'equivalent és **`self`**, la referència a l'objecte actual (primer paràmetre de cada mètode d'instància).

### `super()`

Permet accedir als mètodes de la **classe pare**.

```python
class Vehicle:
    def __init__(self, marca: str) -> None:
        self.marca: str = marca

    def descriure(self) -> str:
        return f"Vehicle de la marca {self.marca}"


class Moto(Vehicle):
    def __init__(self, marca: str, cilindrada: int) -> None:
        super().__init__(marca)             # crida al constructor del pare
        self.cilindrada: int = cilindrada   # self: l'objecte actual

    def descriure(self) -> str:
        base: str = super().descriure()     # reutilitza el mètode del pare
        return f"{base} amb {self.cilindrada} cc"


m: Moto = Moto("Honda", 600)
print(m.descriure())   # Vehicle de la marca Honda amb 600 cc
```

---

## 12. `static`

Els membres **estàtics** pertanyen a la **classe**, no a les instàncies.

| Tipus             | Decorador       | Rep   | Ús                                            |
| ----------------- | --------------- | ----- | --------------------------------------------- |
| Atribut de classe | (cap)           | —     | Dada compartida per tots els objectes         |
| `@classmethod`    | `@classmethod`  | `cls` | Accedeix a l'estat de la classe o el modifica |
| `@staticmethod`   | `@staticmethod` | res   | Funció utilitària dins la classe              |

```python
class Empleat:
    num_empleats: int = 0                 # atribut de classe (compartit)

    def __init__(self, nom: str) -> None:
        self.nom: str = nom
        Empleat.num_empleats += 1

    @classmethod
    def total(cls) -> int:
        return cls.num_empleats

    @staticmethod
    def es_major_d_edat(edat: int) -> bool:
        return edat >= 18


e1: Empleat = Empleat("Pau")
e2: Empleat = Empleat("Laia")

print(Empleat.total())                # 2
print(Empleat.es_major_d_edat(20))    # True
```

---

## 13. `final`

Python **no té** la paraula clau `final`, però hi ha mecanismes per aconseguir un efecte similar.

### a) Constants (convenció)

```python
class Config:
    MAX_USUARIS: int = 100    # MAJÚSCULES = no s'hauria de modificar
```

### b) `typing.Final` i `@final` (només per a analitzadors estàtics com _mypy_)

```python
from typing import Final, final

PI: Final[float] = 3.1416          # constant


class Base:
    @final                          # mètode que no s'ha de sobreescriure
    def metode_fix(self) -> None:
        print("No m'has de sobreescriure")


@final                              # classe que no s'ha d'heretar
class Sellada:
    pass
```

> ⚠️ `Final` i `@final` **no s'imposen en temps d'execució**; només les detecten eines com _mypy_.

### c) Impedir realment l'herència (en execució)

```python
from typing import Any


class NoHeretable:
    def __init_subclass__(cls, **kwargs: Any) -> None:
        raise TypeError("Aquesta classe no es pot heretar")


# class Filla(NoHeretable): pass   # TypeError
```

---

## 14. Interfície

Python **no té** la paraula clau `interface`. S'implementa de dues maneres.

### a) Amb classes abstractes (`ABC`): enfocament _nominal_

Una classe que només té mètodes abstractes actua com a interfície.

```python
from abc import ABC, abstractmethod


class Volable(ABC):
    @abstractmethod
    def volar(self) -> None:
        ...

    @abstractmethod
    def aterrar(self) -> None:
        ...


class Avio(Volable):
    def volar(self) -> None:
        print("L'avió vola")

    def aterrar(self) -> None:
        print("L'avió aterra")


Avio().volar()
```

### b) Amb `Protocol`: enfocament _estructural_ (_duck typing_ tipat)

No cal heretar explícitament; només cal tenir els mètodes requerits.

```python
from typing import Protocol


class Imprimible(Protocol):
    def imprimir(self) -> None: ...


class Document:
    def imprimir(self) -> None:
        print("Imprimint document...")


def enviar_a_impressora(obj: Imprimible) -> None:
    obj.imprimir()


enviar_a_impressora(Document())   # Vàlid sense heretar d'Imprimible
```

---

## Taula resum

| Concepte            | Equivalent en Python                                     |
| ------------------- | -------------------------------------------------------- |
| Classe              | `class Nom:`                                             |
| Objecte             | `obj: Nom = Nom()`                                       |
| `new`               | `__new__` + `__init__` (no cal `new`)                    |
| Encapsulació        | `_protegit`, `__privat`                                  |
| _Getters_/_setters_ | `@property` + `@x.setter`                                |
| Sobrecàrrega        | `*args`, `@overload`, `singledispatchmethod`, `__add__`… |
| Herència            | `class Filla(Pare):`                                     |
| Herència múltiple   | `class C(A, B):` + MRO                                   |
| Abstracció          | `ABC` + `@abstractmethod`                                |
| Polimorfisme        | Sobreescriptura + _duck typing_                          |
| `this` / `super`    | `self` / `super()`                                       |
| `static`            | `@staticmethod`, `@classmethod`, atributs de classe      |
| `final`             | `typing.Final`, `@final` (no s'imposen en execució)      |
| Interfície          | `ABC` pura o `Protocol`                                  |
