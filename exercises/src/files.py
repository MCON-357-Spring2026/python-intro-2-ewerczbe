import json
import os


# =============================================================================
# EXERCISE 3.1: Writing to a File
# =============================================================================
def write_lines(filepath: str, lines: list) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


# =============================================================================
# EXERCISE 3.2: Reading from a File
# =============================================================================
def read_lines(filepath: str) -> list:
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


# =============================================================================
# EXERCISE 3.3: Appending to a File
# =============================================================================
def append_line(filepath: str, line: str) -> None:
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# =============================================================================
# EXERCISE 3.4: Count Words in a File
# =============================================================================
def count_words(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return len(text.split())


# =============================================================================
# EXERCISE 3.5: Write Dictionary to JSON File
# =============================================================================
def save_json(filepath: str, data: dict) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# =============================================================================
# EXERCISE 3.6: Load Dictionary from JSON File
# =============================================================================
def load_json(filepath: str) -> dict:
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# =============================================================================
# EXERCISE 3.7: Update JSON File
# =============================================================================
def update_json(filepath: str, **updates) -> None:
    data = load_json(filepath)
    data.update(updates)
    save_json(filepath, data)


# =============================================================================
# EXERCISE 3.8: Todo List Manager
# =============================================================================
class TodoList:
    def __init__(self, filepath: str):
        self.filepath = filepath
        try:
            self.todos = load_json(filepath)
        except FileNotFoundError:
            self.todos = []

    def _save(self) -> None:
        save_json(self.filepath, self.todos)

    def _next_id(self) -> int:
        if not self.todos:
            return 1
        return max(todo["id"] for todo in self.todos) + 1

    def add(self, task: str) -> int:
        todo_id = self._next_id()
        new_todo = {"id": todo_id, "task": task, "done": False}
        self.todos.append(new_todo)
        self._save()
        return todo_id

    def complete(self, todo_id: int) -> bool:
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["done"] = True
                self._save()
                return True
        return False

    def get_pending(self) -> list:
        return [todo for todo in self.todos if not todo["done"]]

    def get_all(self) -> list:
        return self.todos