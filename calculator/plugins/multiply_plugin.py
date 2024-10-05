from calculator.commands import Command

# Command class for multiplication
class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a  # First operand
        self.b = b  # Second operand

    def execute(self):
        """Perform multiplication and return the result."""
        return self.a * self.b

# Register function to dynamically load the MultiplyCommand
def register():
    return MultiplyCommand
