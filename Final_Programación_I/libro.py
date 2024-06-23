from func_aux import cargar_datos, guardar_datos, obtener_nuevo_id

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para registrar un nuevo libro
def registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible):
    libros = cargar_datos('libros.json')  # Cargar los datos de los libros desde un archivo JSON

    # Verificar que todos los campos sean proporcionados
    if not titulo or not autor or not editorial or not anio_publicacion or not genero or not cantidad_disponible:
        print("Todos los campos son obligatorios.")
        return

    # Crear un diccionario con la información del libro
    libro = {
        'id': obtener_nuevo_id(libros),  # Obtener un nuevo ID para el libro
        'titulo': titulo,
        'autor': autor,
        'editorial': editorial,
        'anio_publicacion': anio_publicacion,
        'genero': genero,
        'cantidad_disponible': int(cantidad_disponible)
    }
    libros.append(libro)  # Añadir el nuevo libro a la lista de libros
    guardar_datos('libros.json', libros)  # Guardar los datos de los libros en el archivo JSON
    print("Libro registrado con éxito.")

# Función para editar un libro existente
def editar_libro(id_libro):
    libros = cargar_datos('libros.json')  # Cargar los datos de los libros desde un archivo JSON

    # Verificar que el ID del libro sea un número
    if not id_libro.isdigit():
        print("El ID del libro debe ser un número.")
        return

    id_libro = int(id_libro)
    for libro in libros:
        if libro['id'] == id_libro:  # Buscar el libro por ID
            # Permitir editar los campos del libro
            libro['titulo'] = input(f"Título [{libro['titulo']}]: ") or libro['titulo']
            libro['autor'] = input(f"Autor [{libro['autor']}]: ") or libro['autor']
            libro['editorial'] = input(f"Editorial [{libro['editorial']}]: ") or libro['editorial']
            libro['anio_publicacion'] = input(f"Año de Publicación [{libro['anio_publicacion']}]: ") or libro['anio_publicacion']
            libro['genero'] = input(f"Género [{libro['genero']}]: ") or libro['genero']
            libro['cantidad_disponible'] = int(input(f"Cantidad Disponible [{libro['cantidad_disponible']}]: ") or libro['cantidad_disponible'])
            break
    else:
        print("ID de libro no encontrado.")
        return

    guardar_datos('libros.json', libros)  # Guardar los datos actualizados de los libros en el archivo JSON
    print("Libro editado con éxito.")

# Función para eliminar un libro por su ID
def eliminar_libro(id_libro):
    libros = cargar_datos('libros.json')  # Cargar los datos de los libros desde un archivo JSON

    # Verificar que el ID del libro sea un número
    if not id_libro.isdigit():
        print("El ID del libro debe ser un número.")
        return

    id_libro = int(id_libro)
    # Crear una nueva lista de libros excluyendo el libro con el ID dado
    libros = [libro for libro in libros if libro['id'] != id_libro]

    guardar_datos('libros.json', libros)  # Guardar los datos actualizados de los libros en el archivo JSON
    print("Libro eliminado con éxito.")

# Función para buscar libros por un término en múltiples campos
def buscar_libro_por_termino(termino):
    libros = cargar_datos('libros.json')  # Cargar los datos de los libros desde un archivo JSON
    # Filtrar libros que contengan el término en el título, autor, editorial, año de publicación o género
    resultado = [libro for libro in libros if
                 termino.lower() in libro['titulo'].lower() or
                 termino.lower() in libro['autor'].lower() or
                 termino.lower() in libro['editorial'].lower() or
                 termino.lower() in str(libro['anio_publicacion']).lower() or
                 termino.lower() in libro['genero'].lower()]
    return resultado

