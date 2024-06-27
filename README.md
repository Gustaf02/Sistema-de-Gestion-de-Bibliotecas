# Sistema-de-Gestión-de-Bibliotecas

## 1. Descripción General del Proyecto
El proyecto de gestión de bibliotecas es una aplicación diseñada para manejar el registro, búsqueda, préstamo y devolución de libros en una biblioteca. Además, permite la gestión de socios, la generación de reportes y la notificación de vencimientos de préstamos. Este sistema facilita la administración de una biblioteca, permitiendo a los usuarios mantener un control eficiente de los recursos y actividades de la misma.

## 2. Estructura del Proyecto
El proyecto está organizado en varios módulos, cada uno de los cuales se encarga de una funcionalidad específica del sistema. Los principales archivos y sus propósitos son:

* biblioteca.py: Contiene la función principal que ofrece un menú interactivo para las diferentes operaciones de la biblioteca.
* libro.py: Maneja las operaciones relacionadas con los libros, como registrar, editar, eliminar y buscar libros.
* socio.py: Gestiona las operaciones relacionadas con los socios de la biblioteca, como registrar, editar y eliminar socios.
* prestamo.py: Controla las operaciones de préstamos y devoluciones de libros.
* busqueda.py: Proporciona funcionalidades de búsqueda de libros basadas en varios criterios.
* reportes.py: Genera reportes de préstamos por socio, libro o fecha.
* notificaciones.py: Envía notificaciones sobre préstamos vencidos.
* func_aux.py: Incluye funciones auxiliares para cargar, guardar y manejar datos en archivos JSON.
* inicializacion_json.py: Inicializa los archivos JSON necesarios para el funcionamiento del sistema.
* interfaz_grafica.py: Proporciona una interfaz gráfica para interactuar con el sistema.

## 3. Funcionalidades del Proyecto
### 3.1 Gestión de Libros
* Registrar Libro: Permite registrar un nuevo libro en el sistema ingresando detalles como título, autor, editorial, año de publicación, género y cantidad disponible.
* Editar Libro: Permite editar la información de un libro existente en el sistema.
* Eliminar Libro: Permite eliminar un libro del sistema.
* Buscar Libro: Permite buscar libros en el sistema utilizando varios criterios como título, género, autor y editorial.
### 3.2 Gestión de Socios
* Registrar Socio: Permite registrar un nuevo socio en la biblioteca ingresando detalles como nombre, apellido, DNI, teléfono, email, dirección y fecha de nacimiento.
* Editar Socio: Permite editar la información de un socio existente.
* Eliminar Socio: Permite eliminar un socio del sistema.
### 3.3 Gestión de Préstamos
* Registrar Préstamo: Permite registrar un nuevo préstamo de un libro a un socio, especificando la fecha de préstamo y el costo.
* Registrar Devolución: Permite registrar la devolución de un libro prestado, actualizando la cantidad disponible del libro y el estado del préstamo.
### 3.4 Reportes y Notificaciones
* Generar Reporte: Permite generar reportes de préstamos por socio, libro o fecha.
* Notificar Vencimientos: Envía notificaciones sobre préstamos vencidos a los socios correspondientes.
### 3.5 Inicialización de Datos
* Inicialización de Archivos JSON: El archivo inicializacion_json.py se encarga de crear y estructurar los archivos JSON necesarios para el funcionamiento del sistema, garantizando que se disponga de una base de datos inicial limpia.
### 3.6 Interfaz Gráfica
* Interfaz Gráfica del Usuario (GUI): Proporcionada por interfaz_grafica.py, esta interfaz permite a los usuarios interactuar con el sistema de manera más intuitiva, facilitando la realización de las operaciones disponibles en el sistema.
  
## 4. Descripción Técnica del Proyecto
El proyecto está desarrollado en Python y utiliza archivos JSON para almacenar los datos de libros, socios y préstamos. Las principales operaciones de lectura y escritura en archivos JSON están encapsuladas en funciones auxiliares en el archivo func_aux.py. Esto asegura una gestión eficiente y segura de los datos, facilitando su manipulación y manteniendo la integridad de la información.

Ejemplo, de función auxiliar:

![image](https://github.com/Gustaf02/Sistema-de-Gestion-de-Bibliotecas/assets/92409193/dba8ad21-070b-4324-b2bd-5fe262e55af5)

Estas funciones permiten cargar y guardar datos de manera eficiente y segura, asegurando que los archivos se manejen correctamente.

## 5. Video

https://vimeo.com/970127143?share=copy

## 6. Conclusión
El proyecto de gestión de bibliotecas es una herramienta integral para la administración de bibliotecas, proporcionando funcionalidades esenciales para la gestión de libros, socios y préstamos. Su estructura modular facilita la expansión y el mantenimiento, mientras que el uso de archivos JSON asegura una gestión eficiente de los datos.

## Integrantes 
       
       ┃━ ━📂 \Israel Leonardo Montiel 

       ┃━ ━📂 \Carlos Gustavo Ortiz





