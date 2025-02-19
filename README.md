# Advanced Scientific Calculator

A powerful Python-based scientific calculator with support for basic arithmetic, trigonometry, logarithms, statistics, and number base conversions.

## Features

- Basic arithmetic operations (add, subtract, multiply, divide)
- Trigonometric functions (sin, cos, tan, and their inverses)
- Logarithmic and exponential functions
- Mathematical constants (π, e, etc.)
- Number base conversions (binary, hexadecimal, octal)
- Statistical functions (mean, standard deviation)
- Memory functions
- Angle mode switching (degrees/radians)

## GitHub Repository Setup

This project is hosted on GitHub. Here's how it was set up:

1. **Initialize Git Repository**
```bash
# Initialize git in the project directory
git init
```

2. **Create .gitignore**
Created a `.gitignore` file with Python-specific exclusions:
```bash
# Python
__pycache__/
*.py[cod]
*$py.class
build/
dist/
*.egg-info/

# Virtual Environment
.env
.venv
env/
venv/

# IDE
.idea/
.vscode/
```

3. **Add and Commit Files**
```bash
# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: Advanced Scientific Calculator"
```

4. **Create and Switch to Feature Branch**
```bash
# Create and switch to new branch
git checkout -b calculator
```

5. **Connect to Remote Repository**
```bash
# Add remote repository
git remote add origin https://github.com/wajihh/uv-projects.git

# Push to GitHub
git push -u origin calculator
```

6. **Create Pull Request**
- Visit: https://github.com/wajihh/uv-projects/pull/new/calculator
- Create pull request to merge calculator branch into main

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd calc
```

2. Create and activate a virtual environment using `uv`:
```bash
uv venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage

### Running the Demo

To see all available functions in action, run:
```bash
python src/calc/calculator.py
```

### Interactive Usage

You can use the calculator interactively in Python:

```python
from calc.src.calc.calculator import Calculator, AngleMode

# Create calculator instance
calc = Calculator()

# Basic Operations
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0

# Trigonometric Functions (default in degrees)
calc.set_angle_mode(AngleMode.DEGREES)
sin_30 = calc.sin(30)          # 0.5
cos_60 = calc.cos(60)          # 0.5
tan_45 = calc.tan(45)          # 1.0

# Switch to radians if needed
calc.set_angle_mode(AngleMode.RADIANS)
sin_pi_6 = calc.sin(math.pi/6)  # 0.5

# Logarithms and Exponentials
log_100 = calc.log(100)         # 2.0 (base 10)
ln_e = calc.ln(math.e)          # 1.0
exp_2 = calc.exp(2)             # 7.3891

# Constants
pi = calc.get_constant('pi')    # 3.141592653589793
e = calc.get_constant('e')      # 2.718281828459045

# Number Base Conversions
binary = calc.to_binary(15)     # "1111"
hexa = calc.to_hex(255)         # "ff"
octal = calc.to_octal(64)       # "100"

# Statistical Functions
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
mean = calc.mean(numbers)        # 3.0
std_dev = calc.std_dev(numbers) # 1.4142

# Memory Operations
calc.memory_store(5)            # Store 5 in memory
value = calc.memory_recall()    # Get value from memory (5)
calc.memory_add(3)              # Add 3 to memory (now 8)
calc.memory_clear()             # Clear memory (0)
```

### Available Functions

#### Basic Operations
- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract b from a
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide a by b
- `power(base, exponent)`: Calculate base raised to exponent
- `square_root(number)`: Calculate square root
- `percentage(number, percent)`: Calculate percentage of a number

#### Trigonometric Functions
- `sin(angle)`: Sine of angle
- `cos(angle)`: Cosine of angle
- `tan(angle)`: Tangent of angle
- `asin(value)`: Inverse sine (arcsin)
- `acos(value)`: Inverse cosine (arccos)
- `atan(value)`: Inverse tangent (arctan)

#### Logarithmic Functions
- `log(number, base=10)`: Logarithm with specified base
- `ln(number)`: Natural logarithm
- `exp(number)`: e raised to the power of number

#### Number Base Conversions
- `to_binary(number)`: Convert decimal to binary
- `to_hex(number)`: Convert decimal to hexadecimal
- `to_octal(number)`: Convert decimal to octal

#### Statistical Functions
- `mean(numbers)`: Calculate arithmetic mean
- `std_dev(numbers)`: Calculate standard deviation

#### Memory Operations
- `memory_store(value)`: Store value in memory
- `memory_recall()`: Recall value from memory
- `memory_clear()`: Clear memory
- `memory_add(value)`: Add value to memory

#### Constants
- Access constants using `get_constant(name)`:
  - 'pi': π (3.141592653589793)
  - 'e': e (2.718281828459045)
  - 'tau': τ (2π)
  - 'inf': infinity

## Error Handling

The calculator includes robust error handling for common mathematical errors:
- Division by zero
- Invalid input types
- Negative numbers in square root
- Empty lists in statistical functions
- Invalid angle values
- Non-integer values in base conversions

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## License

[Add your license information here]
