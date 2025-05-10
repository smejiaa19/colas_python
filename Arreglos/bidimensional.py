def crea_array_doble():
    """
    Proceso CreaArrayDoble
    Crea una matriz (lista de listas) de 2x3, 
    toma la entrada del usuario para llenarla, y luego imprime la matriz.
    """

    # Dimension A[2,3]  (Equivalente en Python: una lista de listas)
    A = [[0] * 3 for _ in range(2)]  # Crea una matriz de 2 filas y 3 columnas, inicializada con 0s.


    for i in range(2):  # range(2) va de 0 a 1.
        for j in range(3):  # range(3) va de 0 a 2.
            print("Escriba el valor a almacenar")
            # Leer A[i,j]
            A[i][j] = input()  # Leer la entrada del usuario y guardarla en A[i][j].

    for i in range(2):
        for j in range(3):
            # Escribir "A[",i,",",j,"]=",A[i,j]
            print(f"A[{i},{j}]={A[i][j]}")  # Imprime el valor de A[i][j] con formato.

# Ejemplo de cómo llamar a la función:
crea_array_doble()
