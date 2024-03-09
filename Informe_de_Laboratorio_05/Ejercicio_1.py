# Ejercicio 01: Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.

def es_primo(numero):
    # Verifica si el número es menor que 2, en cuyo caso no es primo
    if numero < 2:
        return False
    # Itera desde 2 hasta el número - 1 para verificar si tiene divisores
    for i in range(2, numero):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    # Si no se encontraron divisores, el número es primo
    return True

def numeros_primos_en_conjunto(conjunto):
    # Inicializa un conjunto para almacenar los números primos
    primos = set()
    # Itera sobre cada número en el conjunto dado
    for numero in conjunto:
        # Verifica si el número es primo usando la función es_primo(numero)
        if es_primo(numero):
            # Si es primo, lo agrega al conjunto de primos
            primos.add(numero)
    # Devuelve el conjunto de números primos
    return primos

# Conjunto de números de ejemplo
conjunto_de_numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10, 23, 31}
# Encuentra los números primos en el conjunto utilizando la función numeros_primos_en_conjunto
conjunto_de_primos = numeros_primos_en_conjunto(conjunto_de_numeros)
# Imprime el conjunto de números primos
print(conjunto_de_primos)