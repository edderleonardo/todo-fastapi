"""
Routers in APIs organize and group related endpoints (routes) into separate
modules or files, enhancing code modularity and structure.
"""

from fastapi import APIRouter

from controllers.todo_controller import Todo, TodoController, TodoCreate

router = APIRouter()
todo_controller = TodoController()


@router.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    return todo_controller.create_todo(todo)


@router.get("/todos", response_model=list[Todo])
async def get_todo():
    return todo_controller.get_todos()


@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):
    return todo_controller.get_todo_by_id(todo_id)

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    return todo_controller.update_todo_by_id(todo_id, updated_todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return todo_controller.delete_todo_by_id(todo_id)
