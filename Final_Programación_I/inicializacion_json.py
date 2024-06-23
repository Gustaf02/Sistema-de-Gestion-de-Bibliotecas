import os  # Importar el módulo os para interactuar con el sistema operativo. Útil para contexto relacionados. 
import json  # Importar el módulo json para trabajar con archivos JSON

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para inicializar archivos JSON con datos vacíos
def inicializar_json():
    # Crear listas vacías para libros, socios y préstamos
    libros = []
    socios = []
    prestamos = []
    
    # Abrir (o crear si no existe) el archivo 'libros.json' en modo escritura
    # y escribir la lista vacía de libros en formato JSON
    with open('libros.json', 'w') as f:
        json.dump(libros, f, indent=4)  # indent=4 para una mejor legibilidad del archivo JSON
    
    # Abrir (o crear si no existe) el archivo 'socios.json' en modo escritura
    # y escribir la lista vacía de socios en formato JSON
    with open('socios.json', 'w') as f:
        json.dump(socios, f, indent=4)  # indent=4 para una mejor legibilidad del archivo JSON
    
    # Abrir (o crear si no existe) el archivo 'prestamos.json' en modo escritura
    # y escribir la lista vacía de préstamos en formato JSON
    with open('prestamos.json', 'w') as f:
        json.dump(prestamos, f, indent=4)  # indent=4 para una mejor legibilidad del archivo JSON

# Llamar a la función inicializar_json() si este archivo se ejecuta directamente
if __name__ == "__main__":
    inicializar_json()  # Inicializa los archivos JSON con datos vacíos

# Llamar a la función inicializar_json() al inicio del script principal
if __name__ == "__main__":
    inicializar_json()
