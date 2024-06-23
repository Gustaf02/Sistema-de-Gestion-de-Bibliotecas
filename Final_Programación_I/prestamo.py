from func_aux import cargar_datos, guardar_datos, obtener_nuevo_id
import datetime

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para registrar el préstamo de un libro
def registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo):
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

# Verificar que todos los campos obligatorios estén completos
    if not id_socio or not id_libro or not fecha_prestamo:
        print("Todos los campos son obligatorios.")
        return

    id_libro = int(id_libro)
    # Buscar el libro por ID y verificar disponibilidad
    for libro in libros:
        if libro['id'] == id_libro:
            if libro['cantidad_disponible'] <= 0:
                print("No hay copias disponibles para préstamo.")
                return
            libro['cantidad_disponible'] -= 1
            break
    else:
        print("ID de libro no encontrado.")
        return

    # # Calcular la fecha de devolución prevista (una semana después de la fecha de préstamo)
    fecha_prestamo_dt = datetime.datetime.strptime(fecha_prestamo, '%Y-%m-%d')
    fecha_devolucion_prevista = fecha_prestamo_dt + datetime.timedelta(weeks=1)

    prestamo = {
        'id': obtener_nuevo_id(prestamos), # Obtener un nuevo ID único para el préstamo
        'id_socio': int(id_socio),
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'costo': float(costo) if costo else 0.0, # Convertir costo a float, si se proporciona
        'fecha_devolucion_prevista': fecha_devolucion_prevista.strftime('%Y-%m-%d'),
        'fecha_devolucion': None,
        'estado_prestamo': 'En Curso' # Estado inicial del préstamo
    }
    prestamos.append(prestamo) # Añadir el préstamo a la lista de préstamos
    guardar_datos('prestamos.json', prestamos) # Guardar los datos de préstamos
    guardar_datos('libros.json', libros) # Guardar los datos de libros actualizados
    print("Préstamo registrado con éxito.")

# Función que permite la devolución del préstamo 
def devolver_prestamo(id_prestamo, fecha_devolucion):
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

# Verificar que el ID del préstamo sea un número
    if not id_prestamo.isdigit():
        print("El ID del préstamo debe ser un número.")
        return

    id_prestamo = int(id_prestamo)
# Buscar el préstamo por ID
    for prestamo in prestamos:
        if prestamo['id'] == id_prestamo:
            prestamo['fecha_devolucion'] = fecha_devolucion
            prestamo['estado_prestamo'] = 'Devuelto'
     # Actualizar la cantidad disponible del libro
            for libro in libros:
                if libro['id'] == prestamo['id_libro']:
                    libro['cantidad_disponible'] += 1
                    break
            break
    else:
        print("ID de préstamo no encontrado.")
        return

    guardar_datos('prestamos.json', prestamos) # Guardar los datos de préstamos actualizados
    guardar_datos('libros.json', libros) # Guardar los datos de libros actualizados
    print("Devolución registrada con éxito.")

