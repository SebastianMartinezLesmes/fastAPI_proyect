import psycopg2
from psycopg2 import sql
from fastapi import HTTPException

# Datos de conexión (ajusta según tu entorno)
DB_HOST = "localhost"
DB_PORT = "5432"
DB_USER = "postgres"
DB_PASSWORD = "1234"

def get_connection(dbname="postgres"):
    """
    Crear conexión a la base de datos.
    Por defecto conecta al esquema 'postgres'.
    """
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión: {e}")


def check_connection():
    """Verificar conexión con la base de datos."""
    conn = get_connection()
    conn.close()
    return {"status": "success", "message": "Conexión a PostgreSQL exitosa"}


def create_database(db_name: str):
    """Crear una nueva base de datos."""
    conn = get_connection()
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        return {"status": "success", "message": f"Base de datos '{db_name}' creada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear DB: {e}")
    finally:
        cursor.close()
        conn.close()


def drop_database(db_name: str):
    """Eliminar base de datos."""
    conn = get_connection()
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(db_name)))
        return {"status": "success", "message": f"Base de datos '{db_name}' eliminada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar DB: {e}")
    finally:
        cursor.close()
        conn.close()


def create_table(db_name: str, table_name: str):
    """Crear una tabla simple en una DB existente."""
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(sql.SQL(
            """
            CREATE TABLE IF NOT EXISTS {} (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                edad INT
            )
            """
        ).format(sql.Identifier(table_name)))
        conn.commit()
        return {"status": "success", "message": f"Tabla '{table_name}' creada en DB '{db_name}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear tabla: {e}")
    finally:
        cursor.close()
        conn.close()


def drop_table(db_name: str, table_name: str):
    """Eliminar tabla en una DB existente."""
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name)))
        conn.commit()
        return {"status": "success", "message": f"Tabla '{table_name}' eliminada en DB '{db_name}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar tabla: {e}")
    finally:
        cursor.close()
        conn.close()


# CRUD básico
def insert_user(db_name: str, table_name: str, nombre: str, edad: int):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("INSERT INTO {} (nombre, edad) VALUES (%s, %s) RETURNING id")
            .format(sql.Identifier(table_name)),
            (nombre, edad)
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        return {"status": "success", "message": "Usuario insertado", "id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al insertar usuario: {e}")
    finally:
        cursor.close()
        conn.close()


def get_users(db_name: str, table_name: str):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(sql.SQL("SELECT id, nombre, edad FROM {}").format(sql.Identifier(table_name)))
        rows = cursor.fetchall()
        return [{"id": r[0], "nombre": r[1], "edad": r[2]} for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener usuarios: {e}")
    finally:
        cursor.close()
        conn.close()


def update_user(db_name: str, table_name: str, user_id: int, nombre: str, edad: int):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("UPDATE {} SET nombre=%s, edad=%s WHERE id=%s")
            .format(sql.Identifier(table_name)),
            (nombre, edad, user_id)
        )
        conn.commit()
        return {"status": "success", "message": f"Usuario {user_id} actualizado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar usuario: {e}")
    finally:
        cursor.close()
        conn.close()


def delete_user(db_name: str, table_name: str, user_id: int):
    conn = get_connection(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute(
            sql.SQL("DELETE FROM {} WHERE id=%s").format(sql.Identifier(table_name)),
            (user_id,)
        )
        conn.commit()
        return {"status": "success", "message": f"Usuario {user_id} eliminado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario: {e}")
    finally:
        cursor.close()
        conn.close()
