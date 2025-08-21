from fastapi import APIRouter
from app.services import postgresql

router = APIRouter(
    prefix="/PostgreSQL",
    tags=["CRUD PostgreSQL"]
)

# Verificar conexión
@router.get("/check-db")
def check_db():
    return postgresql.check_connection()

# Crear / eliminar DB
@router.post("/create-db/{db_name}")
def create_db(db_name: str):
    return postgresql.create_database(db_name)

@router.delete("/drop-db/{db_name}")
def drop_db(db_name: str):
    return postgresql.drop_database(db_name)

# Crear / eliminar tabla
@router.post("/create-table/{db_name}/{table_name}")
def create_table(db_name: str, table_name: str):
    return postgresql.create_table(db_name, table_name)

@router.delete("/drop-table/{db_name}/{table_name}")
def drop_table(db_name: str, table_name: str):
    return postgresql.drop_table(db_name, table_name)

# CRUD usuarios
@router.post("/insert/{db_name}/{table_name}")
def insert_user(db_name: str, table_name: str, nombre: str, edad: int):
    return postgresql.insert_user(db_name, table_name, nombre, edad)

@router.get("/users/{db_name}/{table_name}")
def get_users(db_name: str, table_name: str):
    return postgresql.get_users(db_name, table_name)

@router.put("/update/{db_name}/{table_name}/{user_id}")
def update_user(db_name: str, table_name: str, user_id: int, nombre: str, edad: int):
    return postgresql.update_user(db_name, table_name, user_id, nombre, edad)

@router.delete("/delete/{db_name}/{table_name}/{user_id}")
def delete_user(db_name: str, table_name: str, user_id: int):
    return postgresql.delete_user(db_name, table_name, user_id)
