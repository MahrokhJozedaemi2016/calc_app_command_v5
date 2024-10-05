import pytest
from calculator.plugins.multiply_plugin import MultiplyCommand, register

def test_multiply_command_execute():
    """Test the execute method of MultiplyCommand"""
    multiply_command = MultiplyCommand(4, 5)
    result = multiply_command.execute()
    assert result == 20, "MultiplyCommand execute method failed"

def test_multiply_command_register():
    """Test the register function for MultiplyCommand"""
    command_class = register()
    assert command_class == MultiplyCommand, "MultiplyCommand register function failed"
