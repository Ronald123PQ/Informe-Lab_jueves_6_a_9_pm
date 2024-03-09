# Ejercicio 11: Multiplica una matriz por un número.

import numpy as np # Importa la biblioteca numpy para trabajar con matrices y operaciones numéricas.

# Define una función llamada crear_matriz que crea una matriz con valores ingresados por el usuario.
def crear_matriz(filas, columnas):
    # Crea una matriz de ceros con las dimensiones especificadas por el usuario.
    matriz = np.zeros((filas, columnas), dtype=float)

    # Recorre cada posición de la matriz y solicita al usuario que ingrese el valor para esa posición.
    for i in range(filas):
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor para la posición {i+1},{j+1}: "))
            # Solicita al usuario que ingrese el valor para la posición i, j.
            matriz[i, j] = valor  # Asigna el valor ingresado a la posición correspondiente en la matriz.

    return matriz  # Retorna la matriz creada por el usuario.

# Define una función llamada multiplicar_matriz_por_numero que multiplica una matriz por un número.
def multiplicar_matriz_por_numero(matriz, numero):
    return matriz * numero  # Retorna la matriz resultante de la multiplicación por el número especificado.

# Solicita al usuario el número de filas y columnas para la matriz.
filas = int(input("Ingrese el número de filas: "))  # Solicita al usuario el número de filas para la matriz.
columnas = int(input("Ingrese el número de columnas: "))  # Solicita al usuario el número de columnas para la matriz.

# Crea la matriz con los valores ingresados por el usuario.
matriz = crear_matriz(filas, columnas)

# Solicita al usuario el número por el cual desea multiplicar la matriz.
numero = int(input("Ingrese el número por el cual desea multiplicar la matriz: "))

# Multiplica la matriz por el número especificado por el usuario.
matriz_resultante = multiplicar_matriz_por_numero(matriz, numero)

# Imprime la matriz original y la matriz resultante.
print("\nMatriz original:")
print(matriz)
print("\nMatriz multiplicada por", numero, ":")
print(matriz_resultante)