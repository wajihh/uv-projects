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
