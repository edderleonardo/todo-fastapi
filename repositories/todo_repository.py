"""
Repositories provide an abstraction layer for data persistence operations,
encapsulating interactions with databases or external data sources.
They offer standardized methods for storing, retrieving, updating, and deleting data.
"""

from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str


class Todo(TodoCreate):
    id: int
    completed: bool = False
    
    
class TodoRepository:
    
    def __init__(self):
        self.todos = []
    
    def create_todo(self, todo: TodoCreate) -> Todo:
        new_todo = Todo(id=len(self.todos) + 1, **todo.model_dump())
        self.todos.append(new_todo)
        return new_todo

    def get_todos(self) -> list[Todo]:
        return self.todos

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo_by_id(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        for todo in self.todos:
            if todo.id == todo_id:
                todo.title = updated_todo.title
                todo.completed = not todo.completed
                return todo
        return None

    def delete_todo_by_id(self, todo_id: int) -> bool:
        for index, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[index]
                return True
        return False