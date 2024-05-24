from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.services.consultas import (
    personajes_servicios,
)

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return "wenas"

@app.get("/personajes")
async def get_personajes():
    return await personajes_servicios()