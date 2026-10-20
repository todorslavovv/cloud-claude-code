"""Chapter 11, Section 11.10: training a one-hidden-layer network with NumPy.

This file reproduces the listing printed in the notes; run it with
    python3 ch11_train_network.py
"""

import numpy as np

rng = np.random.default_rng(0)

# Data: class 1 inside the unit circle, class 0 in a ring around it.
n = 400
r = np.concatenate([rng.uniform(0, 1, n // 2),
                    rng.uniform(1.5, 2.5, n // 2)])
angle = rng.uniform(0, 2 * np.pi, n)
X = np.column_stack([r * np.cos(angle), r * np.sin(angle)])
y = np.concatenate([np.ones(n // 2), np.zeros(n // 2)])

# One hidden layer of 16 ReLU units and one output logit.
H = 16
W1 = rng.normal(0, np.sqrt(2 / 2), (H, 2))   # He initialisation
b1 = np.zeros(H)
w2 = rng.normal(0, np.sqrt(1 / H), H)
b2 = 0.0

lr = 0.5
for step in range(1, 501):
    # Forward pass for all examples at once (one row each).
    Z1 = X @ W1.T + b1              # pre-activations, n x H
    A1 = np.maximum(Z1, 0)          # ReLU
    z2 = A1 @ w2 + b2               # output logits, length n
    # Binary cross-entropy, computed stably from the logits.
    loss = np.mean(np.logaddexp(0, z2) - y * z2)

    # Backward pass.
    q = 1 / (1 + np.exp(-z2))       # predicted P(y = 1)
    d2 = (q - y) / n                # dL/dz2
    grad_w2 = A1.T @ d2
    grad_b2 = d2.sum()
    D1 = np.outer(d2, w2) * (Z1 > 0)    # dL/dZ1
    grad_W1 = D1.T @ X
    grad_b1 = D1.sum(axis=0)

    # Gradient descent step.
    W1 -= lr * grad_W1
    b1 -= lr * grad_b1
    w2 -= lr * grad_w2
    b2 -= lr * grad_b2

    if step in (1, 10, 50, 100, 500):
        accuracy = np.mean((z2 > 0) == y)
        print(f"step {step:3d}  loss {loss:.3f}  accuracy {accuracy:.3f}")
