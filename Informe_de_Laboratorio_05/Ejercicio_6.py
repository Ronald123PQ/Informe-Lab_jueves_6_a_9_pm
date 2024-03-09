# Ejercicio 06:Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en el segundo conjunto pero no en el primero.

def numeros_en_segundo_no_en_primero(conjunto1, conjunto2):
    # Calcula la diferencia entre el segundo conjunto y el primero utilizando el método difference()
    numeros_resultado = conjunto2.difference(conjunto1)
    return numeros_resultado

# Conjuntos de ejemplo
conjunto_numeros1 = {1, 2, 3, 4, 5}
conjunto_numeros2 = {4, 5, 6, 7, 8}

# Llama a la función para encontrar los números en el segundo conjunto pero no en el primero
resultado = numeros_en_segundo_no_en_primero(conjunto_numeros1, conjunto_numeros2)

# Imprime los resultados
print("Números en el segundo conjunto pero no en el primero:")
print(resultado)