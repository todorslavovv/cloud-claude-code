"""Chapter 8, Section 8.3: gradient descent for linear regression.

This file reproduces the listing printed in the notes; run it with
    python3 ch08_gradient_descent.py
"""

import numpy as np

X = np.array([[1, 1], [2, 1], [3, 1]], dtype=float)  # x and ones
y = np.array([2, 3, 5], dtype=float)
theta = np.zeros(2)                  # parameters (w, b)
eta = 0.05                           # learning rate

for step in range(500):
    residuals = y - X @ theta
    grad = -2 / len(y) * X.T @ residuals   # gradient of the MSE
    theta = theta - eta * grad             # gradient descent update

print(theta)                         # approximately [1.5, 0.333]
