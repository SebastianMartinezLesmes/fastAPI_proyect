from fastapi import APIRouter, HTTPException
from app.services import oracle

router = APIRouter(
    prefix="/Oracle",
    tags=["CRUD Oracle"]
)

# 1. Verificación
@router.get("/check-db")
def check_db():
    try:
        oracle.check_connection()
        return {"status": "success", "message": "Conectado a Oracle"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 2. Crear/Eliminar Usuario (equivalente a "base de datos")
@router.post("/create-user/{username}/{password}")
def create_user(username: str, password: str):
    try:
        oracle.create_user(username, password)
        return {"status": "success", "message": f"Usuario {username} creado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/drop-user/{username}")
def drop_user(username: str):
    try:
        oracle.drop_user(username)
        return {"status": "success", "message": f"Usuario {username} eliminado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 3. Crear/Eliminar Tabla
@router.post("/create-table")
def create_table():
    try:
        oracle.create_table()
        return {"status": "success", "message": "Tabla creada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/drop-table")
def drop_table():
    try:
        oracle.drop_table()
        return {"status": "success", "message": "Tabla eliminada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 4. CRUD
@router.post("/usuarios")
def create_usuario(nombre: str, email: str):
    try:
        oracle.insert_usuario(nombre, email)
        return {"status": "success", "message": "Usuario creado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/usuarios")
def list_usuarios():
    try:
        return oracle.get_usuarios()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/usuarios/{user_id}")
def update_usuario(user_id: int, nombre: str, email: str):
    try:
        oracle.update_usuario(user_id, nombre, email)
        return {"status": "success", "message": "Usuario actualizado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/usuarios/{user_id}")
def delete_usuario(user_id: int):
    try:
        oracle.delete_usuario(user_id)
        return {"status": "success", "message": "Usuario eliminado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
