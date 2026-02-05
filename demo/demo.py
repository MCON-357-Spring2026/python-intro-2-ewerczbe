"""
Python Crash Course Demo
=========================
Demonstrates: Functions, Classes, Files, and JSON

Run this file to see all concepts in action:
python python_demo.py
"""

import json
from datetime import datetime


# =============================================================================
# PART 1: FUNCTIONS
# =============================================================================

print("=" * 60)
print("PART 1: FUNCTIONS")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 Positional Arguments
# -----------------------------------------------------------------------------
print("\n--- 1.1 Positional Arguments ---")

def format_full_name(first: str, last: str) -> str:
    """Format first and last name with proper casing."""
    first = first.strip().title()
    last = last.strip().title()
    return f"{first} {last}"

# Arguments passed in order
print(format_full_name("mary", "smith"))       # Mary Smith
print(format_full_name("  JOHN  ", "doe"))     # John Doe


# -----------------------------------------------------------------------------
# 1.2 Named (Keyword) Arguments
# -----------------------------------------------------------------------------
print("\n--- 1.2 Named (Keyword) Arguments ---")

# Same function, but arguments specified by name (order doesn't matter)
print(format_full_name(last="Jones", first="Alice"))  # Alice Jones
print(format_full_name(first="Bob", last="Wilson"))   # Bob Wilson


# -----------------------------------------------------------------------------
# 1.3 Default Values
# -----------------------------------------------------------------------------
print("\n--- 1.3 Default Values ---")

def greet(name: str, punctuation: str = "!") -> str:
    """Greet someone with optional punctuation."""
    return f"Hello, {name}{punctuation}"

print(greet("Students"))        # Uses default: Hello, Students!
print(greet("Students", "!!!")) # Override default: Hello, Students!!!
print(greet("World", "?"))      # Hello, World?


# -----------------------------------------------------------------------------
# 1.4 *args - Variable Positional Arguments
# -----------------------------------------------------------------------------
print("\n--- 1.4 *args - Variable Positional Arguments ---")

def average(*args: float) -> float:
    """Calculate average of any number of values."""
    if not args:
        raise ValueError("At least one value is required")
    return sum(args) / len(args)

print(f"average(10, 20, 30) = {average(10, 20, 30)}")           # 20.0
print(f"average(5, 10) = {average(5, 10)}")                     # 7.5
print(f"average(100) = {average(100)}")                         # 100.0
print(f"average(1, 2, 3, 4, 5) = {average(1, 2, 3, 4, 5)}")     # 3.0


def concatenate(*words: str) -> str:
    """Join any number of words with spaces."""
    return " ".join(words)

print(concatenate("Hello", "World"))                    # Hello World
print(concatenate("Python", "is", "awesome", "!"))      # Python is awesome !


# -----------------------------------------------------------------------------
# 1.5 **kwargs - Variable Named Arguments
# -----------------------------------------------------------------------------
print("\n--- 1.5 **kwargs - Variable Named Arguments ---")

def print_profile(**kwargs):
    """Print any named attributes passed in."""
    print("Profile:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_profile(name="Mary", role="Student", course="Python")
print()
print_profile(username="jdoe", email="jdoe@example.com", active=True, login_count=42)


# -----------------------------------------------------------------------------
# 1.6 Combining Positional, *args, and **kwargs
# -----------------------------------------------------------------------------
print("\n--- 1.6 Combining Positional, *args, and **kwargs ---")

def log_event(event_type: str, *messages, **metadata):
    """
    Log an event with optional messages and metadata.

    Args:
        event_type: Required - type of event (positional)
        *messages: Optional - any number of log messages
        **metadata: Optional - any named metadata fields
    """
    print(f"[EVENT] {event_type}")
    for msg in messages:
        print(f"  - {msg}")
    if metadata:
        print(f"  Metadata: {metadata}")

log_event("LOGIN", "User authenticated", "Session started", user="mary", ip="127.0.0.1")
print()
log_event("ERROR", "Connection failed", "Retrying...", code=500, service="database")
print()
log_event("STARTUP")  # Just the event type, no messages or metadata


# -----------------------------------------------------------------------------
# 1.7 Lambdas (Anonymous Functions)
# -----------------------------------------------------------------------------
print("\n--- 1.7 Lambdas (Anonymous Functions) ---")

# Regular function
def square(x: int) -> int:
    return x * x

# Equivalent lambda
square_lambda = lambda x: x * x

print(f"square(5) = {square(5)}")                    # 25
print(f"square_lambda(5) = {square_lambda(5)}")      # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"add(3, 7) = {add(3, 7)}")                    # 10

# Lambda with sorting
numbers = [5, 2, 9, 1, 7]
print(f"Original list: {numbers}")

# Sort by value
sorted_asc = sorted(numbers)
print(f"Sorted ascending: {sorted_asc}")

# Sort by distance from 5 using lambda
sorted_by_distance = sorted(numbers, key=lambda n: abs(n - 5))
print(f"Sorted by distance from 5: {sorted_by_distance}")  # [5, 7, 2, 9, 1]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, range(10)))
print(f"Even numbers 0-9: {evens}")  # [0, 2, 4, 6, 8]

# Lambda with map
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(f"Squares of 1-5: {squared}")  # [1, 4, 9, 16, 25]


# =============================================================================
# PART 2: CLASSES
# =============================================================================

print("\n" + "=" * 60)
print("PART 2: CLASSES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 Constructors and Instance Attributes
# -----------------------------------------------------------------------------
print("\n--- 2.1 Constructors and Instance Attributes ---")

class Counter:
    """A simple counter that can be incremented."""

    def __init__(self, start: int = 0):
        """Constructor - runs when creating a new Counter."""
        self.value = start  # Instance attribute - unique to each object

# Create two separate Counter instances
c1 = Counter()       # starts at 0 (default)
c2 = Counter(10)     # starts at 10

print(f"c1.value = {c1.value}")  # 0
print(f"c2.value = {c2.value}")  # 10

# Each instance has its own value
c1.value = 5
print(f"After c1.value = 5:")
print(f"  c1.value = {c1.value}")  # 5
print(f"  c2.value = {c2.value}")  # 10 (unchanged)


# -----------------------------------------------------------------------------
# 2.2 Class Attributes
# -----------------------------------------------------------------------------
print("\n--- 2.2 Class Attributes ---")

class Counter:
    """Counter with class-level configuration."""

    # Class attributes - shared by ALL instances
    DEFAULT_STEP = 1
    description = "A simple counter"
    instance_count = 0  # Track how many counters exist

    def __init__(self, start: int = 0):
        self.value = start  # Instance attribute
        Counter.instance_count += 1  # Increment class attribute

# Access class attributes without creating an instance
print(f"Counter.DEFAULT_STEP = {Counter.DEFAULT_STEP}")
print(f"Counter.description = {Counter.description}")
print(f"Counter.instance_count = {Counter.instance_count}")

# Create some instances
c1 = Counter()
c2 = Counter(100)
c3 = Counter(50)

# Class attribute is shared - all instances see the same count
print(f"After creating 3 counters:")
print(f"  Counter.instance_count = {Counter.instance_count}")  # 3
print(f"  c1.instance_count = {c1.instance_count}")            # 3 (same)
print(f"  c2.instance_count = {c2.instance_count}")            # 3 (same)


# -----------------------------------------------------------------------------
# 2.3 Instance Methods
# -----------------------------------------------------------------------------
print("\n--- 2.3 Instance Methods ---")

class Counter:
    """Counter with instance methods."""

    DEFAULT_STEP = 1

    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int | None = None) -> int:
        """Increment and return the new value. Uses DEFAULT_STEP if no step provided."""
        step = step if step is not None else Counter.DEFAULT_STEP
        self.value += step
        return self.value

    def decrement(self, step: int = 1) -> int:
        """Decrement and return the new value."""
        self.value -= step
        return self.value

    def reset(self) -> None:
        """Reset counter to zero."""
        self.value = 0

    def display(self) -> str:
        """Return a string representation."""
        return f"Counter(value={self.value})"

c = Counter(10)
print(f"Initial: {c.display()}")           # Counter(value=10)
print(f"After increment(): {c.increment()}")    # 11
print(f"After increment(5): {c.increment(5)}")  # 16
print(f"After decrement(): {c.decrement()}")    # 15
print(f"After decrement(10): {c.decrement(10)}")# 5
c.reset()
print(f"After reset(): {c.display()}")     # Counter(value=0)


# -----------------------------------------------------------------------------
# 2.4 Class Methods
# -----------------------------------------------------------------------------
print("\n--- 2.4 Class Methods ---")

class Counter:
    """Counter with class methods as alternative constructors."""

    DEFAULT_STEP = 1

    def __init__(self, start: int = 0):
        self.value = start

    @classmethod
    def from_string(cls, text: str) -> "Counter":
        """Alternative constructor: create Counter from a string."""
        start = int(text)
        return cls(start)

    @classmethod
    def from_list(cls, values: list) -> "Counter":
        """Alternative constructor: create Counter starting at sum of list."""
        return cls(sum(values))

    @classmethod
    def get_default_step(cls) -> int:
        """Class method to access class attribute."""
        return cls.DEFAULT_STEP

# Regular constructor
c1 = Counter(50)
print(f"Counter(50): value = {c1.value}")

# Alternative constructor from string
c2 = Counter.from_string("100")
print(f"Counter.from_string('100'): value = {c2.value}")

# Alternative constructor from list
c3 = Counter.from_list([10, 20, 30])
print(f"Counter.from_list([10, 20, 30]): value = {c3.value}")

# Class method accessing class attribute
print(f"Counter.get_default_step() = {Counter.get_default_step()}")


# -----------------------------------------------------------------------------
# 2.5 Inheritance
# -----------------------------------------------------------------------------
print("\n--- 2.5 Inheritance ---")

class Counter:
    """Base counter class."""

    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int = 1) -> int:
        self.value += step
        return self.value

    def get_info(self) -> str:
        return f"Counter at {self.value}"


class LabeledCounter(Counter):
    """Counter with an additional label - inherits from Counter."""

    def __init__(self, start: int = 0, label: str = "default"):
        super().__init__(start)  # Call parent constructor
        self.label = label       # Add new attribute

    def get_info(self) -> str:
        # Child class can access parent's attributes
        return f"[{self.label}] Counter at {self.value}"


class BoundedCounter(Counter):
    """Counter with min/max limits - inherits from Counter."""

    def __init__(self, start: int = 0, min_val: int = 0, max_val: int = 100):
        super().__init__(start)
        self.min_val = min_val
        self.max_val = max_val

    def increment(self, step: int = 1) -> int:
        """Override to respect bounds."""
        new_value = self.value + step
        self.value = min(new_value, self.max_val)  # Don't exceed max
        return self.value

    def decrement(self, step: int = 1) -> int:
        """Override to respect bounds."""
        new_value = self.value - step
        self.value = max(new_value, self.min_val)  # Don't go below min
        return self.value


# Base class
base = Counter(10)
print(f"Base Counter: {base.get_info()}")
base.increment(5)
print(f"After increment(5): {base.get_info()}")

print()

# LabeledCounter inherits increment() from parent
labeled = LabeledCounter(0, label="session")
print(f"LabeledCounter: {labeled.get_info()}")
labeled.increment(10)  # Uses inherited method
print(f"After increment(10): {labeled.get_info()}")

print()

# BoundedCounter with limits
bounded = BoundedCounter(50, min_val=0, max_val=100)
print(f"BoundedCounter: value={bounded.value}, min={bounded.min_val}, max={bounded.max_val}")
print(f"increment(60): {bounded.increment(60)}")   # Capped at 100
print(f"decrement(150): {bounded.decrement(150)}") # Floored at 0


# -----------------------------------------------------------------------------
# 2.6 Method Overriding with super()
# -----------------------------------------------------------------------------
print("\n--- 2.6 Method Overriding with super() ---")

class Counter:
    """Base counter."""

    def __init__(self, start: int = 0):
        self.value = start

    def increment(self, step: int = 1) -> int:
        self.value += step
        return self.value


class LoggingCounter(Counter):
    """Counter that logs every increment."""

    def __init__(self, start: int = 0, name: str = "counter"):
        super().__init__(start)
        self.name = name
        self.history = []

    def increment(self, step: int = 1) -> int:
        """Override increment to add logging, then call parent method."""
        old_value = self.value
        result = super().increment(step)  # Call parent's increment
        log_entry = f"{self.name}: {old_value} -> {result} (+{step})"
        self.history.append(log_entry)
        print(f"  [LOG] {log_entry}")
        return result


lc = LoggingCounter(0, name="clicks")
lc.increment()
lc.increment(5)
lc.increment(3)
print(f"Final value: {lc.value}")
print(f"History: {lc.history}")


# =============================================================================
# PART 3: WORKING WITH FILES
# =============================================================================

print("\n" + "=" * 60)
print("PART 3: WORKING WITH FILES")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 Writing Text to a File
# -----------------------------------------------------------------------------
print("\n--- 3.1 Writing Text to a File ---")

# 'w' mode = write (overwrites existing content)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: Hello from Python!\n")
    f.write("Line 2: This is a demo file.\n")
    f.write("Line 3: Files are useful for persistence.\n")

print("Wrote 3 lines to notes.txt")

# Writing multiple lines at once
lines = [
    "Item A\n",
    "Item B\n",
    "Item C\n"
]
with open("items.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Wrote items.txt using writelines()")


# -----------------------------------------------------------------------------
# 3.2 Reading Text from a File
# -----------------------------------------------------------------------------
print("\n--- 3.2 Reading Text from a File ---")

# Read entire file as a single string
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("Contents of notes.txt:")
print(content)

# Read file line by line
print("Reading items.txt line by line:")
with open("items.txt", "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"  {line_number}: {line.strip()}")

# Read all lines into a list
with open("notes.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()

print(f"\nRead {len(all_lines)} lines into a list")


# -----------------------------------------------------------------------------
# 3.3 Appending to a File
# -----------------------------------------------------------------------------
print("\n--- 3.3 Appending to a File ---")

# 'a' mode = append (adds to end of file)
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Line 4: This line was appended!\n")
    f.write(f"Line 5: Appended at {datetime.now()}\n")

print("Appended 2 lines to notes.txt")

# Verify by reading
with open("notes.txt", "r", encoding="utf-8") as f:
    print("\nUpdated contents:")
    print(f.read())


# =============================================================================
# PART 4: WORKING WITH JSON
# =============================================================================

print("=" * 60)
print("PART 4: WORKING WITH JSON")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 Python Dict → JSON File
# -----------------------------------------------------------------------------
print("\n--- 4.1 Python Dict → JSON File ---")

# Create a Python dictionary
course_data = {
    "course": "Python Crash Course",
    "topics": ["functions", "classes", "files", "json"],
    "week": 2,
    "instructor": {
        "name": "Dr. Smith",
        "email": "smith@university.edu"
    },
    "enrolled_students": 25,
    "active": True
}

# Write to JSON file
with open("course.json", "w", encoding="utf-8") as f:
    json.dump(course_data, f, indent=2)

print("Wrote course_data to course.json:")
print(json.dumps(course_data, indent=2))


# -----------------------------------------------------------------------------
# 4.2 JSON File → Python Dict
# -----------------------------------------------------------------------------
print("\n--- 4.2 JSON File → Python Dict ---")

# Read from JSON file
with open("course.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(f"Loaded course: {loaded_data['course']}")
print(f"Topics: {loaded_data['topics']}")
print(f"Instructor: {loaded_data['instructor']['name']}")
print(f"Active: {loaded_data['active']}")
print(f"Type of loaded_data: {type(loaded_data)}")


# -----------------------------------------------------------------------------
# 4.3 JSON String ↔ Python Object
# -----------------------------------------------------------------------------
print("\n--- 4.3 JSON String ↔ Python Object ---")

# Python object to JSON string
user = {"name": "Alice", "age": 30, "roles": ["admin", "user"]}
json_string = json.dumps(user)
print(f"JSON string: {json_string}")
print(f"Type: {type(json_string)}")

# JSON string to Python object
parsed = json.loads(json_string)
print(f"Parsed back: {parsed}")
print(f"Type: {type(parsed)}")
print(f"parsed['name'] = {parsed['name']}")


# -----------------------------------------------------------------------------
# 4.4 Working with Lists of Objects
# -----------------------------------------------------------------------------
print("\n--- 4.4 Working with Lists of Objects ---")

students = [
    {"id": 1, "name": "Alice", "grade": 95},
    {"id": 2, "name": "Bob", "grade": 87},
    {"id": 3, "name": "Charlie", "grade": 92}
]

# Write list to JSON
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=2)

print("Wrote students list to students.json")

# Read and process
with open("students.json", "r", encoding="utf-8") as f:
    loaded_students = json.load(f)

print("\nStudent grades:")
for student in loaded_students:
    print(f"  {student['name']}: {student['grade']}")

avg_grade = sum(s['grade'] for s in loaded_students) / len(loaded_students)
print(f"Average grade: {avg_grade:.1f}")


# =============================================================================
# PART 5: PUTTING IT ALL TOGETHER
# =============================================================================

print("\n" + "=" * 60)
print("PART 5: PUTTING IT ALL TOGETHER")
print("=" * 60)

class StudentGradebook:
    """
    A complete example combining classes, files, and JSON.

    Demonstrates:
    - Constructor and instance attributes
    - Instance methods
    - Class methods (alternative constructors)
    - File I/O
    - JSON serialization
    """

    DEFAULT_PASSING_GRADE = 60  # Class attribute

    def __init__(self, course_name: str):
        """Initialize a new gradebook."""
        self.course_name = course_name
        self.students = {}  # id -> {"name": str, "grades": list}

    @classmethod
    def from_json_file(cls, filepath: str) -> "StudentGradebook":
        """Alternative constructor: load gradebook from JSON file."""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        gradebook = cls(data["course_name"])
        gradebook.students = data.get("students", {})
        return gradebook

    def add_student(self, student_id: str, name: str) -> None:
        """Add a new student to the gradebook."""
        self.students[student_id] = {"name": name, "grades": []}

    def add_grade(self, student_id: str, grade: float) -> None:
        """Add a grade for a student."""
        if student_id not in self.students:
            raise ValueError(f"Student {student_id} not found")
        self.students[student_id]["grades"].append(grade)

    def get_average(self, student_id: str) -> float:
        """Get a student's average grade."""
        grades = self.students[student_id]["grades"]
        return sum(grades) / len(grades) if grades else 0.0

    def is_passing(self, student_id: str) -> bool:
        """Check if student is passing."""
        return self.get_average(student_id) >= self.DEFAULT_PASSING_GRADE

    def get_class_summary(self, **filters) -> dict:
        """
        Get summary statistics.
        Uses **kwargs for optional filters.
        """
        results = {
            "course": self.course_name,
            "total_students": len(self.students),
            "passing": 0,
            "failing": 0,
            "averages": {}
        }

        for sid, data in self.students.items():
            avg = self.get_average(sid)
            results["averages"][data["name"]] = round(avg, 1)
            if self.is_passing(sid):
                results["passing"] += 1
            else:
                results["failing"] += 1

        return results

    def save_to_json(self, filepath: str) -> None:
        """Save gradebook to JSON file."""
        data = {
            "course_name": self.course_name,
            "students": self.students
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def export_report(self, filepath: str) -> None:
        """Export a text report to a file."""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Grade Report: {self.course_name}\n")
            f.write("=" * 40 + "\n\n")

            for sid, data in self.students.items():
                avg = self.get_average(sid)
                status = "PASS" if self.is_passing(sid) else "FAIL"
                f.write(f"{data['name']} ({sid})\n")
                f.write(f"  Grades: {data['grades']}\n")
                f.write(f"  Average: {avg:.1f} - {status}\n\n")


# Demo the complete class
print("\n--- Creating and Using StudentGradebook ---")

# Create gradebook
gb = StudentGradebook("Python 101")

# Add students
gb.add_student("S001", "Alice Johnson")
gb.add_student("S002", "Bob Smith")
gb.add_student("S003", "Charlie Brown")

# Add grades using the add_grade method
gb.add_grade("S001", 95)
gb.add_grade("S001", 88)
gb.add_grade("S001", 92)

gb.add_grade("S002", 72)
gb.add_grade("S002", 68)
gb.add_grade("S002", 75)

gb.add_grade("S003", 55)
gb.add_grade("S003", 58)
gb.add_grade("S003", 52)

# Get summary
summary = gb.get_class_summary()
print(f"\nClass Summary:")
print(f"  Course: {summary['course']}")
print(f"  Total Students: {summary['total_students']}")
print(f"  Passing: {summary['passing']}")
print(f"  Failing: {summary['failing']}")
print(f"  Averages: {summary['averages']}")

# Save to JSON
gb.save_to_json("gradebook.json")
print("\nSaved gradebook to gradebook.json")

# Export text report
gb.export_report("grade_report.txt")
print("Exported report to grade_report.txt")

# Load from JSON (alternative constructor)
print("\n--- Loading Gradebook from JSON ---")
loaded_gb = StudentGradebook.from_json_file("gradebook.json")
print(f"Loaded course: {loaded_gb.course_name}")
print(f"Students: {list(loaded_gb.students.keys())}")

# Show the exported report
print("\n--- Contents of grade_report.txt ---")
with open("grade_report.txt", "r", encoding="utf-8") as f:
    print(f.read())


# =============================================================================
# SUMMARY
# =============================================================================

print("=" * 60)
print("DEMO COMPLETE!")
print("=" * 60)
print("""
Files created during this demo:
  - notes.txt      (text file demo)
  - items.txt      (writelines demo)
  - course.json    (JSON writing demo)
  - students.json  (JSON list demo)
  - gradebook.json (complete class demo)
  - grade_report.txt (text export demo)

Topics covered:
  ✓ Functions: positional args, keyword args, defaults
  ✓ Functions: *args, **kwargs, combining them
  ✓ Functions: lambda expressions
  ✓ Classes: constructors, instance attributes
  ✓ Classes: class attributes
  ✓ Classes: instance methods
  ✓ Classes: class methods (@classmethod)
  ✓ Classes: inheritance with super()
  ✓ Classes: method overriding
  ✓ Files: reading and writing text
  ✓ Files: appending to files
  ✓ JSON: dump/load (files), dumps/loads (strings)
""")