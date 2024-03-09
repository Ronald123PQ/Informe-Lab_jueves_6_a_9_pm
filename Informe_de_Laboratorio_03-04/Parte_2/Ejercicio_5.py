# Ejercicio 5: Escribe una función que encuentre la matriz de covarianza de dos matrices.

import numpy as np
# Importa la biblioteca NumPy para trabajar con matrices y operaciones numéricas

def matriz_covarianza(X, Y):
    # Comprueba si el número de observaciones en X e Y es el mismo
    if X.shape[0] != Y.shape[0]:
        raise ValueError("Las matrices deben tener el mismo número de observaciones")

    # Calcula las medias de las filas de las matrices X e Y
    mean_X = np.mean(X, axis=1, keepdims=True)
    mean_Y = np.mean(Y, axis=1, keepdims=True)

    # Obtiene el número de observaciones en las matrices X e Y
    n = X.shape[1]

    # Crea una matriz de ceros para almacenar la matriz de covarianza
    cov_matrix = np.zeros((X.shape[0], Y.shape[0]))

    # Calcula la covarianza entre las filas de X e Y
    for i in range(X.shape[0]):  # Recorre las filas de la matriz X
        for j in range(Y.shape[0]):  # Recorre las filas de la matriz Y
            # Calcula la covarianza entre la fila i de X y la fila j de Y
            cov_matrix[i, j] = np.sum((X[i, :] - mean_X[i]) * (Y[j, :] - mean_Y[j])) / n

    return cov_matrix

X = np.array([[1, 2, 3], [4, 5, 6]])  # Definición de la matriz X
Y = np.array([[7, 8, 9], [10, 11, 12]])  # Definición de la matriz Y

# Llama a la función para calcular la matriz de covarianza entre X e Y
covariance_matrix = matriz_covarianza(X, Y)

# Imprime la matriz de covarianza resultante
print("Matriz de covarianza entre X e Y:")
print(covariance_matrix)