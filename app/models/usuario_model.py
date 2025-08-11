from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
