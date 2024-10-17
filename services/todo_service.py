"""
Services contain the core business logic of the API, implementing specific
functionalities and operations required by the application.
They abstract complex business rules from the API endpoints.
"""

from repositories.todo_repository import Todo, TodoCreate, TodoRepository


class TodoService:
    def __init__(self):
        self.todos_repository = TodoRepository()

    def create_todo(self, todo: TodoCreate) -> Todo:
        return self.todos_repository.create_todo(todo)

    def get_todos(self) -> list[Todo]:
        return self.todos_repository.get_todos()

    def get_todo_by_id(self, todo_id: int) -> Todo | None:
        return self.todos_repository.get_todo_by_id(todo_id)

    def update_todo_by_id(self, todo_id: int, updated_todo: TodoCreate) -> Todo | None:
        return self.todos_repository.update_todo_by_id(todo_id, updated_todo)

    def delete_todo_by_id(self, todo_id: int) -> bool:
        return self.todos_repository.delete_todo_by_id(todo_id)
