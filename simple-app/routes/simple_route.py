# routes/simple_route.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/hola")
def say_hello():
    return {"mensaje": "Hola desde simple_route.py"}