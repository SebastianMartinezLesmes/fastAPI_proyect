### Creación del entorno virtual
```python
python -m venv nombre_del_entorno
``` 
### Entrar en el entorno virtual
```
nombre_del_entorno\Scripts\activate
```
### Instalar dependencias
```
pip install -r requeriments.txt
```
### Para visualizar las dependencias de este proyecto, consulta el archivo requirements.txt con las siguientes líneas en la terminal
```
pip freeze requeriments.txt
```
```
pip list
```
### Salir del entorno virtual
```
deactivate
```
### Ejecutar servidor local (Generación de cache)
```
uvicorn main:app --reload
```
### Ejecutar servidor local (Sin generar cache)
```bash
# Windows
set PYTHONDONTWRITEBYTECODE=1 && uvicorn main:app --reload
```
```bash
# macOS/Linux
PYTHONDONTWRITEBYTECODE=1 uvicorn main:app --reload
```

[Ruta de consultas de fastAPI](http://127.0.0.1:8000/docs)
