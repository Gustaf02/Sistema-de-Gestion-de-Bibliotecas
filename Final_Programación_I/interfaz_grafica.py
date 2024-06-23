import tkinter as tk
from tkinter import messagebox
from libro import registrar_libro, buscar_libro_por_termino

"""PROGRAMADORES: ISRAEL LEONARDO MONTIEL-  CARLOS GUSTAVO ORTIZ"""

# Función para manejar el registro de un nuevo libro desde la interfaz gráfica
def registrar():
    # Obtener los valores de los campos de entrada
    titulo = entry_titulo_reg.get()
    autor = entry_autor_reg.get()
    editorial = entry_editorial_reg.get()
    anio_publicacion = entry_anio_reg.get()
    genero = entry_genero_reg.get()
    cantidad_disponible = entry_cantidad_reg.get()

    # Llamar a la función de registrar libro
    registrar_libro(titulo, autor, editorial, anio_publicacion, genero, cantidad_disponible)
    # Mostrar un mensaje de éxito
    messagebox.showinfo("Registro", "Libro registrado con éxito.")

# Función para manejar la búsqueda de libros desde la interfaz gráfica
def buscar():
    # Obtener el término de búsqueda del campo de entrada
    termino = entry_termino_bus.get()

    # Llamar a la función de buscar libro por término
    resultados = buscar_libro_por_termino(termino)

    # Mostrar los resultados en un mensaje
    if resultados:
        resultados_text = "\n".join([f"{libro['titulo']} por {libro['autor']}" for libro in resultados])
        messagebox.showinfo("Resultados de la búsqueda", resultados_text)
    else:
        messagebox.showinfo("Resultados de la búsqueda", "No se encontraron libros que coincidan con el término.")

# Crear la ventana principal de la interfaz gráfica
root = tk.Tk()
root.title("Sistema de Gestión de Biblioteca")

# Sección de registro de libros
tk.Label(root, text="Registrar Libro").grid(row=0, column=0, columnspan=2)
tk.Label(root, text="Título").grid(row=1, column=0)
tk.Label(root, text="Autor").grid(row=2, column=0)
tk.Label(root, text="Editorial").grid(row=3, column=0)
tk.Label(root, text="Año de Publicación").grid(row=4, column=0)
tk.Label(root, text="Género").grid(row=5, column=0)
tk.Label(root, text="Cantidad Disponible").grid(row=6, column=0)

# Campos de entrada para el registro de libros
entry_titulo_reg = tk.Entry(root)
entry_autor_reg = tk.Entry(root)
entry_editorial_reg = tk.Entry(root)
entry_anio_reg = tk.Entry(root)
entry_genero_reg = tk.Entry(root)
entry_cantidad_reg = tk.Entry(root)

entry_titulo_reg.grid(row=1, column=1)
entry_autor_reg.grid(row=2, column=1)
entry_editorial_reg.grid(row=3, column=1)
entry_anio_reg.grid(row=4, column=1)
entry_genero_reg.grid(row=5, column=1)
entry_cantidad_reg.grid(row=6, column=1)

# Botón para registrar el libro
tk.Button(root, text='Registrar', command=registrar).grid(row=7, column=1, pady=4)

# Sección de búsqueda de libros
tk.Label(root, text="Buscar Libro").grid(row=0, column=2, columnspan=2)
tk.Label(root, text="Término de Búsqueda").grid(row=1, column=2)

# Campo de entrada para el término de búsqueda
entry_termino_bus = tk.Entry(root)
entry_termino_bus.grid(row=1, column=3)

# Botón para buscar el libro
tk.Button(root, text='Buscar', command=buscar).grid(row=2, column=3, pady=4)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()

