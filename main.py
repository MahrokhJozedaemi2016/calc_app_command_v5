from calculator.calculator import Calculator
from calculator.calculations import Calculations
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand  # Import command classes
from decimal import Decimal, InvalidOperation

# Available command mappings
operation_mappings = {
    'add': AddCommand,
    'subtract': SubtractCommand,
    'multiply': MultiplyCommand,
    'divide': DivideCommand
}

def display_menu():
    """Displays the list of available commands."""
    print("\nAvailable commands:")
    print("  add: Add two numbers")
    print("  subtract: Subtract two numbers")
    print("  multiply: Multiply two numbers")
    print("  divide: Divide two numbers")
    print("  history: View calculation history")
    print("  clear_history: Clear calculation history")
    print("  exit: Exit the calculator")

def calculate_and_store(a, b, operation_name):
    """Performs the calculation and stores it in history."""
    try:
        # Convert inputs to Decimal
        a_decimal, b_decimal = map(Decimal, [a, b])
        
        # Check if the operation exists in the mapping
        CommandClass = operation_mappings.get(operation_name)
        
        if CommandClass:
            # Create a command object for the operation
            command = CommandClass(a_decimal, b_decimal)
            calc = Calculator()
            result = calc.compute(command)
            print(f"The result of {operation_name} between {a} and {b} is {result}")
        else:
            print(f"Unknown operation: {operation_name}")
            return
        
        # Store the calculation in history
        Calculations.add_calculation(command)
        
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def prompt_for_numbers(operation_name):
    """Prompts the user to input two numbers for the operation."""
    print(f"\nEnter two numbers for {operation_name}:")
    try:
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        return a, b
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def interactive_calculator():
    """Runs the interactive calculator."""
    # Display initial welcome message
    print("Welcome to the interactive calculator!")
    print("Type 'menu' to see the available commands or 'exit' to quit.")

    while True:
        user_input = input("\nEnter a command: ").strip().lower()

        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'menu':
            display_menu()
        elif user_input == 'history':
            # View the history of calculations
            history = Calculations.get_history()
            if history:
                for idx, operation in enumerate(history, 1):
                    print(f"{idx}: {operation}")
            else:
                print("No history available.")
        elif user_input == 'clear_history':
            # Clear the calculation history
            Calculations.clear_history()
            print("Calculation history cleared.")
        elif user_input in operation_mappings:
            # If the user input matches an operation, prompt for two numbers
            a, b = prompt_for_numbers(user_input)
            if a and b:
                # Perform and store the calculation
                calculate_and_store(a, b, user_input)
        else:
            print("Invalid input. Please type 'menu' to see the available commands.")

if __name__ == "__main__":
    interactive_calculator()