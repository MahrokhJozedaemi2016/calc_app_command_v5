class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a + self.b

    def __repr__(self):
        return f"Add {self.a} and {self.b} = {self.execute()}"

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a - self.b

    def __repr__(self):
        return f"Subtract {self.a} and {self.b} = {self.execute()}"

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return self.a * self.b

    def __repr__(self):
        return f"Multiply {self.a} and {self.b} = {self.execute()}"

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b

    def __repr__(self):
        return f"Divide {self.a} by {self.b} = {self.execute()}"
