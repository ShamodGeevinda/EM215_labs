import numpy as np
import matplotlib.pyplot as plt

# given function
fn = (lambda x: -0.1*(x**4)- 0.5*(x**2)-0.5*x+1.2)

# initial values
x0 = 0.5
h =1
f_2dash = -1.3

# arrays to store calculateda values
H      = np.array([])
ctr_Df = np.array([])
ctr_E  = np.array([])

# loop to calculate centered difference approximations
while(h>= 1/2**17):
    df      = (fn(x0+h)-2*fn(x0)+fn(x0-h))/h**2
    e       = abs(f_2dash-df)
    ctr_Df  = np.append(ctr_Df, df)
    ctr_E   = np.append(ctr_E,e)
    H       = np.append(H,h)
    h       = h/2


# plotting the graphs
plt.plot(H, ctr_E, marker=".", ms =5, color="green")
plt.title("Error vs Step size")
plt.legend(["Centered Approximation"])
plt.xlabel("Step size (h)")
plt.ylabel("Absolute error")
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()

