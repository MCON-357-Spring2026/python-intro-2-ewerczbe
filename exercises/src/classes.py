'''python
from calendar import error'''

# =============================================================================
# EXERCISE 2.1: Basic Class with Constructor
# =============================================================================
class Product:
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self) -> float:
        return self.price * self.quantity

    def is_in_stock(self) -> bool:
        return self.quantity > 0


# =============================================================================
# EXERCISE 2.2: Class with Class Attributes
# =============================================================================
class BankAccount:
    bank_name = "Python Bank"
    total_accounts = 0

    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = float(balance)
        BankAccount.total_accounts += 1

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_info(self) -> str:
        return f"Account {self.account_number} ({self.owner}): ${self.balance:.2f}"


# =============================================================================
# EXERCISE 2.3: Class Methods
# =============================================================================
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, kelvin: float) -> "Temperature":
        celsius = kelvin - 273.15
        return cls(celsius)

    def to_fahrenheit(self) -> float:
        return self.celsius * 9/5 + 32

    def to_kelvin(self) -> float:
        return self.celsius + 273.15


# =============================================================================
# EXERCISE 2.4: Inheritance
# =============================================================================
class Employee:
    def __init__(self, name: str, employee_id: str, base_salary: float):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def get_annual_salary(self) -> float:
        return self.base_salary

    def get_info(self) -> str:
        return f"ID: {self.employee_id} - {self.name}"


class Manager(Employee):
    def __init__(self, name: str, employee_id: str, base_salary: float,
                 department: str, bonus: float = 0):
        super().__init__(name, employee_id, base_salary)
        self.department = department
        self.bonus = bonus

    def get_annual_salary(self) -> float:
        return self.base_salary + self.bonus

    def get_info(self) -> str:
        return f"ID: {self.employee_id} - {self.name} (Manager, {self.department})"


class Developer(Employee):
    def __init__(self, name: str, employee_id: str, base_salary: float,
                 programming_languages: list = None):
        super().__init__(name, employee_id, base_salary)
        self.programming_languages = programming_languages if programming_languages else []

    def add_language(self, language: str) -> None:
        self.programming_languages.append(language)

    def get_info(self) -> str:
        return f"ID: {self.employee_id} - {self.name} (Developer)"

