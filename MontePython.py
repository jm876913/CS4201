import random as r
import math as m

# Number of darts that land inside.
inside = 0
inside2 = 0
inside3 = 0
inside4 = 0
inside5 = 0
inside6 = 0
inside7 = 0
inside8 = 0
inside9 = 0
# Total number of darts to throw.
total = 10000000

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
# ab = abs(pi - expected)
# error = float(ab / expected) * 100
# print("First experimental percent error")
# print(error)

for j in range(0, total):
  # Generate random x, y in [0, 1].
  n2 = r.random()**2
  o2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(n2 + o2) < 1.0:
    inside2 += 1

pi2 = (float(inside2) / total) * 4
print("Second experimental pi value")
print(pi2)

# ab2 = abs(pi2 - expected)
# error = float(ab2 / expected) * 100
# print("Second experimental value percent error")
# print(error)



for k in range(0, total):
  # Generate random x, y in [0, 1].
  z2 = r.random()**2
  v2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(z2 + v2) < 1.0:
    inside3 += 1

pi3 = (float(inside3) / total) * 4
print("third experimental pi value")
print(pi3)

# ab2 = abs(pi2 - expected)
# error = float(ab2 / expected) * 100
# print("third experimental value percent error")
# print(error)



for l in range(0, total):
  # Generate random x, y in [0, 1].
  a2 = r.random()**2
  b2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(a2 + b2) < 1.0:
    inside4 += 1
pi4 = (float(inside4) / total) * 4

for n in range(0, total):
  # Generate random x, y in [0, 1].
  c2 = r.random()**2
  d2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(c2 + d2) < 1.0:
    inside5 += 1
pi5 = (float(inside5) / total) * 4

for o in range(0, total):
  # Generate random x, y in [0, 1].
  e2 = r.random()**2
  f2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(e2 + f2) < 1.0:
    inside6 += 1
pi6 = (float(inside6) / total) * 4

for p in range(0, total):
  # Generate random x, y in [0, 1].
  g2 = r.random()**2
  h2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(g2 + h2) < 1.0:
    inside7 += 1
pi7 = (float(inside7) / total) * 4

for q in range(0, total):
  # Generate random x, y in [0, 1].
  ii2 = r.random()**2
  jj2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(ii2 + jj2) < 1.0:
    inside8 += 1
pi8 = (float(inside8) / total) * 4

for s in range(0, total):
  # Generate random x, y in [0, 1].
  kk2 = r.random()**2
  ll2 = r.random()**2
    # Increment if inside unit circle.
  if m.sqrt(kk2 + ll2) < 1.0:
    inside9 += 1
pi9 = (float(inside9) / total) * 4

print("average experimental value from all simulations")
avg = float((pi + pi2 + pi3 + pi4 + pi5 + pi6 + pi7 + pi8 + pi9)/9)
print(avg)

abavg = abs(avg - expected)
error = float(abavg / expected) * 100
print("average experimental value percent error")
print(error)

print("The percent difference between the two experimental values")
upper = abs(pi - avg)
lower = (float(pi + avg))/2
diff = (upper/lower)*100
print(diff)    

