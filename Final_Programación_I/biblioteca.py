from libro import registrar_libro, editar_libro, eliminar_libro
from socio import registrar_socio, editar_socio, eliminar_socio
from prestamo import registrar_prestamo, devolver_prestamo
from busqueda import buscar_libro_por_titulo, buscar_libro_por_genero, buscar_libro_por_autor, buscar_libro_por_editorial
from reportes import reporte_prestamos_por_socio, reporte_prestamos_por_libro, reporte_prestamos_por_fecha
from notificaciones import notificar_vencimiento

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función principal de la biblioteca que ofrece un menú para las diferentes operaciones
def main():
    while True:
        # Mostrar el menú de opciones
        print("\nSistema de Gestión de Bibliotecas")
        print("1. Registrar Libro")
        print("2. Editar Libro")
        print("3. Eliminar Libro")
        print("4. Registrar Socio")
        print("5. Editar Socio")
        print("6. Eliminar Socio")
        print("7. Registrar Préstamo")
        print("8. Registrar Devolución")
        print("9. Buscar Libro")
        print("10. Generar Reporte")
        print("11. Notificar Vencimientos")
        print("0. Salir")

        # Solicitar al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")

        # Procesar la opción seleccionada
        if opcion == '1':
            # Registrar un nuevo libro
            titulo = input("Título: ")
            autor = input("Autor: ")
            editorial = input("Editorial: ")
            anio_publicacion = input("Año de Publicación: ")
            genero = input("Género: ")
            cantidad_disponible = input("Cantidad Disponible: ")
            registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
        elif opcion == '2':
            # Editar un libro existente
            id_libro = input("ID del Libro a editar: ")
            editar_libro(id_libro)
        elif opcion == '3':
            # Eliminar un libro existente
            id_libro = input("ID del Libro a eliminar: ")
            eliminar_libro(id_libro)
        elif opcion == '4':
            # Registrar un nuevo socio
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            direccion = input("Dirección: ")
            fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
            registrar_socio(nombre, apellido, dni, telefono, email, direccion, fecha_nacimiento)
        elif opcion == '5':
            # Editar un socio existente
            id_socio = input("ID del Socio a editar: ")
            editar_socio(id_socio)
        elif opcion == '6':
            # Eliminar un socio existente
            id_socio = input("ID del Socio a eliminar: ")
            eliminar_socio(id_socio)
        elif opcion == '7':
            # Registrar un nuevo préstamo
            id_socio = input("ID del Socio: ")
            id_libro = input("ID del Libro: ")
            fecha_prestamo = input("Fecha de Préstamo (YYYY-MM-DD): ")
            costo = input("Costo: ")
            registrar_prestamo(id_socio, id_libro, fecha_prestamo, costo)
        elif opcion == '8':
            # Registrar la devolución de un préstamo
            id_prestamo = input("ID del Préstamo: ")
            fecha_devolucion = input("Fecha de Devolución (YYYY-MM-DD): ")
            devolver_prestamo(id_prestamo, fecha_devolucion)
        elif opcion == '9':
            # Buscar un libro
            criterio = input("Buscar por (1) Título, (2) Género, (3) Autor, (4) Editorial: ")
            if criterio == '1':
                # Buscar libro por título
                titulo = input("Título: ")
                resultados = buscar_libro_por_titulo(titulo)
            elif criterio == '2':
                # Buscar libro por género
                genero = input("Género: ")
                resultados = buscar_libro_por_genero(genero)
            elif criterio == '3':
                # Buscar libro por autor
                autor = input("Autor: ")
                resultados = buscar_libro_por_autor(autor)
            elif criterio == '4':
                # Buscar libro por editorial
                editorial = input("Editorial: ")
                resultados = buscar_libro_por_editorial(editorial)
            else:
                print("Opción no válida.")
                continue
            
            # Mostrar los resultados de la búsqueda
            for resultado in resultados:
                print(resultado)
        elif opcion == '10':
            # Generar un reporte
            tipo_reporte = input("Generar reporte por (1) Socio, (2) Libro, (3) Fecha: ")
            if tipo_reporte == '1':
                # Reporte de préstamos por socio
                id_socio = input("ID del Socio: ")
                resultados = reporte_prestamos_por_socio(id_socio)
            elif tipo_reporte == '2':
                # Reporte de préstamos por libro
                id_libro = input("ID del Libro: ")
                resultados = reporte_prestamos_por_libro(id_libro)
            elif tipo_reporte == '3':
                # Reporte de préstamos por fecha
                fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
                resultados = reporte_prestamos_por_fecha(fecha_inicio, fecha_fin)
            else:
                print("Opción no válida.")
                continue

            # Mostrar los resultados del reporte
            for resultado in resultados:
                print(resultado)
        elif opcion == '11':
            # Notificar vencimientos de préstamos
            notificar_vencimiento()
        elif opcion == '0':
            # Salir del programa
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la función principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main()
