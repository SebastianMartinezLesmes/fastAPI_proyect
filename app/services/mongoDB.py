from pymongo import MongoClient
from bson import ObjectId

# Conexión a MongoDB (cambiar si usas Atlas)
client = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección
db = client["FastAPI"]
usuarios_collection = db["usuarios"]

# Funciones CRUD
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
