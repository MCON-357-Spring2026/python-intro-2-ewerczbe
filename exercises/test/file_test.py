import pytest
import os
from exercises.src.files import *


class TestFileOperations:
    """Test suite for basic file operations"""

    @pytest.fixture(autouse=True)
    def cleanup(self):
        """Cleanup test files before and after each test"""
        test_files = [
            "test_output.txt", "test_append.txt", "test_words.txt",
            "test_data.json", "test_update.json", "test_todos.json"
        ]
        # Cleanup before test
        for f in test_files:
            if os.path.exists(f):
                os.remove(f)

        yield

        # Cleanup after test
        for f in test_files:
            if os.path.exists(f):
                os.remove(f)

    def test_write_lines(self):
        """Test 3.1 - write_lines function"""
        write_lines("test_output.txt", ["Line 1", "Line 2", "Line 3"])
        with open("test_output.txt", "r") as f:
            content = f.read()
        assert "Line 1\n" in content and "Line 2\n" in content, "write_lines failed"

    def test_read_lines(self):
        """Test 3.2 - read_lines function"""
        write_lines("test_output.txt", ["Line 1", "Line 2", "Line 3"])
        lines = read_lines("test_output.txt")
        assert lines == ["Line 1", "Line 2", "Line 3"], f"read_lines failed: got {lines}"

    def test_append_line(self):
        """Test 3.3 - append_line function"""
        append_line("test_append.txt", "First")
        append_line("test_append.txt", "Second")
        lines = read_lines("test_append.txt")
        assert lines == ["First", "Second"], f"append_line failed: got {lines}"

    def test_count_words(self):
        """Test 3.4 - count_words function"""
        write_lines("test_words.txt", ["Hello World", "This is Python programming"])
        count = count_words("test_words.txt")
        assert count == 6, f"count_words failed: expected 6, got {count}"


class TestJSONOperations:
    """Test suite for JSON file operations"""

    @pytest.fixture(autouse=True)
    def cleanup(self):
        """Cleanup test files before and after each test"""
        test_files = ["test_data.json", "test_update.json"]
        for f in test_files:
            if os.path.exists(f):
                os.remove(f)

        yield

        for f in test_files:
            if os.path.exists(f):
                os.remove(f)

    def test_save_json(self):
        """Test 3.5 - save_json function"""
        test_data = {"name": "Alice", "scores": [85, 90, 88]}
        save_json("test_data.json", test_data)
        with open("test_data.json", "r") as f:
            loaded = json.load(f)
        assert loaded == test_data, "save_json failed"

    def test_load_json(self):
        """Test 3.6 - load_json function"""
        test_data = {"name": "Alice", "scores": [85, 90, 88]}
        save_json("test_data.json", test_data)
        loaded = load_json("test_data.json")
        assert loaded["name"] == "Alice", "load_json failed"
        assert loaded["scores"] == [85, 90, 88], "load_json failed"

    def test_update_json(self):
        """Test 3.7 - update_json function"""
        save_json("test_update.json", {"a": 1, "b": 2})
        update_json("test_update.json", b=20, c=30)
        result = load_json("test_update.json")
        assert result == {"a": 1, "b": 20, "c": 30}, f"update_json failed: {result}"


class TestTodoList:
    """Test suite for Exercise 3.8: TodoList class"""

    @pytest.fixture(autouse=True)
    def cleanup(self):
        """Cleanup test file before and after each test"""
        if os.path.exists("test_todos.json"):
            os.remove("test_todos.json")

        yield

        if os.path.exists("test_todos.json"):
            os.remove("test_todos.json")

    def test_todo_add(self):
        """Test TodoList add method returns incrementing IDs"""
        todo = TodoList("test_todos.json")
        id1 = todo.add("Task 1")
        id2 = todo.add("Task 2")
        assert id1 == 1 and id2 == 2, "add() should return incrementing IDs"

    def test_todo_get_pending(self):
        """Test TodoList get_pending method"""
        todo = TodoList("test_todos.json")
        todo.add("Task 1")
        todo.add("Task 2")
        assert len(todo.get_pending()) == 2, "Should have 2 pending"

    def test_todo_complete(self):
        """Test TodoList complete method"""
        todo = TodoList("test_todos.json")
        id1 = todo.add("Task 1")

        assert todo.complete(id1) == True, "complete() should return True"
        assert todo.complete(999) == False, "complete() should return False for invalid ID"

    def test_todo_complete_updates_pending(self):
        """Test TodoList completing a task updates pending list"""
        todo = TodoList("test_todos.json")
        todo.add("Task 1")
        id2 = todo.add("Task 2")

        todo.complete(1)
        pending = todo.get_pending()
        assert len(pending) == 1, "Should have 1 pending after completing 1"
        assert pending[0]["task"] == "Task 2", "Wrong pending task"

    def test_todo_persistence(self):
        """Test TodoList persists data to file"""
        todo = TodoList("test_todos.json")
        todo.add("Task 1")
        todo.add("Task 2")

        # Create new instance from same file
        todo2 = TodoList("test_todos.json")
        assert len(todo2.get_all()) == 2, "Should load 2 todos from file"

