from funciones_database import *

# ******************************************************************
# DECLARACION DE FUNCIONES
# ******************************************************************

# Funcion que muestra el menú
def menu_mostrar_opciones():
    print("-" * 30)
    print(" Menú principal")
    print("-" * 30)
    print("1. Agregar producto\n2. Mostrar producto\n3. Actualizar\n4. Eliminar\n5. Buscar producto\n6. Reporte bajo Stock\n7. Salir")
    opcion = input("Ingrese la opción deseada: ")
    return opcion


# Agregar producto
def menu_registrar_producto():
    print("--AGREGAR PRODUCTO--")
    nombre = input("Ingresá el nombre del producto: ")
    descripcion = input("Ingresá su descripción: ")
    categoria = input("Ingresá su categoría: ")

    # Validación de cantidad en números enteros
    while True:
        try:
            cantidad = int(input("Ingresá cantidad del producto: "))
            break
        except Exception as error:
            print("Error: debe ingresar un número entero")

    # Validación de precio en números enteros
    while True:
        try:
            precio = int(input("Ingresá el precio del producto: "))
            break
        except Exception as error:
            print("Error: debe ingresar un número entero")

    # Creación de un diccionario temporal
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_insertar_producto(producto)
    print(f"\nProducto insertado exitosamente: \n{producto}")
    print("¿Desea agregar otro producto?")
    masproductos = input(
            "Ingrese 's' para agregar otro o cualquier tecla para volver al menú principal: "
        )
    if masproductos == "s":
            return menu_registrar_producto()
# Mostrar producto
def menu_mostrar_productos():
    lista_productos = db_get_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos que mostrar")


# Actualizar producto
def menu_actualizar_producto():
    id = int(input("\nIngrese el id del producto a actualizar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print(f"ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)
        nueva_cantidad = int(input(f"Cantidad actual {get_producto[4]} - Nueva cantidad: "))
        db_actualizar_producto(id, nueva_cantidad)
        print("Registro actualizado exitosamente!")


# Eliminar producto
def menu_eliminar_producto():
    id = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print(f"No se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)


# Buscar producto
def menu_buscar_producto():
    id = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_producto_by_id(id)
    if not get_producto:
        print(f"ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)


# Reporte bajo stock
def menu_reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el stock mínimo:"))
    lista_productos = db_get_productos_by_condicion(minimo_stock)
    if not lista_productos:
        print(f"No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)