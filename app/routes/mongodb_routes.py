from fastapi import APIRouter, HTTPException
from app.models.usuario_model import Usuario
from app.services import mongoDB

router = APIRouter(
    prefix="/MongoDB",
    tags=["CRUD MongoDB"]
)

@router.get("/check-db")
def check_db():
    return mongoDB.check_database_connection()

@router.post("/post_users")
def crear_usuario(usuario: Usuario):
    usuario_id = mongoDB.crear_usuario(usuario.dict())
    return {"id": usuario_id}

@router.get("/get_users")
def listar_usuarios():
    return mongoDB.obtener_usuarios()

@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: str):
    usuario = mongoDB.obtener_usuario_por_id(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: str, usuario: Usuario):
    if not mongoDB.actualizar_usuario(usuario_id, usuario.dict()):
        raise HTTPException(status_code=404, detail="Usuario no encontrado o sin cambios")
    return {"mensaje": "Usuario actualizado"}

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    if not mongoDB.eliminar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}

@router.delete("/eliminar_db")
def eliminar_base_datos():
    try:
        mongoDB.client.drop_database("FastAPI")
        return {"mensaje": "Base de datos 'FastAPI' eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
