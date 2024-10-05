import pytest
from calculator.commands import Command, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Test Command class raising NotImplementedError
def test_command_execute_not_implemented():
    command = Command()
    with pytest.raises(NotImplementedError, match="Subclasses must implement the 'execute' method."):
        command.execute()

# Test Repr for AddCommand
def test_add_command_repr():
    add_command = AddCommand(2, 3)
    assert repr(add_command) == "Add 2 and 3 = 5", "AddCommand __repr__ failed"

# Test Repr for SubtractCommand
def test_subtract_command_repr():
    subtract_command = SubtractCommand(5, 3)
    assert repr(subtract_command) == "Subtract 5 and 3 = 2", "SubtractCommand __repr__ failed"

# Test Repr for MultiplyCommand
def test_multiply_command_repr():
    multiply_command = MultiplyCommand(4, 3)
    assert repr(multiply_command) == "Multiply 4 and 3 = 12", "MultiplyCommand __repr__ failed"

# Test Repr for DivideCommand
def test_divide_command_repr():
    divide_command = DivideCommand(10, 2)
    assert repr(divide_command) == "Divide 10 by 2 = 5.0", "DivideCommand __repr__ failed"

# Additional test for Divide by zero scenario (covered in test_calculator.py but for completeness)
def test_divide_command_by_zero_repr():
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()
