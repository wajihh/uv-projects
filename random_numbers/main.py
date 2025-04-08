import random

# Generate and print 10 random numbers between 1 and 100
for _ in range(10):
    number = random.randint(1, 100)
    print(number, end=' ')
print()  # Print a newline at the end
import numpy as np
import matplotlib.pyplot as plt

# Generate points for x-axis
x = np.linspace(-4, 4, 100)

# Calculate standard normal distribution
y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.title('Standard Normal Distribution')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
