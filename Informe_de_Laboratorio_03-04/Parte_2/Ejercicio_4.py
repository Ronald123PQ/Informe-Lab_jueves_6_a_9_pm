# Ejercicio 4: Escribe una función que encuentre la submatriz de mayor suma de una matriz.

import numpy as np
# NumPy es una biblioteca de Python utilizada para trabajar con matrices y operaciones matemáticas.

def submatriz_mayor_suma(matriz):
    # Define una función para encontrar la submatriz de una matriz dada que tenga la mayor suma de elementos.

    filas, columnas = matriz.shape
    # Obtiene el número de filas y columnas de la matriz.
    max_suma = float('-inf')
    # Inicializa la variable max_suma con un valor negativo grande para comparaciones.

    resultado = None
    # Inicializa la variable resultado que almacenará los índices de la submatriz con la mayor suma.

    for i in range(filas):
        # Itera sobre las filas de la matriz.
        suma_temporal = np.zeros(columnas)
        # Inicializa un array temporal de suma para cada fila.
        for j in range(i, filas):
            # Itera sobre las filas posteriores, formando submatrices.
            suma_temporal += matriz[j, :]
            # Suma las filas para formar una submatriz.
            suma_actual = np.sum(suma_temporal)
            # Calcula la suma total de la submatriz actual.

            if suma_actual > max_suma:
                # Si la suma actual es mayor que la suma máxima encontrada hasta ahora.
                max_suma = suma_actual
                # Actualiza la suma máxima.
                resultado = ((i, 0), (j, columnas - 1))
                # Almacena los índices de la submatriz con la mayor suma.

    return resultado
    # Retorna los índices de la submatriz con la mayor suma.

# Solicita al usuario que ingrese el número de filas de la matriz y lo convierte a un entero.
filas = int(input("Ingrese el número de filas: "))
# Solicita al usuario que ingrese el número de columnas de la matriz y lo convierte a un entero.
columnas = int(input("Ingrese el número de columnas: "))

# Crea una matriz aleatoria de dimensiones (filas, columnas) con valores entre -10 y 10 utilizando NumPy.
mi_matriz = np.random.randint(-10, 10, size=(filas, columnas))

print("La matriz es:")
print(mi_matriz)
# Imprime la matriz generada.

# Llama a la función submatriz_mayor_suma para encontrar la submatriz de mayor suma en la matriz.
submatriz = submatriz_mayor_suma(mi_matriz)

if submatriz is not None:
    # Si se encontró una submatriz con la mayor suma.
    print(f"La submatriz de mayor suma es:")
    # Imprime un mensaje indicando la submatriz de mayor suma.
    print(mi_matriz[submatriz[0][0]:submatriz[1][0]+1, submatriz[0][1]:submatriz[1][1]+1])
    # Imprime la submatriz de mayor suma.
else:
    print("La matriz está vacía.")
    # Imprime un mensaje indicando que la matriz está vacía si no se encontró ninguna submatriz.