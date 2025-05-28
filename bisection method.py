import math

def f(x):
    return math.exp(-x) - x

def bisection_method(xl, xu, tol=1e-6, max_iter=100):
    if f(xl) * f(xu) >= 0:
        print("The function must change sign over the interval.")
        return None

    for iteration in range(1, max_iter + 1):
        xr = (xl + xu) / 2
        f_xr = f(xr)
        f_xl = f(xl)

        print(f"Iteration {iteration}: xl = {xl:.6f}, xu = {xu:.6f}, xr = {xr:.6f}, f(xr) = {f_xr:.6f}")

        if abs(f_xr) < tol:
            print(f"Converged to root: {xr:.6f} after {iteration} iterations.")
            return xr

        if f_xl * f_xr < 0:
            xu = xr
        else:
            xl = xr

    print("Maximum iterations reached without convergence.")
    return None

# Example usage:
root = bisection_method(0, 1)
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(0, 1, 400)
y_vals = np.exp(-x_vals) - x_vals

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=r'$f(x)=e^{-x }- x$', color='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.title('Graph of $f(x) = e^{-x} - x$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
