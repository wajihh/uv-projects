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
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
.env
.venv
env/
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Misc
.DS_Store
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
git clone https://github.com/wajihh/uv-projects.git
cd uv-projects/calculator
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
import math

# Create calculator instance
calc = Calculator()

# Basic Operations
result = calc.add(5, 3)        # 8
result = calc.subtract(10, 4)  # 6
result = calc.multiply(6, 7)   # 42
result = calc.divide(15, 3)    # 5.0
result = calc.power(2, 3)      # 8
result = calc.square_root(16)  # 4.0
result = calc.percentage(200, 15)  # 30.0

# Trigonometric Functions (default in degrees)
calc.set_angle_mode(AngleMode.DEGREES)
sin_30 = calc.sin(30)          # 0.5
cos_60 = calc.cos(60)          # 0.5
tan_45 = calc.tan(45)          # 1.0
asin_val = calc.asin(0.5)      # 30.0
acos_val = calc.acos(0.5)      # 60.0
atan_val = calc.atan(1.0)      # 45.0

# Switch to radians if needed
calc.set_angle_mode(AngleMode.RADIANS)
sin_pi_6 = calc.sin(math.pi/6)  # 0.5
cos_pi_3 = calc.cos(math.pi/3)  # 0.5
tan_pi_4 = calc.tan(math.pi/4)  # 1.0

# Logarithms and Exponentials
log_100 = calc.log(100)         # 2.0 (base 10)
log2_8 = calc.log(8, 2)         # 3.0 (base 2)
ln_e = calc.ln(math.e)          # 1.0
exp_2 = calc.exp(2)             # 7.3891

# Constants
pi = calc.get_constant('pi')    # 3.141592653589793
e = calc.get_constant('e')      # 2.718281828459045
tau = calc.get_constant('tau')  # 6.283185307179586

# Number Base Conversions
binary = calc.to_binary(15)     # "1111"
hexa = calc.to_hex(255)         # "ff"
octal = calc.to_octal(64)       # "100"

# Statistical Functions
numbers = [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0]
mean = calc.mean(numbers)        # 5.0
std_dev = calc.std_dev(numbers) # 2.0

# Memory Operations
calc.memory_store(10)           # Store 10
value = calc.memory_recall()    # Get 10
calc.memory_add(5)             # Add 5 to memory
value = calc.memory_recall()    # Get 15
calc.memory_clear()            # Reset to 0
```

### Error Handling

The calculator includes robust error handling for common mathematical errors:
```python
# Division by zero
try:
    calc.divide(1, 0)
except ValueError as e:
    print(e)  # "Cannot divide by zero"

# Negative square root
try:
    calc.square_root(-1)
except ValueError as e:
    print(e)  # "Cannot calculate square root of negative number"

# Non-integer base conversion
try:
    calc.to_binary(3.14)
except ValueError as e:
    print(e)  # "Binary conversion only works with integers"
```

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## License

[Add your license information here]
