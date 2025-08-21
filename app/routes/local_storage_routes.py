from fastapi import APIRouter
from app.services import local_storage

router = APIRouter(prefix="/localstorage", tags=["LocalStorage"])

# Crear un nuevo localStorage
@router.post("/create")
def create_storage():
    return local_storage.create_storage()

# Obtener todos los datos
@router.get("/")
def get_all():
    return local_storage.get_all()

# Obtener un valor por clave
@router.get("/{key}")
def get_item(key: str):
    return local_storage.get_item(key)

# Agregar o actualizar un valor
@router.post("/{key}")
def set_item(key: str, value: str):
    return local_storage.set_item(key, value)

# Eliminar un valor
@router.delete("/{key}")
def delete_item(key: str):
    return local_storage.delete_item(key)

# Eliminar todo el localStorage
@router.delete("/")
def clear_storage():
    return local_storage.clear_storage()
