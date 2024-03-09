#6)Toma una cadena de texto y muestra su inversión.

# Definición de la función invertir_cadena que invierte una cadena de texto
def invertir_cadena(cadena):
    return cadena[::-1]

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Llamar a la función invertir_cadena con el texto ingresado por el usuario y almacenar el resultado
cadena_invertida = invertir_cadena(texto)

# Imprimir la cadena invertida
print(f"La cadena invertida es: {cadena_invertida}")