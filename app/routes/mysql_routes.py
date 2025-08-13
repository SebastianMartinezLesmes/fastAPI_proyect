from fastapi import APIRouter, HTTPException
from app.models.usuario_model import Usuario

router = APIRouter(
    prefix="/MySQL",
    tags=["CRUD MySQL"]
)

@router.get("/check-db")
def check_mysql_db():
    try:
        # Aquí luego llamarías a tu lógica en services/mysql.py
        return {"status": "success", "message": "Conectado a MySQL"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
