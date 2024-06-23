from func_aux import cargar_datos, guardar_datos, obtener_nuevo_id

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para registrar un nuevo socio
def registrar_socio(nombre, apellido, dni, telefono, email, direccion, fecha_nacimiento):
    # Cargar los datos de los socios existentes
    socios = cargar_datos('socios.json')

    # Verificar que todos los campos requeridos están llenos
    if not nombre or not apellido or not dni or not telefono or not email or not direccion or not fecha_nacimiento:
        print("Todos los campos son obligatorios.")
        return

    # Crear un nuevo diccionario para el socio
    socio = {
        'id': obtener_nuevo_id(socios),  # Obtener un nuevo ID único
        'nombre': nombre,
        'apellido': apellido,
        'dni': dni,
        'telefono': telefono,
        'email': email,
        'direccion': direccion,
        'fecha_nacimiento': fecha_nacimiento
    }
    # Agregar el nuevo socio a la lista de socios
    socios.append(socio)
    # Guardar los datos actualizados en el archivo JSON
    guardar_datos('socios.json', socios)
    print("Socio registrado con éxito.")

# Función para editar los detalles de un socio existente
def editar_socio(id_socio):
    # Cargar los datos de los socios existentes
    socios = cargar_datos('socios.json')

    # Verificar que el ID del socio es un número
    if not id_socio.isdigit():
        print("El ID del socio debe ser un número.")
        return

    id_socio = int(id_socio)
    # Buscar el socio por su ID
    for socio in socios:
        if socio['id'] == id_socio:
            # Pedir nuevos valores para cada campo, manteniendo el valor existente si no se proporciona uno nuevo
            socio['nombre'] = input(f"Nombre [{socio['nombre']}]: ") or socio['nombre']
            socio['apellido'] = input(f"Apellido [{socio['apellido']}]: ") or socio['apellido']
            socio['dni'] = input(f"DNI [{socio['dni']}]: ") or socio['dni']
            socio['telefono'] = input(f"Teléfono [{socio['telefono']}]: ") or socio['telefono']
            socio['email'] = input(f"Email [{socio['email']}]: ") or socio['email']
            socio['direccion'] = input(f"Dirección [{socio['direccion']}]: ") or socio['direccion']
            socio['fecha_nacimiento'] = input(f"Fecha de Nacimiento [{socio['fecha_nacimiento']}]: ") or socio['fecha_nacimiento']
            break
    else:
        # Mostrar un mensaje si el socio no es encontrado
        print("ID de socio no encontrado.")
        return

    # Guardar los datos actualizados en el archivo JSON
    guardar_datos('socios.json', socios)
    print("Socio editado con éxito.")

# Función para eliminar un socio existente
def eliminar_socio(id_socio):
    # Cargar los datos de los socios existentes
    socios = cargar_datos('socios.json')

    # Verificar que el ID del socio es un número
    if not id_socio.isdigit():
        print("El ID del socio debe ser un número.")
        return

    id_socio = int(id_socio)
    # Crear una nueva lista de socios excluyendo el socio a eliminar
    socios = [socio for socio in socios if socio['id'] != id_socio]

    # Guardar los datos actualizados en el archivo JSON
    guardar_datos('socios.json', socios)
    print("Socio eliminado con éxito.")
