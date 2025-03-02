# simple_route.py
from fastapi import APIRouter
todo_router = APIRouter()

todo_list = []
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {"mensaje": "Todo agregado exitosamente"}
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}