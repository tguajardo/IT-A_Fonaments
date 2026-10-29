lista = ["a", "b", "c", "d"]

elementToDelete = ""  # 0    1    2
for element in lista:  # ["b", "c", "d"]
    if element == "a":
        elementToDelete = element
if elementToDelete != "":
    lista.remove(elementToDelete)

print(lista)

indexToDelete = -1
for index in range(len(lista)):
    if lista[index] == "c":
        indexToDelete = index

if indexToDelete != -1:
    lista.pop(indexToDelete)

print(lista)
