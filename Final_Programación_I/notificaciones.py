import datetime  # Importar el módulo datetime para trabajar con fechas
from func_aux import cargar_datos # Importar la función cargar_datos para manejar archivos JSON

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para notificar sobre préstamos vencidos
def notificar_vencimiento():
  # Cargar datos de préstamos y socios desde archivos JSON
    prestamos = cargar_datos('prestamos.json')
    socios = cargar_datos('socios.json')

    hoy = datetime.date.today().isoformat()  # Obtener la fecha actual en formato ISO (YYYY-MM-DD)

    # Recorrer la lista de préstamos
    for prestamo in prestamos:
        # Verificar si el préstamo no ha sido devuelto y la fecha de préstamo es anterior a la fecha actual
        if not prestamo['fecha_devolucion'] and prestamo['fecha_prestamo'] < hoy:
            # Buscar el socio correspondiente al ID del préstamo
            socio = next((s for s in socios if s['id'] == prestamo['id_socio']), None)
            if socio:
                # Imprimir una notificación sobre el préstamo vencido
                print(f"Notificación: El socio {socio['nombre']} {socio['apellido']} con DNI {socio['dni']} tiene un préstamo vencido para el libro con ID {prestamo['id_libro']} desde el {prestamo['fecha_prestamo']}.")

# Se llama a la función (se elimina al usar la función desde otro archivo)
# notificar_vencimiento()