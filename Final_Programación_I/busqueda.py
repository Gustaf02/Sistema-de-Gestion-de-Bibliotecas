from func_aux import cargar_datos

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para buscar libros por título
def buscar_libro_por_titulo(titulo):
    libros = cargar_datos('libros.json')
    resultado = [libro for libro in libros if titulo.lower() in libro['titulo'].lower()]
    return resultado

# Función para buscar libros por género
def buscar_libro_por_genero(genero):
    libros = cargar_datos('libros.json')
    resultado = [libro for libro in libros if genero.lower() in libro['genero'].lower()]
    return resultado

# Función para buscar libros por autor
def buscar_libro_por_autor(autor):
    libros = cargar_datos('libros.json')
    resultado = [libro for libro in libros if autor.lower() in libro['autor'].lower()]
    return resultado

# Función para buscar libros por editorial
def buscar_libro_por_editorial(editorial):
    libros = cargar_datos('libros.json')
    resultado = [libro for libro in libros if editorial.lower() in libro['editorial'].lower()]
    return resultado

