import math

# Define the function
def f(x):
    return math.exp(-x) - x

# Define the derivative of the function
def f_prime(x):
    return -math.exp(-x) - 1

# Newton-Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            print("Zero derivative. No solution found.")
            return None
        x_new = x - fx / fpx
        print(f"Iteration {i+1}: x = {x_new:.6f}, f(x) = {f(x_new):.6f}")
        if abs(x_new - x) < tol:
            print(f"Converged to root: {x_new:.6f} after {i+1} iterations.")
            return x_new
        x = x_new
    print("Maximum iterations reached without convergence.")
    return None

# Example usage:
initial_guess = 0.5
root = newton_raphson(initial_guess)
import numpy as np
import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return np.exp(-x) - x

def f_prime(x):
    return -np.exp(-x) - 1

# Newton-Raphson method with plotting
def newton_raphson_plot(x0, tol=1e-6, max_iter=10):
    x = x0
    x_vals = np.linspace(0, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=r'$f(x) = e^{-x} - x$', color='blue')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Newton-Raphson Method for $f(x) = e^{-x} - x$')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if fpx == 0:
            print("Zero derivative. No solution found.")
            break
        x_new = x - fx / fpx
        # Plot the tangent line
        tangent_x = np.linspace(x - 0.5, x + 0.5, 10)
        tangent_y = fx + fpx * (tangent_x - x)
        plt.plot(tangent_x, tangent_y, 'r--', label='Tangent' if i == 0 else "")
        plt.plot(x, fx, 'ko')  # Current point
        if abs(x_new - x) < tol:
            print(f"Converged to root: {x_new:.6f} after {i+1} iterations.")
            break
        x = x_new

    plt.legend()
    plt.show()

# Example usage:
initial_guess = 0.5
newton_raphson_plot(initial_guess)
