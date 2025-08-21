# Diccionario en memoria que simula un localStorage
_local_storage = {}

def create_storage():
    global _local_storage
    _local_storage = {}
    return {"message": "Local storage creado exitosamente"}

def set_item(key: str, value: str):
    _local_storage[key] = value
    return {"message": f"Item '{key}' agregado/actualizado"}

def get_item(key: str):
    return {"key": key, "value": _local_storage.get(key)}

def get_all():
    return _local_storage

def delete_item(key: str):
    if key in _local_storage:
        del _local_storage[key]
        return {"message": f"Item '{key}' eliminado"}
    return {"error": f"Item '{key}' no encontrado"}

def clear_storage():
    global _local_storage
    _local_storage = {}
    return {"message": "Local storage eliminado"}
