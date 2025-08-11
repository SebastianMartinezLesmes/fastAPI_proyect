from fastapi import APIRouter
from app.services.south_park import personajes_servicios

router = APIRouter(
    prefix="/personajes",
    tags=["API_south_park"]
)

@router.get("/")
async def get_personajes():
    return await personajes_servicios()
