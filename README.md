# Python Crash Course: Functions, Classes, Files & JSON

This assignment covers core Python concepts that form the foundation for Django development.

## 📁 Project Structure

```
├── demo/
│   └── demo.py                    # Complete working examples
├── exercises/src/
│   ├── functions.py    # Functions practice
│   ├── classes.py      # Classes practice
│   ├── file.py   # Files & JSON practice
│   └── project.py  # Mini-project (all concepts)
└── README.md
```

## 🎯 Learning Objectives

By completing these exercises, you will practice:

- **Functions**: positional/keyword arguments, default values, `*args`, `**kwargs`, lambdas
- **Classes**: constructors, instance/class attributes, methods, `@classmethod`, inheritance
- **Files**: reading, writing, and appending text files
- **JSON**: serializing and deserializing data with `json.dump()` and `json.load()`

## 🚀 Getting Started

### Step 1: Review the Demo

Start by running the demo to see all concepts in action:

```bash
python demo/demo.py
```

The demo file contains fully working examples for every concept covered in the exercises. Use it as a reference while completing your work.

### Step 2: Complete the Exercises

Work through each exercise file in order. Each file contains:

- Clear instructions for what to implement
- `TODO` comments marking where to write your code
- Starter code with function/class signatures already defined

| File | Topics Covered |
|------|----------------|
| `functions.py` | Positional args, defaults, `*args`, `**kwargs`, lambdas |
| `classes.py` | Constructors, attributes, methods, inheritance |
| `file.py` | File I/O, JSON read/write, persistence |
| `project.py` | Mini-project combining all concepts |

## 📝 Exercise Details

### Exercise 1: Functions

Practice writing reusable functions with various parameter types:

- `calculate_area()` — basic positional arguments
- `format_price()` — default parameter values
- `find_max()` — variable arguments with `*args`
- `build_tag()` — keyword arguments with `**kwargs`
- `send_notification()` — combining all parameter types
- Lambda expressions — anonymous functions for sorting and filtering

### Exercise 2: Classes

Build classes with proper object-oriented design:

- `Product` — constructors and instance attributes
- `BankAccount` — class attributes and instance methods
- `Temperature` — class methods as alternative constructors
- `Employee`, `Manager`, `Developer` — inheritance hierarchy

### Exercise 3: Files and JSON

Work with file I/O and data serialization:

- Reading and writing text files
- Appending to existing files
- Saving and loading JSON data
- `TodoList` class — a complete CRUD example with persistence

### Exercise 4: Library Management System

A mini-project that brings everything together:

- Helper functions using `*args` and `**kwargs`
- `Book` and `Borrower` classes with serialization
- `Library` class managing the full system
- Data persistence with JSON files

## 💡 Tips for Success

1. **Run the demo first** — See how each concept works before implementing it yourself

2. **Read the docstrings** — Each function/class has detailed documentation explaining expected behavior

3. **Work incrementally** — Complete one exercise at a time; don't skip ahead

4. **Test as you go** — Run your file frequently to check your progress

5. **Use the demo as reference** — If you're stuck, find a similar example in `demo/demo.py`

## 📚 Quick Reference

### Function Parameters

```python
def example(required, optional="default", *args, **kwargs):
    pass
```

### Class Structure

```python
class MyClass:
    class_attr = "shared"           # Class attribute
    
    def __init__(self, value):      # Constructor
        self.value = value          # Instance attribute
    
    def method(self):               # Instance method
        return self.value
    
    @classmethod
    def from_string(cls, text):     # Class method
        return cls(int(text))
```

### File Operations

```python
# Write
with open("file.txt", "w") as f:
    f.write("content")

# Read
with open("file.txt", "r") as f:
    content = f.read()

# Append
with open("file.txt", "a") as f:
    f.write("more content")
```

### JSON Operations

```python
import json

# Save to file
with open("data.json", "w") as f:
    json.dump(my_dict, f, indent=2)

# Load from file
with open("data.json", "r") as f:
    my_dict = json.load(f)
```

## ✅ Submission

Complete all four exercise files and push your changes to your repository. Make sure all your code runs without errors before submitting.

Good luck! 🐍