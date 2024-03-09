# Ejercicio 13:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que están duplicados.

def numeros_duplicados(conjunto_numeros):
    # Conjunto para almacenar los números duplicados
    numeros_duplicados = set()
    # Conjunto para almacenar los números vistos
    numeros_vistos = set()

    # Itera a través de cada número en el conjunto de números
    for numero in conjunto_numeros:
        # Verifica si el número ya ha sido visto
        if numero in numeros_vistos:
            # Si el número ya ha sido visto, lo agrega al conjunto de números duplicados
            numeros_duplicados.add(numero)
        else:
            # Si el número no ha sido visto, lo agrega al conjunto de números vistos
            numeros_vistos.add(numero)

    # Devuelve el conjunto de números duplicados
    return numeros_duplicados

# Conjunto de números de ejemplo con duplicados
conjunto_de_numeros = {1, 2, 3, 2, 4, 5, 3, 6}
# Llama a la función para encontrar los números duplicados en el conjunto
conjunto_duplicados = numeros_duplicados(conjunto_de_numeros)

# Imprime el conjunto de números original y el conjunto de números duplicados
print("Conjunto de números:", conjunto_de_numeros)
print("Conjunto de números duplicados:", conjunto_duplicados)