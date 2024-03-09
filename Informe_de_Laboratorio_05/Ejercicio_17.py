# Ejercicio 17:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que tienen una longitud determinada y están ordenadas de menor a mayor.

def palabras_con_longitud_ordenadas(conjunto_palabras, longitud):
    # Crea un conjunto de palabras que tienen la longitud deseada
    palabras_seleccionadas = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    # Ordena las palabras seleccionadas y las convierte en una lista
    palabras_ordenadas = sorted(palabras_seleccionadas)
    return set(palabras_ordenadas)

# Conjunto de palabras de ejemplo
conjunto_de_palabras = {"gato", "perro", "casa", "luz", "sol", "flor"}
# Longitud de palabras deseada
longitud_deseada = 4
# Llama a la función para obtener palabras con la longitud deseada, ordenadas
palabras_seleccionadas_ordenadas = palabras_con_longitud_ordenadas(conjunto_de_palabras, longitud_deseada)

# Imprime el conjunto de palabras original y las palabras seleccionadas con la longitud deseada, ordenadas
print("Conjunto de palabras:", conjunto_de_palabras)
print(f"Palabras con longitud {longitud_deseada} ordenadas:", palabras_seleccionadas_ordenadas)