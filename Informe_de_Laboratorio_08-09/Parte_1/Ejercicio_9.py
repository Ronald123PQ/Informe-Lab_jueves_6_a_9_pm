#9. Asegurar que un módulo se ha importado correctamente.

import sys
# Intenta importar el módulo datetime
try:
    import datetime
    modulo_importado = True
except ImportError:
    modulo_importado = False

# Verificar si el módulo se ha importado correctamente
assert modulo_importado, "Error: No se pudo importar el módulo datetime correctamente"
print("El módulo datetime se ha importado correctamente")