import sqlite3

# DECLARACION DE CONSTANTES
ruta_db = r"C:\Users\Usuario\Downloads\Curso python\proyecto final\inventario.db"


# DECLARACION DE FUNCIONES


##Crea la tabla##
def db_crear_tabla_productos():
    try:  #evita error
        conexion = sqlite3.connect(ruta_db)
        cursor = conexion.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )"""
        )
        conexion.commit()
    except sqlite3.Error as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        conexion.close()


##genera productos##
def db_insertar_producto(producto):
    try:
        with sqlite3.connect(ruta_db) as conexion:
            cursor = conexion.cursor()  
            query = "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)"
            placeholder = (producto["nombre"], producto["descripcion"], producto["categoria"], producto["cantidad"], producto["precio"])
            cursor.execute(query, placeholder)
            conexion.commit()
            return True
    except sqlite3.Error as e:
        print(f"Error al insertar producto: {e}")
        return False


##Devuelve los datos en forma de tupla##
def db_get_productos():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    lista_productos = cursor.fetchall() #retorno de tupla
    conexion.close()
    return lista_productos


##Busca por ID##
def db_get_producto_by_id(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    producto = cursor.fetchone() #retorno de tupla
    conexion.close()
    return producto


##Actualiza cantidad por id##
def db_actualizar_producto(id, nueva_cantidad):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    placeholders = (nueva_cantidad, id)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


##Elimina producto por id##
def db_eliminar_producto(id):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    placeholders = (id,)
    cursor.execute(query, placeholders)
    conexion.commit()
    conexion.close()


##Retorna productos con poco stock##
def db_get_productos_by_condicion(minimo_stock):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = (minimo_stock,)
    cursor.execute(query, placeholders)
    lista_productos = cursor.fetchall() #retorno de tupla
    conexion.close()
    return lista_productos
