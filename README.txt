# Sistema de Gestión de Inventarios en Python

Este proyecto es un sistema simple para crear y gestionar inventarios creado utilizando Python y SQL para la base de datos. Permite realizar operaciones como agregar, mostrar, actualizar, eliminar, buscar productos, y generar reportes de productos con bajo stock a partir de su id. 

## Funcionalidades

- **Agregar Producto:** Permite registrar nuevos productos en el inventario.
- **Mostrar Productos:** Muestra todos los productos registrados, su descripción, categoría, cantidades y precio.
- **Actualizar Producto:** Actualiza la cantidad de un producto existente.
- **Eliminar Producto:** Elimina un producto basado en su ID.
- **Buscar Producto:** Consulta información detallada de un producto por su ID.
- **Reporte Bajo Stock:** Muestra productos cuyo stock está por debajo de un valor mínimo definido.

## Estructura
Se dividió el código en 3 archivos .py y uno .db para mejor organización:
- **main.py** tiene el menú principal para seleccionar las opciones de agregar, mostrar, actualizar, eliminar, buscar y bajo stock de los productos; además de la confirmación antes de realizar algún cambio. 
- **funciones_menu.py** tiene las funcionalidades de cada una de las opciones seleccionadas en el menú. 
- **Inventario.db** es la base de datos donde se almacenará la información básica (id, nombre, descripción, categoría, cantidad y precio).}
- **funciones_database.py** tiene las conexiones con la base de datos.

## Especificaciones
El código fue creado utilizando Python 3.13.1, por lo que se necesitará un editor de código con las extensiones correspondientes. 
Para el manejo de la base de datos fue utilizado SQLite.

## Para utilizar y/o contribuir con este código

Realiza un *fork* del mismo. 

