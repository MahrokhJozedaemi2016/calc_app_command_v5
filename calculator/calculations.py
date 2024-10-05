from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []  # Class-level attribute for storing calculation history

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        # Return a copy of the history to avoid accidental modification
        return cls.history.copy()

    @classmethod
    def clear_history(cls):
        """Completely clear the stored history of calculations."""
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if no history exists."""
        # Simplified return expression for clarity
        return cls.history[-1] if cls.history else None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        # Use list comprehension to search for calculations with the specified operation
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
