from typing import Union, NoReturn

Number = Union[int, float]

class Calculator:
    def __init__(self) -> None:
        self.result: Number = 0

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers."""
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base: Number, exponent: Number) -> Number:
        """Calculate base raised to the power of exponent."""
        return base ** exponent

    def square_root(self, number: Number) -> float:
        """Calculate the square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return number ** 0.5

    def percentage(self, number: Number, percent: Number) -> float:
        """Calculate percentage of a number."""
        return (number * percent) / 100

    def clear(self) -> Number:
        """Reset the calculator."""
        self.result = 0
        return self.result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(5, 3))        # Output: 8
    print(calc.subtract(10, 4))  # Output: 6
    print(calc.multiply(2, 3))   # Output: 6
    print(calc.divide(15, 3))    # Output: 5.0
    print(calc.power(2, 3))      # Output: 8
    print(calc.square_root(16))  # Output: 4.0
    print(calc.percentage(200, 10))  # Output: 20.0 