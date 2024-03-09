# Ejercicio 20:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.

def palabras_palindromas_longitud(words, longitud):
    # Define un conjunto para almacenar palabras palíndromas de la longitud deseada
    palabras_palindromas = set()

    # Itera sobre cada palabra en el conjunto de palabras dado
    for word in words:
        # Verifica si la longitud de la palabra es igual a la longitud deseada
        # y si la palabra es igual a su reverso (es decir, si es un palíndromo)
        if len(word) == longitud and word == word[::-1]:
            # Si es así, agrega la palabra al conjunto de palabras palíndromas
            palabras_palindromas.add(word)

    # Devuelve el conjunto de palabras palíndromas de la longitud especificada
    return palabras_palindromas

# Conjunto de palabras dado
conjunto_palabras = {"ana", "oso", "casa", "reconocer", "radar", "python", "reconocer"}
# Longitud deseada para las palabras palíndromas
longitud_deseada = 9

# Llama a la función para encontrar palabras palíndromas de la longitud especificada
palabras_palindromas = palabras_palindromas_longitud(conjunto_palabras, longitud_deseada)
# Imprime el resultado
print("Palabras palíndromas de longitud", longitud_deseada, ":", palabras_palindromas)