from .calculator import Calculator

def my_calc() -> None:
    """Interactive calculator function that demonstrates basic operations."""
    calc = Calculator()
    print("Welcome to My Calculator!")
    print("Performing some sample calculations...")
    
    # Demonstrate basic operations
    result = calc.add(10, 5)
    print(f"10 + 5 = {result}")
    
    result = calc.multiply(result, 2)
    print(f"Result * 2 = {result}")
    
    result = calc.power(result, 2)
    print(f"Result ^ 2 = {result}")
    
    result = calc.square_root(result)
    print(f"Square root of result = {result}")
    
    print("\nCalculator demonstration completed!")

def main() -> None:
    print("Hello from calc!")

__all__ = ['Calculator', 'my_calc']
