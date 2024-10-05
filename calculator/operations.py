from decimal import Decimal

# Define the functions with type hints
def add(a: Decimal, b: Decimal) -> Decimal:
    """Perform addition of two Decimal numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Perform subtraction of two Decimal numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Perform multiplication of two Decimal numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division of two Decimal numbers, checking for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
