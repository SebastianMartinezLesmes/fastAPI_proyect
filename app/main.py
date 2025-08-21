from fastapi import FastAPI
from app.routes import (
    south_park_routes,
    mongodb_routes,
    mysql_routes,
    oracle_routes,
    postgresql_routes,
    local_storage_routes,
)
app = FastAPI()

@app.get("/", tags=["Inicio"])
def index():
    return "wenas"

# Registrar routers
app.include_router(south_park_routes.router)
app.include_router(local_storage_routes.router)

# DB noSQL
app.include_router(mongodb_routes.router)

# DB SQL
app.include_router(mysql_routes.router)
app.include_router(oracle_routes.router)
app.include_router(postgresql_routes.router)
