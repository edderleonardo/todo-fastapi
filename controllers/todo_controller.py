"""
Controllers handle incoming requests, orchestrate the application’s logic,
and manage the flow of data between the API routes (endpoints) and the services layer.
"""
from fastapi import HTTPException

from services.todo_service import Todo, TodoCreate, TodoService


class TodoController:
    def __init__(self):
        self.todos_service = TodoService()

    def create_todo(self, todo: TodoCreate):
        return self.todos_service.create_todo(todo)

    def get_todos(self):
        return self.todos_service.get_todos()

    def get_todo_by_id(self, todo_id: int):
        todo = self.todos_service.get_todo_by_id(todo_id)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def update_todo_by_id(self, todo_id: int, todo_data: TodoCreate):
        todo = self.todos_service.update_todo_by_id(todo_id, todo_data)
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def delete_todo_by_id(self, todo_id: int):
        if self.todos_service.delete_todo_by_id(todo_id):
            return {"message": "Todo deleted successfully"}
        raise HTTPException(status_code=404, detail="Todo not found")