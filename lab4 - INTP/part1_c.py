import numpy as np
import matplotlib.pyplot as plt

# importing previously written lagrange function
from part1_b import *

# actual function
f = (lambda x : 1/(1+25*(x**2)))

# Generate a data set in the range −1 ≤ 𝑥 ≤ 1 with an equal spacing of 0.1.
x = np.arange(-1, 1.1, 0.1)

# generating corresponding y values
y = f(x)

print("Generated x values")
print(x)
print("Generated y values")
print(y)

# Generate a set of 𝑥 values in [−1, 1] with a spacing of 0.01
new_x = np.arange(-1.0,1.01,0.01)
# print(new_x)

# finding corresponding 𝑦 values using lagrange method
fx = lagrange(list(x), list(y), new_x)

# finding corresponding y values using actual function
y = f(new_x)

# plotting actual value vs interpoleted value
plt.plot(new_x,y, 'g-') # actual curve
plt.plot(new_x,fx,'b-') # interpolated curve
plt.title("Plots Actual vs Lagrange interpolated")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Actual", "Interpolated"])
plt.grid()
plt.show()

# calculating absolute error
e = abs(y - fx)

# plotting error vs x
plt.plot(new_x,e,'r-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()
