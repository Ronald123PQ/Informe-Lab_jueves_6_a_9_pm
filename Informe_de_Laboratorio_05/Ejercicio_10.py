# Ejercicio 10:Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que contienen una letra determinada.

def palabras_con_letra(palabras, letra):
    # Inicializa un conjunto para almacenar las palabras que contienen la letra especificada
    palabras_con_la_letra = set()

    # Itera sobre cada palabra en el conjunto de palabras
    for palabra in palabras:
        # Verifica si la letra está presente en la palabra
        if letra in palabra:
            # Si es así, agrega la palabra al conjunto de palabras con la letra
            palabras_con_la_letra.add(palabra)

    return palabras_con_la_letra

# Conjunto de palabras de ejemplo
conjunto_palabras = {"python", "programacion", "letra", "orden", "conjunto", "palabra"}
# Letra a buscar en las palabras
letra = "a"
# Encuentra las palabras que contienen la letra especificada
resultado = palabras_con_letra(conjunto_palabras, letra)

# Imprime las palabras que contienen la letra especificada
print("Palabras que contienen la letra '{}':".format(letra))
print(resultado)