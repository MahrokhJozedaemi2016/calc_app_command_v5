import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    # Define operation mappings for both Calculator and Calculation tests
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    # Generate test data
    for _ in range(num_records):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Ensure b is not zero for divide operations
        if operation_func == divide:
            b = Decimal('1') if b == Decimal('0') else b

        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        except ValueError as ve:
            if str(ve) == "Cannot divide by zero":
                expected = "Cannot divide by zero"
            else:
                raise ve  # Re-raise other value errors not related to divide by zero

        yield a, b, operation_name, operation_func, expected


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    # Check if the test is expecting any of the dynamically generated fixtures
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        parameters = list(generate_test_data(num_records))

        # Adjust parameters according to the requested test function
        if 'operation_name' in metafunc.fixturenames:
            modified_parameters = [(a, b, op_name, expected) for a, b, op_name, _, expected in parameters]
        else:
            modified_parameters = [(a, b, op_func, expected) for a, b, _, op_func, expected in parameters]

        # Parametrize the test function with the generated data
        metafunc.parametrize("a,b,operation,expected", modified_parameters)
