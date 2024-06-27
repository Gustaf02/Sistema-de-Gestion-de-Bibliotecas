from func_aux import cargar_datos
from datetime import datetime, timedelta

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL- CARLOS GUSTAVO ORTIZ"""

def determinar_estado_prestamo(prestamo):
    fecha_vencimiento_prevista = prestamo.get('fecha_devolucion_prevista')
    fecha_devolucion = prestamo.get('fecha_devolucion')

    if fecha_vencimiento_prevista:
        fecha_vencimiento_prevista = datetime.strptime(fecha_vencimiento_prevista, '%Y-%m-%d')
        hoy = datetime.now()

        # Calculamos la fecha límite, 7 días después de la fecha de vencimiento prevista
        fecha_limite = fecha_vencimiento_prevista + timedelta(days=7)

        if fecha_devolucion is None and hoy > fecha_limite:
            print("El libro no se ha devuelto, por ende el socio se encuentra en mora")
            return 'moroso'
        else:
            return 'en curso'
    else:
        return 'fecha de vencimiento no disponible'

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
        return []

    # Filtrar los préstamos realizados por el socio especificado
    resultado = []
    for prestamo in prestamos:
        if prestamo['id_socio'] == int(id_socio):
            prestamo['estado'] = determinar_estado_prestamo(prestamo)
            resultado.append(prestamo)

    return resultado

# Generar un reporte de préstamos por libro
def reporte_prestamos_por_libro(id_libro):
    print("Ejecutando reporte de préstamos por libro...")  # Depuración
    # Cargar los datos de préstamos y libros
    prestamos = cargar_datos('prestamos.json')
    libros = cargar_datos('libros.json')

    # Buscar el libro por su ID
    libro = next((l for l in libros if l['id'] == int(id_libro)), None)
    if not libro:
        # Mostrar un mensaje si el libro no es encontrado
        print("ID de libro no encontrado.")
        return []

    # Filtrar los préstamos realizados para el libro especificado
    resultado = []
    for prestamo in prestamos:
        if prestamo['id_libro'] == int(id_libro):
            prestamo['estado'] = determinar_estado_prestamo(prestamo)
            resultado.append(prestamo)

    return resultado

# Generar un reporte de préstamos por un rango de fechas
def reporte_prestamos_por_fecha(fecha_inicio, fecha_fin):
    # Cargar los datos de préstamos
    prestamos = cargar_datos('prestamos.json')

    # Convertir fechas de inicio y fin a objetos datetime
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

    # Filtrar los préstamos realizados dentro del rango de fechas especificado
    resultado = []
    for prestamo in prestamos:
        fecha_prestamo = datetime.strptime(prestamo['fecha_prestamo'], '%Y-%m-%d')
        if fecha_inicio <= fecha_prestamo <= fecha_fin:
            prestamo['estado'] = determinar_estado_prestamo(prestamo)
            resultado.append(prestamo)

    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    print("Seleccione una opción para generar el reporte:")
    print("1. Reporte de préstamos por socio")
    print("2. Reporte de préstamos por libro")
    print("3. Reporte de préstamos por rango de fechas")
    opcion = input("Ingrese el número de opción: ")

    print(f"Ha seleccionado la opción {opcion}.")  # Depuración

    if opcion == "1":
        id_socio = input("Ingrese el ID del socio para generar el reporte: ")
        prestamos_socio = reporte_prestamos_por_socio(id_socio)
        for prestamo in prestamos_socio:
            print(f"ID del Socio: {prestamo['id_socio']}")
            print(f"Libro ID: {prestamo['id_libro']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de vencimiento: {prestamo.get('fecha_devolucion_prevista', 'No disponible')}, Estado: {prestamo['estado']}, Estado del préstamo: {prestamo['estado_prestamo']}, Costo: {prestamo['costo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No disponible')}")
            if prestamo['estado'] == 'moroso':
                print("El libro no se ha devuelto (aunque el préstamo figure en curso), por ende el socio se encuentra en mora")

    elif opcion == "2":
        id_libro = input("Ingrese el ID del libro para generar el reporte: ")
        prestamos_libro = reporte_prestamos_por_libro(id_libro)
        for prestamo in prestamos_libro:
            print(f"Libro ID: {prestamo['id_libro']}, ID del Socio: {prestamo['id_socio']}, Fecha de préstamo: {prestamo['fecha_prestamo']}, Fecha de vencimiento: {prestamo.get('fecha_devolucion_prevista', 'No disponible')}, Estado: {prestamo['estado']}, Estado del préstamo: {prestamo['estado_prestamo']}, Costo: {prestamo['costo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No disponible')}")
            if prestamo['estado'] == 'moroso':
                print("El libro no se ha devuelto (aunque el préstamo figure en curso), por ende el socio se encuentra en mora")

    elif opcion == "3":
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        prestamos_fecha = reporte_prestamos_por_fecha(fecha_inicio, fecha_fin)
        for prestamo in prestamos_fecha:
            print(f"Fecha de préstamo: {prestamo['fecha_prestamo']}, Libro ID: {prestamo['id_libro']}, ID del Socio: {prestamo['id_socio']}, Fecha de vencimiento: {prestamo.get('fecha_devolucion_prevista', 'No disponible')}, Estado: {prestamo['estado']}, Estado del préstamo: {prestamo['estado_prestamo']}, Costo: {prestamo['costo']}, Fecha de devolución: {prestamo.get('fecha_devolucion', 'No disponible')}")
            if prestamo['estado'] == 'moroso':
                print("El libro no se ha devuelto (aunque el préstamo figure en curso), por ende, el socio se encuentra en mora")

    else:
        print("Opción no válida.")
