# Ejercicio 18:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada y están ordenadas de mayor a menor.

def palabras_con_letra(palabras, letra):
    # Filtra las palabras que contienen la letra especificada
    palabras_filtradas = [palabra for palabra in palabras if letra in palabra]
    # Ordena las palabras filtradas de mayor a menor
    palabras_ordenadas = sorted(palabras_filtradas, reverse=True)
    return palabras_ordenadas

# Conjunto de palabras de ejemplo
conjunto_palabras = {"manzana", "banana", "pera", "uva", "piña", "melon", "pepino", "arandano"}
# Letra a buscar en las palabras
letra_determinada = "a"
# Llama a la función para obtener palabras con la letra especificada, ordenadas de mayor a menor
resultado = palabras_con_letra(conjunto_palabras, letra_determinada)
print("Palabras con la letra '{}' ordenadas de mayor a menor:".format(letra_determinada))
print(resultado)