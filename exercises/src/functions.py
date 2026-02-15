# =============================================================================
# EXERCISE 1.1: Basic Function with Positional Arguments
# =============================================================================
def calculate_area(width: float, height: float) -> float:
    return width * height


# =============================================================================
# EXERCISE 1.2: Function with Default Values
# =============================================================================
def format_price(amount: float, currency: str = "$", decimals: int = 2) -> str:
    return f"{currency}{round(amount, decimals)}"


# =============================================================================
# EXERCISE 1.3: Function with *args
# =============================================================================
def find_max(*args) -> float:
    if not args:
        raise ValueError("No arguments provided")
    return max(args)


# =============================================================================
# EXERCISE 1.4: Function with **kwargs
# =============================================================================
def build_tag(tag_name: str, **kwargs) -> str:
    if kwargs:
        attrs = " ".join(f'{key}="{value}"' for key, value in kwargs.items())
        return f"<{tag_name} {attrs}>"
    return f"<{tag_name}>"


# =============================================================================
# EXERCISE 1.5: Combining Parameters
# =============================================================================
def send_notification(recipient: str, message: str, *cc, **options) -> dict:
    return {
        "to": recipient,
        "message": message,
        "cc": list(cc),
        "options": options
    }


# =============================================================================
# EXERCISE 1.6: Lambda Expressions
# =============================================================================
double = lambda x: x * 2

is_even = lambda x: x % 2 == 0

last_char = lambda s: s[-1]

words = ["python", "java", "go", "javascript", "c"]
sorted_by_length = sorted(words, key=lambda w: len(w))

numbers = [-3, 5, -1, 8, 0, -2, 10]
positive_only = list(filter(lambda n: n > 0, numbers))