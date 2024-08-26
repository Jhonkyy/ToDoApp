# TODO: Add code here

class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(f"{tag}")

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"


class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description: str) -> int:
        element_id = len(self.todos) + 1
        new_todo = Todo(code_id=element_id, title=title, description=description)
        self.todos[element_id] = new_todo
        return element_id

    def pending_todos(self) -> list:
        pending_list = [todo for todo in self.todos.values() if not todo.completed]
        return pending_list

    def completed_todos(self) -> list:
        completed_list = [todo for todo in self.todos.values() if todo.completed]
        return completed_list

    def tags_todo_count(self) -> dict:
        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1
        return tag_count
