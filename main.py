from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.south_park import personajes_servicios
from app.services import mongoDB

app = FastAPI()

# Modelo de Usuario
class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int

@app.get("/", tags=["Inicio"])
def index():
    return "wenas"

@app.get("/personajes", tags=["API_south_park"])
async def get_personajes():
    return await personajes_servicios()

# CRUD Usuarios MongoDB
@app.post("/usuarios", tags=["CRUD MongoDB"])
def crear_usuario(usuario: Usuario):
    usuario_id = mongoDB.crear_usuario(usuario.dict())
    return {"id": usuario_id}

@app.get("/usuarios", tags=["CRUD MongoDB"])
def listar_usuarios():
    return mongoDB.obtener_usuarios()

@app.get("/usuarios/{usuario_id}", tags=["CRUD MongoDB"])
def obtener_usuario(usuario_id: str):
    usuario = mongoDB.obtener_usuario_por_id(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/usuarios/{usuario_id}", tags=["CRUD MongoDB"])
def actualizar_usuario(usuario_id: str, usuario: Usuario):
    if not mongoDB.actualizar_usuario(usuario_id, usuario.dict()):
        raise HTTPException(status_code=404, detail="Usuario no encontrado o sin cambios")
    return {"mensaje": "Usuario actualizado"}

@app.delete("/usuarios/{usuario_id}", tags=["CRUD MongoDB"])
def eliminar_usuario(usuario_id: str):
    if not mongoDB.eliminar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}

@app.delete("/eliminar_db", tags=["CRUD MongoDB"])
def eliminar_base_datos():
    try:
        mongoDB.client.drop_database("FastAPI")
        return {"mensaje": "Base de datos 'FastAPI' eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))