# Ejercicio 09:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada.

def palabras_con_longitud(conjunto_palabras, longitud):
    # Inicializa un conjunto para almacenar las palabras con la longitud deseada
    palabras_seleccionadas = set()

    # Itera sobre cada palabra en el conjunto de palabras
    for palabra in conjunto_palabras:
        # Verifica si la longitud de la palabra es igual a la longitud deseada
        if len(palabra) == longitud:
            # Si es así, agrega la palabra al conjunto de palabras seleccionadas
            palabras_seleccionadas.add(palabra)

    return palabras_seleccionadas

# Conjunto de palabras de ejemplo
conjunto_de_palabras = {"gato", "perro", "casa", "luz", "sol", "flor"}
# Longitud deseada de las palabras
longitud_deseada = 4
# Encuentra las palabras con la longitud deseada en el conjunto de palabras
palabras_seleccionadas = palabras_con_longitud(conjunto_de_palabras, longitud_deseada)

# Imprime el conjunto de palabras original y las palabras con la longitud deseada
print("Conjunto de palabras:", conjunto_de_palabras)
print(f"Palabras con longitud {longitud_deseada}:", palabras_seleccionadas)