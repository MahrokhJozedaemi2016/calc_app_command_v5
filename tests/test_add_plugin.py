import pytest
from calculator.plugins.add_plugin import AddCommand, register

def test_add_command_execute():
    """Test the execute method of AddCommand"""
    add_command = AddCommand(5, 3)
    result = add_command.execute()
    assert result == 8, "AddCommand execute method failed"

def test_add_command_register():
    """Test the register function for AddCommand"""
    command_class = register()
    assert command_class == AddCommand, "AddCommand register function failed"
