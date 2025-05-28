import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the quadratic equation: ax^2 + bx + c
a = 1
b = -3
c = 2

# Define the quadratic function
def quadratic(x):
    return a*x**2 + b*x + c

# Generate x values
x = np.linspace(-10, 10, 400)
y = quadratic(x)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis

# Highlight roots using the quadratic formula (for visualization)
discriminant = b**2 - 4*a*c
if discriminant >= 0:
    root1 = (-b + np.sqrt(discriminant)) / (2*a)
    root2 = (-b - np.sqrt(discriminant)) / (2*a)
    plt.plot(root1, 0, 'ro', label='Root 1')
    plt.plot(root2, 0, 'go', label='Root 2')

# Add labels and grid
plt.title('Graphical Solution of a Quadratic Equation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
