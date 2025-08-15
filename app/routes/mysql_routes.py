from fastapi import APIRouter, HTTPException
from app.services import mysql

router = APIRouter(
    prefix="/MySQL",
    tags=["CRUD MySQL"]
)

# Verificar conexión
@router.get("/check-db")
def check_mysql_db():
    try:
        mysql.conectar()
        return {"status": "success", "message": "Conectado a MySQL"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear DB
@router.post("/create-db/{nombre_db}")
def create_db(nombre_db: str):
    try:
        return {"message": mysql.crear_db(nombre_db)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Borrar DB
@router.delete("/delete-db/{nombre_db}")
def delete_db(nombre_db: str):
    try:
        return {"message": mysql.borrar_db(nombre_db)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Crear tabla
@router.post("/create-table/{nombre_db}/{nombre_tabla}")
def create_table(nombre_db: str, nombre_tabla: str):
    try:
        return {"message": mysql.crear_tabla(nombre_db, nombre_tabla)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Borrar tabla
@router.delete("/delete-table/{nombre_db}/{nombre_tabla}")
def delete_table(nombre_db: str, nombre_tabla: str):
    try:
        return {"message": mysql.borrar_tabla(nombre_db, nombre_tabla)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# CRUD
@router.post("/insert/{nombre_db}/{nombre_tabla}")
def insert_data(nombre_db: str, nombre_tabla: str, nombre: str, edad: int):
    try:
        return {"message": mysql.insertar_dato(nombre_db, nombre_tabla, nombre, edad)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get/{nombre_db}/{nombre_tabla}")
def get_data(nombre_db: str, nombre_tabla: str):
    try:
        return mysql.obtener_datos(nombre_db, nombre_tabla)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update/{nombre_db}/{nombre_tabla}/{id}")
def update_data(nombre_db: str, nombre_tabla: str, id: int, nombre: str, edad: int):
    try:
        return {"message": mysql.actualizar_dato(nombre_db, nombre_tabla, id, nombre, edad)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete/{nombre_db}/{nombre_tabla}/{id}")
def delete_data(nombre_db: str, nombre_tabla: str, id: int):
    try:
        return {"message": mysql.eliminar_dato(nombre_db, nombre_tabla, id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
