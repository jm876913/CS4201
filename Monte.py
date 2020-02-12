import random as r
import math as m

inside = 0

total = 100000000
limit = 10

# Iterate for the number of darts.
for i in range(0, total):
# Generate random x, y in [0, 1].
    x2 = r.random()**2
    y2 = r.random()**2
        # Increment if inside unit circle.
    if m.sqrt(x2 + y2) < 1.0:
        inside += 1

# inside / total = pi / 4
pi = (float(inside) / total) * 4

# It works!
print("First experimental pi value")
print(pi)
expected = 3.141592
ab = abs(pi - expected)
error = float(ab / expected) * 100
print("First experimental percent error")
print(error)