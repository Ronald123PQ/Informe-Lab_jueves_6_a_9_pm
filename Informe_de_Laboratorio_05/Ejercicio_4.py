# Ejercicio 04:Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos.

def numeros_en_ambos_conjuntos(conjunto1, conjunto2):
    # Encuentra los números comunes a ambos conjuntos usando el método intersection()
    numeros_comunes = conjunto1.intersection(conjunto2)
    return numeros_comunes

# Conjuntos de números de ejemplo
conjunto_numeros1 = {1, 2, 3, 4, 5}
conjunto_numeros2 = {4, 5, 6, 7, 8}

# Llama a la función para encontrar los números comunes en ambos conjuntos
resultado = numeros_en_ambos_conjuntos(conjunto_numeros1, conjunto_numeros2)

# Imprime los números que están en ambos conjuntos
print("Números en ambos conjuntos:")
print(resultado)