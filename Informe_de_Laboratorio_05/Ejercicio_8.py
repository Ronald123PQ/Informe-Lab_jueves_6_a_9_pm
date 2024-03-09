# Ejercicio 08:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son palíndromos.

def es_palindromo(palabra):
    # Comprueba si la palabra es un palíndromo comparando la palabra original con su inversa
    return palabra == palabra[::-1]

def palabras_palindromos(conjunto_palabras):
    palindromos = set()

    # Itera sobre cada palabra en el conjunto
    for palabra in conjunto_palabras:
        # Verifica si la palabra es un palíndromo
        if es_palindromo(palabra):
            # Si es un palíndromo, agrega la palabra al conjunto de palíndromos
            palindromos.add(palabra)

    return palindromos

# Conjunto de palabras de ejemplo
conjunto_palabras = {"ala", "oso", "reconocer", "cívico", "radar", "python"}

# Encuentra las palabras que son palíndromos en el conjunto de palabras
resultado = palabras_palindromos(conjunto_palabras)

# Imprime las palabras que son palíndromos
print("Palabras que son palíndromos:")
print(resultado)