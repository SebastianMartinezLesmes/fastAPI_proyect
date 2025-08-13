from bson import ObjectId
from app.config.settings import db, client

usuarios_collection = db["usuarios"]

def check_database_connection():
    try:
        client.server_info()  
        return {"status": "success", "message": "Conectado a la base de datos"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"No se pudo conectar a la base de datos: {str(e)}")
                            
def crear_usuario(usuario: dict):
    result = usuarios_collection.insert_one(usuario)
    return str(result.inserted_id)

def obtener_usuarios():
    usuarios = list(usuarios_collection.find())
    for usuario in usuarios:
        usuario["_id"] = str(usuario["_id"])
    return usuarios

def obtener_usuario_por_id(usuario_id: str):
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        usuario["_id"] = str(usuario["_id"])
    return usuario

def actualizar_usuario(usuario_id: str, nuevos_datos: dict):
    result = usuarios_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": nuevos_datos}
    )
    return result.modified_count > 0

def eliminar_usuario(usuario_id: str):
    result = usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
    return result.deleted_count > 0
