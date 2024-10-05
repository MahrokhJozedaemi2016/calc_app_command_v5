from calculator.calculator import Calculator
from calculator.commands import AddCommand, DivideCommand

if __name__ == "__main__":
    calc = Calculator()

    # Example: Running AddCommand with multiprocessing
    add_command = AddCommand(10, 5)
    calc.compute_with_multiprocessing(add_command)

    # Example: Running DivideCommand with multiprocessing
    divide_command = DivideCommand(20, 4)
    calc.compute_with_multiprocessing(divide_command)
