import pytest
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Fixture to set up a calculator instance before each test
@pytest.fixture
def calc():
    return Calculator()

# Existing Tests
def test_add_command(calc):
    add_command = AddCommand(10, 5)
    result = calc.compute(add_command)
    assert result == 15, "Addition result is incorrect"

def test_subtract_command(calc):
    sub_command = SubtractCommand(10, 5)
    result = calc.compute(sub_command)
    assert result == 5, "Subtraction result is incorrect"

def test_multiply_command(calc):
    multiply_command = MultiplyCommand(10, 5)
    result = calc.compute(multiply_command)
    assert result == 50, "Multiplication result is incorrect"

def test_divide_command(calc):
    divide_command = DivideCommand(10, 5)
    result = calc.compute(divide_command)
    assert result == 2, "Division result is incorrect"

def test_divide_by_zero(calc):
    # Test divide by zero scenario
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.compute(divide_command)

# New Tests to Improve Coverage

# Test Plugin Loading (Success Case)
def test_load_plugin_success():
    calc = Calculator()
    calc.load_plugin('add_plugin')  # Assuming add_plugin exists
    assert 'add_plugin' in calc.plugins  # Verify the plugin is loaded
    assert calc.plugins['add_plugin'] is not None  # Ensure plugin is registered

# Test Plugin Loading (Failure Case)
def test_load_plugin_failure():
    calc = Calculator()
    with pytest.raises(ImportError, match="Failed to load plugin: non_existent_plugin"):
        calc.load_plugin('non_existent_plugin')  # Test for a plugin that doesn’t exist

# Test Command Creation (Success Case)
def test_create_command_success():
    calc = Calculator()
    calc.load_plugin('add_plugin')  # Assuming add_plugin exists
    command = calc.create_command('add_plugin', 2, 3)  # Create add command with 2 and 3
    assert command is not None  # Ensure command is created successfully
    assert command.execute() == 5  # Ensure the command works correctly

# Test Command Creation (Failure Case)
def test_create_command_failure():
    calc = Calculator()
    with pytest.raises(ValueError, match="Plugin not found: non_existent_plugin"):
        calc.create_command('non_existent_plugin', 2, 3)  # Test for plugin that hasn’t been loaded
