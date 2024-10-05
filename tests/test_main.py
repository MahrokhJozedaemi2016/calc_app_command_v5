import pytest
from main import calculate_and_store
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of add between 5 and 3 is 8"),
    ("10", "2", 'subtract', "The result of subtract between 10 and 2 is 8"),
    ("4", "5", 'multiply', "The result of multiply between 4 and 5 is 20"),
    ("20", "4", 'divide', "The result of divide between 20 and 4 is 5"),
    ("1", "1", 'divide', "The result of divide between 1 and 1 is 1"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero."),
    ("9", "3", 'unknown', "Unknown operation: unknown."),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_store(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_store function with various inputs."""
    calculate_and_store(a_string, b_string, operation_string)  # Use the correct function
    captured = capsys.readouterr().out.strip().rstrip(".")
    assert captured == expected_string.rstrip(".")
