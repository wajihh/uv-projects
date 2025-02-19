from typing import Union, NoReturn, List
import math
from enum import Enum

Number = Union[int, float]

class AngleMode(Enum):
    DEGREES = "degrees"
    RADIANS = "radians"

class Calculator:
    def __init__(self) -> None:
        self.result: Number = 0
        self.memory: Number = 0
        self.angle_mode: AngleMode = AngleMode.DEGREES
        self.constants = {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
            'inf': math.inf
        }

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

    def set_angle_mode(self, mode: AngleMode) -> None:
        """Set the angle mode for trigonometric calculations."""
        self.angle_mode = mode

    def _convert_to_radians(self, angle: Number) -> float:
        """Convert angle to radians based on current angle mode."""
        return math.radians(angle) if self.angle_mode == AngleMode.DEGREES else angle

    def sin(self, angle: Number) -> float:
        """Calculate sine of an angle."""
        return math.sin(self._convert_to_radians(angle))

    def cos(self, angle: Number) -> float:
        """Calculate cosine of an angle."""
        return math.cos(self._convert_to_radians(angle))

    def tan(self, angle: Number) -> float:
        """Calculate tangent of an angle."""
        return math.tan(self._convert_to_radians(angle))

    def asin(self, value: Number) -> float:
        """Calculate inverse sine (arcsin)."""
        result = math.asin(value)
        return math.degrees(result) if self.angle_mode == AngleMode.DEGREES else result

    def acos(self, value: Number) -> float:
        """Calculate inverse cosine (arccos)."""
        result = math.acos(value)
        return math.degrees(result) if self.angle_mode == AngleMode.DEGREES else result

    def atan(self, value: Number) -> float:
        """Calculate inverse tangent (arctan)."""
        result = math.atan(value)
        return math.degrees(result) if self.angle_mode == AngleMode.DEGREES else result

    def log(self, number: Number, base: Number = 10) -> float:
        """Calculate logarithm with specified base (default is 10)."""
        return math.log(number, base)

    def ln(self, number: Number) -> float:
        """Calculate natural logarithm."""
        return math.log(number)

    def factorial(self, number: int) -> int:
        """Calculate factorial of a number."""
        if not isinstance(number, int) or number < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        return math.factorial(number)

    def exp(self, number: Number) -> float:
        """Calculate e raised to the power of number."""
        return math.exp(number)

    def nth_root(self, number: Number, n: Number) -> float:
        """Calculate the nth root of a number."""
        if number < 0 and n % 2 == 0:
            raise ValueError("Even root of negative number is undefined")
        return math.pow(number, 1/n)

    def memory_store(self, value: Number) -> None:
        """Store a value in memory."""
        self.memory = value

    def memory_recall(self) -> Number:
        """Recall the value stored in memory."""
        return self.memory

    def memory_clear(self) -> None:
        """Clear the memory."""
        self.memory = 0

    def memory_add(self, value: Number) -> None:
        """Add a value to memory."""
        self.memory += value

    def get_constant(self, name: str) -> float:
        """Get the value of a mathematical constant."""
        return self.constants.get(name, 0.0)

    def to_binary(self, number: int) -> str:
        """Convert decimal to binary."""
        if not isinstance(number, int):
            raise ValueError("Binary conversion only works with integers")
        return bin(number)[2:]  # Remove '0b' prefix

    def to_hex(self, number: int) -> str:
        """Convert decimal to hexadecimal."""
        if not isinstance(number, int):
            raise ValueError("Hexadecimal conversion only works with integers")
        return hex(number)[2:]  # Remove '0x' prefix

    def to_octal(self, number: int) -> str:
        """Convert decimal to octal."""
        if not isinstance(number, int):
            raise ValueError("Octal conversion only works with integers")
        return oct(number)[2:]  # Remove '0o' prefix

    def mean(self, numbers: List[Number]) -> float:
        """Calculate arithmetic mean of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate mean of empty list")
        return sum(numbers) / len(numbers)

    def std_dev(self, numbers: List[Number]) -> float:
        """Calculate standard deviation of a list of numbers."""
        if not numbers:
            raise ValueError("Cannot calculate standard deviation of empty list")
        mean = self.mean(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return math.sqrt(variance)

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    
    print("\n=== Advanced Calculator Demo ===\n")
    
    # Basic operations
    print("1. Basic Operations:")
    print(f"   5 + 3 = {calc.add(5, 3)}")
    print(f"   10 - 4 = {calc.subtract(10, 4)}")
    print(f"   6 × 7 = {calc.multiply(6, 7)}")
    print(f"   15 ÷ 3 = {calc.divide(15, 3)}")
    
    # Trigonometric functions
    print("\n2. Trigonometric Functions (in degrees):")
    calc.set_angle_mode(AngleMode.DEGREES)
    print(f"   sin(30°) = {calc.sin(30):.4f}")
    print(f"   cos(60°) = {calc.cos(60):.4f}")
    print(f"   tan(45°) = {calc.tan(45):.4f}")
    
    # Logarithmic functions
    print("\n3. Logarithmic Functions:")
    print(f"   log10(100) = {calc.log(100)}")
    print(f"   ln(e) = {calc.ln(math.e)}")
    print(f"   e^2 = {calc.exp(2):.4f}")
    
    # Constants
    print("\n4. Mathematical Constants:")
    print(f"   π = {calc.get_constant('pi')}")
    print(f"   e = {calc.get_constant('e')}")
    
    # Number base conversions
    print("\n5. Number Base Conversions:")
    print(f"   15 in binary = {calc.to_binary(15)}")
    print(f"   255 in hexadecimal = {calc.to_hex(255)}")
    print(f"   64 in octal = {calc.to_octal(64)}")
    
    # Statistical functions
    print("\n6. Statistical Functions:")
    numbers: List[Number] = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"   Numbers: {numbers}")
    print(f"   Mean = {calc.mean(numbers)}")
    print(f"   Standard Deviation = {calc.std_dev(numbers):.4f}")
    
    print("\n=== End of Demo ===\n") 