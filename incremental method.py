import math

def f(x):
    return math.exp(-x) - x

def incremental_search(f, x_start, x_end, step):
    x = x_start
    while x < x_end:
        f_x = f(x)
        f_x_next = f(x + step)
        if f_x * f_x_next < 0:
            print(f"Sign change detected between x = {x} and x = {x + step}")
            print(f"Approximate root at x = {(x + x + step) / 2}")
        x += step

# Example usage:
incremental_search(f, 0, 1, 0.01)
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x) - x

# Incremental search parameters
x_start = 0
x_end = 1
step = 0.01

# Generate x values for plotting
x_vals = np.linspace(x_start, x_end, 500)
y_vals = f(x_vals)

# Initialize list to store intervals where sign change occurs
sign_change_intervals = []

# Perform incremental search to find sign changes
x = x_start
while x < x_end:
    f_x = f(x)
    f_x_next = f(x + step)
    if f_x * f_x_next < 0:
        sign_change_intervals.append((x, x + step))
    x += step

# Plot the function
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis

# Highlight intervals with sign changes
for interval in sign_change_intervals:
    x_mid = (interval[0] + interval[1]) / 2
    plt.plot(x_mid, f(x_mid), 'ro')  # Mark approximate root

# Add labels and legend
plt.title('Graph of $f(x) = e^{-x} - x$ with Incremental Search')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
