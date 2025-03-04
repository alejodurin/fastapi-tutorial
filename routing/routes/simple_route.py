# simple_route.py
from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()
todo_list = []
@todo_router.post("/todo")
async def agregar_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "mensaje": "Todo agregado exitosamente."
    }

@todo_router.get("/todo")
async def obtener_todo() -> dict:
   return {
     "todos": todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def obtener_un_todo(todo_id: int = Path(title="El ID de Todo a buscar")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
           return {
              "todo": todo
            }
    return {
       "mensaje": "Todo con ID provisto no existe."
    }

@todo_router.put("/todo/{todo_id}")
async def actualizar_todo(todo_data: TodoItem, todo_id: int = Path(title="El ID de Todo para actualizar")) -> dict:
    for todo in todo_list:
       if todo.id == todo_id:
          todo.item = todo_data.item
          return {
              "mensaje": "Todo fue actualizado exitosamente."
              }
    return {
        "mensaje": "Todo con ID provisto no existe."
    }


@todo_router.delete("/todo/{todo_id}")
async def borrar_un_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "mensaje": "Todo borrado exitosamente."
            }
    return {
        "mensaje": "Todo con ID provisto no existe."
    }

@todo_router.delete("/todo")
async def borrar_todo() -> dict:
    todo_list.clear()
    return {
        "mensaje": "Todos borrados exitosamente."
    }