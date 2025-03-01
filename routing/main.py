# main.py
from fastapi import FastAPI
import uvicorn
from routes.simple_route import todo_router

app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {
        "mensaje": "Hola desde main.py"
    }

app.include_router(todo_router)

if __name__ == "__main__":
    # Correr el servidor uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000,)