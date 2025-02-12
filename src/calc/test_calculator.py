from .calculator import Calculator
import pytest


def test_calculator_operations():
    calc = Calculator()
    
    # Test addition
    assert calc.add(5, 3) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)  # Handle floating point precision
    
    # Test subtraction
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(3.5, 1.2) == pytest.approx(2.3)
    
    # Test multiplication
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(2.5, 2) == 5.0
    
    # Test division
    assert calc.divide(15, 3) == 5.0
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(5, 2) == 2.5
    
    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)
    
    # Test power
    assert calc.power(2, 3) == 8
    assert calc.power(2, 0) == 1
    assert calc.power(2, -1) == 0.5
    
    # Test square root
    assert calc.square_root(16) == 4.0
    assert calc.square_root(2) == pytest.approx(1.4142135623730951)
    
    # Test negative square root
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        calc.square_root(-1)
    
    # Test percentage
    assert calc.percentage(200, 10) == 20.0
    assert calc.percentage(100, 50) == 50.0
    assert calc.percentage(50, 25) == 12.5
    
    # Test clear
    assert calc.clear() == 0
    assert calc.result == 0


def test_calculator_chained_operations():
    calc = Calculator()
    
    # Test a series of operations
    result = calc.add(10, 5)        # 15
    result = calc.multiply(result, 2)  # 30
    result = calc.subtract(result, 5)  # 25
    result = calc.divide(result, 5)    # 5
    assert result == 5.0


def test_calculator_edge_cases():
    calc = Calculator()
    
    # Test very large numbers
    assert calc.add(1e15, 1e15) == 2e15
    
    # Test very small numbers
    assert calc.add(1e-15, 1e-15) == pytest.approx(2e-15)
    
    # Test mixed integer and float operations
    assert calc.multiply(2, 3.5) == 7.0
    
    # Test zero operations
    assert calc.multiply(0, 5) == 0
    assert calc.power(0, 2) == 0
    assert calc.power(2, 0) == 1


if __name__ == "__main__":
    # Run the tests and print results
    test_calculator_operations()
    test_calculator_chained_operations()
    test_calculator_edge_cases()
    print("All tests passed successfully!") 