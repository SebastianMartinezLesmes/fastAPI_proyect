## Clonacion del proyecto con Git
```powershell
git clone https://github.com/SebastianMartinezLesmes/fastAPI_proyect.git
``` 

## Creación del entorno virtual
```Windows (PowerShell)
python -m venv nombre_del_entorno
``` 
```linux/os (bash)
python3 -m venv nombre_del_entorno
``` 

### Entrar en el entorno virtual
```Windows (PowerShell)
nombre_del_entorno\Scripts\activate
```
```linux/os (bash)
source nombre_del_entorno/bin/activate
```

### Instalar dependencias
```
pip install -r requeriments.txt
```
### Para visualizar las dependencias consulta el archivo requirements.txt 
```
pip freeze requeriments.txt
```
```
pip list
```
### Salir del entorno virtual
```Windows (PowerShell)
deactivate
```
```linux/os (bash)
deactivate
```

### Ejecutar servidor local (Generación de cache)
```
uvicorn app.main:app --reload
```
### Ejecutar servidor local (Sin generar cache)
``` Windows (PowerShell)
# Windows
set PYTHONDONTWRITEBYTECODE=1 && uvicorn app.main:app --reload
```
```linux/os (bash)
PYTHONDONTWRITEBYTECODE=1 uvicorn app.main:app --reload
```

[Ruta de consultas de fastAPI](http://127.0.0.1:8000/docs)


## Información del proyecto

Este proyecto está desarrollado con **FastAPI** y tiene como objetivo demostrar la integración de múltiples fuentes de datos, tanto externas (APIs) como internas (bases de datos SQL y NoSQL).  

Se incluyen distintos endpoints organizados por módulos:

---

### 1. Endpoint: Consulta API de South Park  
- Permite realizar consultas a una API pública de **South Park**.  
- Ejemplo de funcionalidad:
  - Obtener listado de personajes.
  - Buscar personajes por nombre.
  - Filtrar información relevante (episodios, frases, etc.).

---

### 2. Endpoints: CRUD en bases de datos **relacionales**  
Se implementan conexiones y operaciones CRUD (Create, Read, Update, Delete) con distintas bases de datos SQL.  

**Bases de datos soportadas:**
- **MySQL**
- **PostgreSQL** (con `psycopg2-binary`)
- **Oracle**

**Funcionalidades principales:**
- Verificación de conexión con la base de datos.
- Creación y eliminación de **bases de datos**.
- Creación y eliminación de **tablas**.
- Operaciones CRUD sobre registros (insertar, consultar, actualizar y borrar).

---

### 3. Endpoints: CRUD en bases de datos **no relacionales**  
Actualmente soporta **MongoDB**.  

**Funcionalidades principales:**
- Verificación de conexión con la base de datos.
- Creación y eliminación de colecciones.
- Operaciones CRUD sobre documentos (insertar, consultar, actualizar y borrar).

---

## estructura del proyecto


---

## Arquitectura del proyecto

El proyecto está organizado siguiendo buenas prácticas de FastAPI:

```
app/
├── main.py # Punto de entrada de la aplicación
├── routes/ # Definición de endpoints (routers)
│ ├── south_park_routes.py
│ ├── mysql_routes.py
│ ├── postgresql_routes.py
│ ├── oracle_routes.py
│ └── mongodb_routes.py
├── services/ # Lógica de conexión a las bases de datos
│ ├── mysql.py
│ ├── postgresql.py
│ ├── oracle.py
│ └── mongodb.py
└── models/ # Modelos Pydantic y esquemas de datos
```



Licencia

Agregar una licencia (ej. MIT, Apache 2.0).