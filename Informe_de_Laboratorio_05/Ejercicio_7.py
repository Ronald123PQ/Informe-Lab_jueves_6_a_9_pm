# Ejercicio 07:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas.

def son_anagramas(palabra1, palabra2):
    # Comprueba si las palabras son anagramas ordenando sus letras y comparando los resultados
    return sorted(palabra1) == sorted(palabra2)

def anagramas_en_conjunto(conjunto):
    anagramas = set()

    # Itera sobre cada palabra en el conjunto
    for palabra1 in conjunto:
        for palabra2 in conjunto:
            # Verifica si las palabras son diferentes y son anagramas
            if palabra1 != palabra2 and son_anagramas(palabra1, palabra2):
                # Si son anagramas, agrega ambas palabras al conjunto de anagramas
                anagramas.add(palabra1)
                anagramas.add(palabra2)

    return anagramas

# Conjunto de palabras de ejemplo
conjunto_de_palabras = {"hola", "aloh", "mundo", "samir", "juan"}

# Encuentra los anagramas en el conjunto de palabras
conjunto_de_anagramas = anagramas_en_conjunto(conjunto_de_palabras)

# Imprime el conjunto de palabras que son anagramas
print("El conjunto de palabras anagramas son:", conjunto_de_anagramas)