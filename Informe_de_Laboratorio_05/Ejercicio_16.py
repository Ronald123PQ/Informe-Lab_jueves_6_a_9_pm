# Ejercicio 16:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos y están ordenadas de menor a mayor.

def palabras_palindromos_ordenadas(palabras):
    # Crea un conjunto para almacenar las palabras palíndromas
    palindromos = set()

    # Itera sobre cada palabra en el conjunto de palabras
    for palabra in palabras:
        # Verifica si la palabra es igual a su inversa, es decir, si es un palíndromo
        if palabra == palabra[::-1]:
            # Si es un palíndromo, agrégalo al conjunto de palíndromos
            palindromos.add(palabra)

    # Ordena los palíndromos encontrados y los convierte en una lista
    palindromos_ordenados = sorted(palindromos)

    return palindromos_ordenados

# Conjunto de palabras de ejemplo
conjunto_palabras = {"ana", "oso", "reconocer", "cívico", "radar", "python", "narran"}
# Llama a la función para obtener las palabras palíndromas ordenadas
resultado = palabras_palindromos_ordenadas(conjunto_palabras)

# Imprime las palabras palíndromas ordenadas de menor a mayor
print("Palabras palíndromos ordenadas de menor a mayor:")
print(resultado)