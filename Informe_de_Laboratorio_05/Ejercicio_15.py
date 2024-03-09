# Ejercicio 15:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son primos y están ordenados de menor a mayor.

def es_primo(numero):
    # Verifica si el número es menor que 2, en cuyo caso no es primo
    if numero < 2:
        return False
    # Itera sobre los números desde 2 hasta la raíz cuadrada del número (int(numero**0.5) + 1)
    for i in range(2, int(numero**0.5) + 1):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True

def primos_ordenados(conjunto_numeros):
    # Crea un conjunto de primos filtrando los números del conjunto utilizando la función es_primo
    primos = {numero for numero in conjunto_numeros if es_primo(numero)}
    # Ordena los primos encontrados y los convierte nuevamente en un conjunto
    primos_ordenados = sorted(primos)
    return set(primos_ordenados)

# Conjunto de números de ejemplo
conjunto_de_numeros = {2, 3, 5, 7, 10, 13, 15}
# Llama a la función para obtener los primos ordenados del conjunto de números
conjunto_primos_ordenados = primos_ordenados(conjunto_de_numeros)

# Imprime el conjunto original de números y el conjunto de primos ordenados
print("Conjunto de números:", conjunto_de_numeros)
print("Conjunto de primos ordenados:", conjunto_primos_ordenados)