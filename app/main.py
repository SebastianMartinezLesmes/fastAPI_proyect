from fastapi import FastAPI
from app.routes import south_park_routes, mongodb_routes

app = FastAPI()

@app.get("/", tags=["Inicio"])
def index():
    return "wenas"

# Registrar routers
app.include_router(south_park_routes.router)
app.include_router(mongodb_routes.router)
