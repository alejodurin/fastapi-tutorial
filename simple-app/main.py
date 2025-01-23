# main.py
from fastapi import FastAPI
import uvicorn
from routes import simple_route # Importamos la ruta que hemos agregado

app = FastAPI()

# Incluimos la ruta desde la carpeta que hemos creado
app.include_router(simple_route.router)

@app.get("/")
def home():
  return {"mensaje": "Hola desde main.py"}

if __name__ == "__main__":
    # Correr el servidor uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000,)