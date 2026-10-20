"""Chapter 4, Section 4.11: solving a linear system with NumPy.

This file reproduces the listing printed in the notes; run it with
    python3 ch04_linear_system.py
"""

import numpy as np

A = np.array([[2, 1],
              [-1, 3],
              [0, 4]])         # a 3 x 2 matrix
x = np.array([3, 2])           # a vector in R^2
print(A @ x)                   # [8 3 8]
print(A.T)                     # the 2 x 3 transpose

B = np.array([[1, 2],
              [3, 4]])
print(np.linalg.det(B))        # -2.0 (up to rounding)
print(np.linalg.solve(B, np.array([5, 6])))   # [-4.   4.5]
