# Ejercicio 02:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que comienzan con una letra determinada.

def palabras_que_comienzan_con_letra(palabras, letra):
    # Crea un conjunto vacío para almacenar las palabras que comienzan con la letra dada
    palabras_comienzan_con_letra = set()

    # Itera sobre cada palabra en el conjunto de palabras dado
    for palabra in palabras:
        # Verifica si la palabra comienza con la letra dada
        if palabra.startswith(letra):
            # Si la palabra comienza con la letra, la agrega al conjunto de palabras
            palabras_comienzan_con_letra.add(palabra)

    # Devuelve el conjunto de palabras que comienzan con la letra dada
    return palabras_comienzan_con_letra

# Conjunto de palabras de ejemplo
conjunto_palabras = {"manzana", "banana", "pera", "sandía", "limón", "uva", "mora"}
# Letra con la que se compararán las palabras
letra = "m"
# Llama a la función para encontrar las palabras que comienzan con la letra dada
resultado = palabras_que_comienzan_con_letra(conjunto_palabras, letra)
# Imprime las palabras que comienzan con la letra dada
print("Palabras que comienzan con la letra '{}':".format(letra))
print(resultado)