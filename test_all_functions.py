from src.calc.calculator import Calculator, AngleMode
import math

def run_calculator_demo():
    calc = Calculator()
    
    def print_section(title):
        print(f"\n{'='*20} {title} {'='*20}")
    
    print("\n🧮 ADVANCED CALCULATOR - COMPLETE FUNCTION DEMO 🧮\n")
    
    # 1. Basic Operations
    print_section("Basic Operations")
    print(f"Addition: 15 + 7 = {calc.add(15, 7)}")
    print(f"Subtraction: 20 - 8 = {calc.subtract(20, 8)}")
    print(f"Multiplication: 6 × 8 = {calc.multiply(6, 8)}")
    print(f"Division: 45 ÷ 5 = {calc.divide(45, 5)}")
    print(f"Power: 2³ = {calc.power(2, 3)}")
    print(f"Square Root: √16 = {calc.square_root(16)}")
    print(f"Percentage: 15% of 200 = {calc.percentage(200, 15)}")
    
    # 2. Trigonometric Functions
    print_section("Trigonometric Functions")
    print("In Degrees:")
    calc.set_angle_mode(AngleMode.DEGREES)
    print(f"sin(30°) = {calc.sin(30):.4f}")
    print(f"cos(60°) = {calc.cos(60):.4f}")
    print(f"tan(45°) = {calc.tan(45):.4f}")
    print(f"arcsin(0.5) = {calc.asin(0.5):.4f}°")
    print(f"arccos(0.5) = {calc.acos(0.5):.4f}°")
    print(f"arctan(1.0) = {calc.atan(1.0):.4f}°")
    
    print("\nIn Radians:")
    calc.set_angle_mode(AngleMode.RADIANS)
    print(f"sin(π/6) = {calc.sin(math.pi/6):.4f}")
    print(f"cos(π/3) = {calc.cos(math.pi/3):.4f}")
    print(f"tan(π/4) = {calc.tan(math.pi/4):.4f}")
    
    # 3. Logarithmic and Exponential Functions
    print_section("Logarithmic and Exponential Functions")
    print(f"log₁₀(100) = {calc.log(100)}")
    print(f"log₂(8) = {calc.log(8, 2)}")
    print(f"ln(e) = {calc.ln(math.e)}")
    print(f"e² = {calc.exp(2):.4f}")
    
    # 4. Constants
    print_section("Mathematical Constants")
    print(f"π = {calc.get_constant('pi')}")
    print(f"e = {calc.get_constant('e')}")
    print(f"τ = {calc.get_constant('tau')}")
    print(f"∞ = {calc.get_constant('inf')}")
    
    # 5. Number Base Conversions
    print_section("Number Base Conversions")
    decimal = 255
    print(f"Decimal number: {decimal}")
    print(f"In binary: {calc.to_binary(decimal)}")
    print(f"In hexadecimal: {calc.to_hex(decimal)}")
    print(f"In octal: {calc.to_octal(decimal)}")
    
    # 6. Statistical Functions
    print_section("Statistical Functions")
    dataset = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
    print(f"Dataset: {dataset}")
    print(f"Mean = {calc.mean(dataset):.2f}")
    print(f"Standard Deviation = {calc.std_dev(dataset):.4f}")
    
    # 7. Memory Operations
    print_section("Memory Operations")
    calc.memory_store(10)
    print(f"Stored in memory: 10")
    print(f"Memory recall: {calc.memory_recall()}")
    calc.memory_add(5)
    print(f"Added 5 to memory")
    print(f"New memory value: {calc.memory_recall()}")
    calc.memory_clear()
    print(f"Memory cleared. Current value: {calc.memory_recall()}")
    
    # 8. Error Handling Demonstration
    print_section("Error Handling Examples")
    try:
        calc.divide(1, 0)
    except ValueError as e:
        print(f"Division by zero: {e}")
    
    try:
        calc.square_root(-1)
    except ValueError as e:
        print(f"Negative square root: {e}")
    
    try:
        calc.to_binary(3.14)
    except ValueError as e:
        print(f"Non-integer base conversion: {e}")
    
    print("\n🧮 END OF CALCULATOR DEMO 🧮\n")

if __name__ == "__main__":
    run_calculator_demo() 