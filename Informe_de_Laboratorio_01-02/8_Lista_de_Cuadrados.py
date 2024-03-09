#8)Crea una lista de los cuadrados de los primeros 10 números naturales.

# Definición de la función calcular_cuadrados_primeros_naturales que calcula los cuadrados de los primeros números naturales
def calcular_cuadrados_primeros_naturales(cantidad):
    # Genera una lista de cuadrados utilizando comprensión de listas
    cuadrados = [n**2 for n in range(1, cantidad + 1)]
    return cuadrados

# Define la cantidad de números naturales cuyos cuadrados se calcularán
cantidad_numeros = 10

# Llama a la función calcular_cuadrados_primeros_naturales con la cantidad de números especificados
lista_cuadrados = calcular_cuadrados_primeros_naturales(cantidad_numeros)

# Imprime la lista de cuadrados de los primeros números naturales
print(f"Lista de cuadrados de los primeros {cantidad_numeros} números naturales:")
print(lista_cuadrados)