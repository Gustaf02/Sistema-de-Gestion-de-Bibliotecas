import json

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para cargar datos
def cargar_datos(archivo):
    with open(archivo, 'r') as f:
        return json.load(f)

# Función para guardar datos
def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

# Función para obtener un nuevo ID para un elemento
def obtener_nuevo_id(lista):
    if lista:
        return max(item['id'] for item in lista) + 1
    return 1



