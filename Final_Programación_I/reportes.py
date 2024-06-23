from func_aux import cargar_datos

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Generar un reporte de préstamos por socio
def reporte_prestamos_por_socio(id_socio):
    # Cargar los datos de préstamos y socios
    prestamos = cargar_datos('prestamos.json')
    socios = cargar_datos('socios.json')

    # Buscar el socio por su ID
    socio = next((s for s in socios if s['id'] == int(id_socio)), None)
    if not socio:
        # Mostrar un mensaje si el socio no es encontrado
        print("ID de socio no encontrado.")
        return

    # Filtrar los préstamos realizados por el socio especificado
    resultado = [prestamo for prestamo in prestamos if prestamo['id_socio'] == int(id_socio)]
    return resultado

# Generar un reporte de préstamos por libro
def reporte_prestamos_por_libro(id_libro):
    # Cargar los datos de préstamos y libros
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

    # Buscar el libro por su ID
    libro = next((l for l in libros if l['id'] == int(id_libro)), None)
    if not libro:
        # Mostrar un mensaje si el libro no es encontrado
        print("ID de libro no encontrado.")
        return

    # Filtrar los préstamos realizados para el libro especificado
    resultado = [prestamo for prestamo in prestamos if prestamo['id_libro'] == int(id_libro)]
    return resultado

# Generar un reporte de préstamos por un rango de fechas
def reporte_prestamos_por_fecha(fecha_inicio, fecha_fin):
    # Cargar los datos de préstamos
    prestamos = cargar_datos('prestamos.json')

    # Filtrar los préstamos realizados dentro del rango de fechas especificado
    resultado = [prestamo for prestamo in prestamos if fecha_inicio <= prestamo['fecha_prestamo'] <= fecha_fin]
    return resultado
