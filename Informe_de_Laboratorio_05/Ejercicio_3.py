# Ejercicio 03:Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que son divisibles por un número determinado.

def numeros_divisibles(conjunto, divisor):
    # Crea un conjunto vacío para almacenar los números divisibles
    divisibles = set()
    # Itera sobre cada número en el conjunto dado
    for numero in conjunto:
        # Verifica si el número es divisible por el divisor dado
        if numero % divisor == 0:
            # Si el número es divisible, lo agrega al conjunto de divisibles
            divisibles.add(numero)
    # Devuelve el conjunto de números divisibles
    return divisibles

# Conjunto de números de ejemplo
conjunto_de_numeros = {2, 3, 5, 7, 10, 13, 15}
# Divisor para encontrar los números divisibles
divisor = 5
# Llama a la función para encontrar los números divisibles por el divisor dado
conjunto_divisible = numeros_divisibles(conjunto_de_numeros, divisor)

# Imprime el conjunto de números y los números divisibles por el divisor
print("Conjunto de números:", conjunto_de_numeros)
print(f"Números divisibles por {divisor}:", conjunto_divisible)