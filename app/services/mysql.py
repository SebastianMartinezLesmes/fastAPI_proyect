import mysql.connector
from mysql.connector import Error

# Datos de conexión (puedes ponerlos en variables de entorno)
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "1234"

def conectar():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD
        )
        if conn.is_connected():
            return conn
    except Error as e:
        raise Exception(f"Error al conectar a MySQL: {e}")

# 1. Crear base de datos
def crear_db(nombre_db: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {nombre_db}")
    conn.close()
    return f"Base de datos '{nombre_db}' creada con éxito"

# 2. Borrar base de datos
def borrar_db(nombre_db: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE IF EXISTS {nombre_db}")
    conn.close()
    return f"Base de datos '{nombre_db}' eliminada con éxito"

# 3. Crear tabla
def crear_tabla(nombre_db: str, nombre_tabla: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"""
        CREATE TABLE {nombre_tabla} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            edad INT
        )
    """)
    conn.close()
    return f"Tabla '{nombre_tabla}' creada en DB '{nombre_db}'"

# 4. Borrar tabla
def borrar_tabla(nombre_db: str, nombre_tabla: str):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"DROP TABLE IF EXISTS {nombre_tabla}")
    conn.close()
    return f"Tabla '{nombre_tabla}' eliminada de DB '{nombre_db}'"

# 5. CRUD
def insertar_dato(nombre_db: str, nombre_tabla: str, nombre: str, edad: int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"INSERT INTO {nombre_tabla} (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conn.commit()
    conn.close()
    return "Dato insertado correctamente"

def obtener_datos(nombre_db: str, nombre_tabla: str):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"SELECT * FROM {nombre_tabla}")
    datos = cursor.fetchall()
    conn.close()
    return datos

def actualizar_dato(nombre_db: str, nombre_tabla: str, id: int, nombre: str, edad: int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"UPDATE {nombre_tabla} SET nombre=%s, edad=%s WHERE id=%s", (nombre, edad, id))
    conn.commit()
    conn.close()
    return "Dato actualizado correctamente"

def eliminar_dato(nombre_db: str, nombre_tabla: str, id: int):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"USE {nombre_db}")
    cursor.execute(f"DELETE FROM {nombre_tabla} WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return "Dato eliminado correctamente"
