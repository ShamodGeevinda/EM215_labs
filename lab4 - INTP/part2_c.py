# Newton's Divided Difference Method
import numpy as np
import matplotlib.pyplot as plt

# importing previous module which can manupulate Divided difference data
from part2_a import * 
from part2_b import *

# 20 x values between -10 and +10
new_x = np.linspace(-10, 10, 20)

# corresponding 20 y values
new_y = np.exp(-1*(new_x**2))
x = np.arange(-10, 10.05, 0.05)

# interpoleted values
y = compute_y(new_x, new_y, x)
# actual values
y1 = np.exp(-1*(x**2))

# ploting actual curve and interpoleted curve
plt.plot(x,y1, 'b-') # actual curve
plt.plot(x,y,'r-') # interpolated curve
plt.title("Plots Actual vs Divided difference method interpolated")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Actual", "Interpolated"])
plt.grid()
plt.show()

# calculating absolute approximation error
e = abs(y1 - y)

# plotting Approximation error vs x
plt.plot(x,e,'g-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()
