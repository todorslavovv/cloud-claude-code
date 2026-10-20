"""Chapter 11, Section 11.8: a minimal reverse-mode automatic differentiation engine.

This file reproduces the listing printed in the notes; run it with
    python3 ch11_autodiff.py
"""

import math

class Value:
    """A number that remembers how it was computed."""

    def __init__(self, data, parents=(), local_grads=()):
        self.data = data                # value from the forward pass
        self.grad = 0.0                 # d(output)/d(self)
        self.parents = parents          # Values it was computed from
        self.local_grads = local_grads  # d(self)/d(parent) for each

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data + other.data, (self, other), (1.0, 1.0))

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        return Value(self.data * other.data, (self, other),
                     (other.data, self.data))

    def relu(self):
        return Value(max(self.data, 0.0), (self,),
                     (1.0 if self.data > 0 else 0.0,))

    def backward(self):
        # List the nodes so that each comes after its parents.
        order, seen = [], set()
        def visit(v):
            if id(v) not in seen:
                seen.add(id(v))
                for p in v.parents:
                    visit(p)
                order.append(v)
        visit(self)
        # Chain rule, from the output back towards the inputs.
        self.grad = 1.0
        for v in reversed(order):
            for p, g in zip(v.parents, v.local_grads):
                p.grad += v.grad * g

x, y = Value(2.0), Value(3.0)
f = (x + y) * (y + 1)
f.backward()
print(f.data, x.grad, y.grad)    # 20.0 4.0 9.0
