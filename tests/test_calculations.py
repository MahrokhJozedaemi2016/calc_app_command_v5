'''My Calculator Test'''

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

# pytest.fixture to set up the calculation environment
@pytest.fixture
def setup_calculations():
    """Clear history and add sample calculations for tests."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation():
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history():
    """Test retrieving the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History does not contain the expected number of calculations"

def test_clear_history():
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_get_latest():
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest() 
    if latest is None:
        assert latest is None
    else:
        assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Latest calculation does not match expected values"

@pytest.mark.usefixtures("setup_calculations")  # Automatically use the fixture to set up test environment
def test_find_by_operation():
    """Test finding calculations in the history by operation type."""
    # Adding operations to the history
    calc1 = Calculation(Decimal('1'), Decimal('2'), add)
    calc1.perform()  # Perform the operation
    Calculations.add_calculation(calc1)  # Add it to history

    calc2 = Calculation(Decimal('3'), Decimal('4'), subtract)
    calc2.perform()
    Calculations.add_calculation(calc2)  # Add it to history

    # Test finding operations by type
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) >= 1, "No 'add' operations found in the history"

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None when history is empty"
