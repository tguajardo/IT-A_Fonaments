# Fer un programa que pregunti a l'usuari/ària pel nombre (número) de paraules que es volen introduir en una llista.
# Un cop l'usuari/ària respongui, el programa haurà de preguntar per tantes paraules com el nombre (número) de paraules que ha dit l’usuari/ària que volia introduir.
# Les paraules s'aniran guardant a la llista i un cop han sigut totes introduïdes, es mostren per pantalla.


# Variables
num_par: int
llista: list[str] = []

# input
in_num_par: str = input("Quantas paraulas vols introduir?: ")
if in_num_par.isdigit():
    num_par = int(in_num_par)
    if num_par == 0:
        print("El nombre de paraules ha de ser positiu.")
        exit()
else:
    print("El nombre de paraules ha de ser positiu.")
    exit()

# operation
for index in range(num_par):
    llista.append(input(f"Introdueix la paraula {index + 1}: "))

# output
print("Has introduit aquestes paraules: ")
print(llista)
