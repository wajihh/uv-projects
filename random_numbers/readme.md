I'll optimize the code by separating the two plots into a single figure with two subplots, which is a more efficient way to display multiple plots. I'll also improve the code organization and readability.


```python:random_numbers/main.py
import random
import numpy as np
import matplotlib.pyplot as plt

# Generate and print 10 random numbers between 1 and 100
for _ in range(10):
    number = random.randint(1, 100)
    print(number, end=' ')
print()  # Print a newline at the end

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# First subplot: Standard Normal Distribution
x = np.linspace(-4, 4, 100)
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

ax1.plot(x, y)
ax1.set_title('Standard Normal Distribution')
ax1.set_xlabel('x')
ax1.set_ylabel('Probability Density')
ax1.grid(True)

# Second subplot: Histogram of random numbers
data = np.random.normal(0, 1, 500)
ax2.hist(data, bins=30, density=True, alpha=0.7, color='skyblue')
ax2.plot(x, y, 'r-', lw=2, label='PDF')
ax2.set_title('Histogram of 500 Random Numbers\nNormal Distribution')
ax2.set_xlabel('Value')
ax2.set_ylabel('Density')
ax2.grid(True)
ax2.legend()

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
```
I've optimized the code in several ways:

1. **Combined the plots into a single figure with two subplots** - Instead of creating two separate figures, I've used `plt.subplots()` to create a single figure with two side-by-side subplots. This is more efficient and provides a better visual comparison.

2. **Improved code organization** - I moved the imports to the top of the file for better readability and organization.

3. **Used object-oriented plotting** - Instead of using the pyplot interface (`plt.plot()`, etc.), I'm now using the object-oriented interface with `ax1` and `ax2` objects. This gives more control and is generally considered a better practice.

4. **Added proper layout management** - I added `plt.tight_layout()` to automatically adjust the spacing between subplots, preventing any overlap.

5. **Optimized figure size** - I set a more appropriate figure size (15x6) for the side-by-side layout.

The code now displays both the standard normal distribution curve and the histogram of random numbers in a single figure, making it easier to compare them. The random number generation at the beginning of the file is preserved as it was.
