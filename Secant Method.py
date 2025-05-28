import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x) - x

# Secant Method implementation with plotting
def secant_method_plot(x0, x1, tol=1e-6, max_iter=100):
    x_vals = np.linspace(0, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Secant Method for $f(x) = e^{-x} - x$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Zero denominator encountered; division by zero.")
            break
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_x2 = f(x2)

        # Plot the secant line
        plt.plot([x0, x1], [f_x0, f_x1], 'r--', label='Secant Line' if i == 0 else "")
        plt.plot(x2, f_x2, 'ko')  # Current approximation

        print(f"Iteration {i+1}: x = {x2:.6f}, f(x) = {f_x2:.6f}")

        if abs(f_x2) < tol:
            print(f"Converged to root: {x2:.6f} after {i+1} iterations.")
            break

        x0, x1 = x1, x2

    plt.legend()
    plt.show()

# Example usage:
initial_guess_0 = 0.0
initial_guess_1 = 1.0
secant_method_plot(initial_guess_0, initial_guess_1)
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x) - x

# Secant Method implementation with plotting
def secant_method_plot(x0, x1, tol=1e-6, max_iter=10):
    x_vals = np.linspace(0, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Secant Method for $f(x) = e^{-x} - x$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Zero denominator encountered; division by zero.")
            break
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_x2 = f(x2)

        # Plot the secant line
        plt.plot([x0, x1], [f_x0, f_x1], 'r--', label='Secant Line' if i == 0 else "")
        plt.plot(x2, f_x2, 'ko')  # Current approximation

        print(f"Iteration {i+1}: x = {x2:.6f}, f(x) = {f_x2:.6f}")

        if abs(f_x2) < tol:
            print(f"Converged to root: {x2:.6f} after {i+1} iterations.")
            break

        x0, x1 = x1, x2

    plt.legend()
    plt.show()

# Example usage:
initial_guess_0 = 0.0
initial_guess_1 = 1.0
secant_method_plot(initial_guess_0, initial_guess_1)
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x) - x

# Secant Method implementation with plotting
def secant_method_plot(x0, x1, tol=1e-6, max_iter=10):
    x_vals = np.linspace(0, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Secant Method for $f(x) = e^{-x} - x$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Zero denominator encountered; division by zero.")
            break
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_x2 = f(x2)

        # Plot the secant line
        plt.plot([x0, x1], [f_x0, f_x1], 'r--', label='Secant Line' if i == 0 else "")
        plt.plot(x2, f_x2, 'ko')  # Current approximation

        print(f"Iteration {i+1}: x = {x2:.6f}, f(x) = {f_x2:.6f}")

        if abs(f_x2) < tol:
            print(f"Converged to root: {x2:.6f} after {i+1} iterations.")
            break

        x0, x1 = x1, x2

    plt.legend()
    plt.show()

# Example usage:
initial_guess_0 = 0.0
initial_guess_1 = 1.0
secant_method_plot(initial_guess_0, initial_guess_1)
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.exp(-x) - x

# Secant Method implementation with plotting
def secant_method_plot(x0, x1, tol=1e-6, max_iter=10):
    x_vals = np.linspace(0, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Secant Method for $f(x) = e^{-x} - x$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if f_x1 - f_x0 == 0:
            print("Zero denominator encountered; division by zero.")
            break
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        f_x2 = f(x2)

        # Plot the secant line
        plt.plot([x0, x1], [f_x0, f_x1], 'r--', label='Secant Line' if i == 0 else "")
        plt.plot(x2, f_x2, 'ko')  # Current approximation

        print(f"Iteration {i+1}: x = {x2:.6f}, f(x) = {f_x2:.6f}")

        if abs(f_x2) < tol:
            print(f"Converged to root: {x2:.6f} after {i+1} iterations.")
            break

        x0, x1 = x1, x2

    plt.legend()
    plt.show()

# Example usage:
initial_guess_0 = 0.0
initial_guess_1 = 1.0
secant_method_plot(initial_guess_0, initial_guess_1)
# 