import numpy as np
import matplotlib.pyplot as plt

# given function
fn = (lambda x: -0.1*(x**4)- 0.5*(x**2)-0.5*x+1.2)

# initial values
x0 = 0.5
h = 1
f_dash = -1.05  # f'(0.5)

# arrays to store data
H = np.array([])
fwd_Df = np.array([])
fwd_E  = np.array([])
bkd_Df = np.array([])
bkd_E  = np.array([])
ctr_Df = np.array([])
ctr_E  = np.array([])

# loop to calculate approximations and errors
while(h>= 1/2**15):

    # forrward difference approximation calculations
    df      = (fn(x0+h)-fn(x0))/h
    e       = abs(f_dash-df)
    fwd_Df  = np.append(fwd_Df, df)
    fwd_E   = np.append(fwd_E,e)

    # backward difference approximations calculations
    df      = (fn(x0)-fn(x0-h))/h
    e       = abs(f_dash-df)
    bkd_Df  = np.append(bkd_Df, df)
    bkd_E   = np.append(bkd_E,e)

    # centered difference approximations calculations
    df      = (fn(x0+h)-fn(x0-h))/(2*h)
    e       = abs(f_dash-df)
    ctr_Df  = np.append(ctr_Df, df)
    ctr_E   = np.append(ctr_E,e)
    #print("%.10f" %e) ---> for tabluation purpose
    # printing values in above way

    H       = np.append(H,h)
    h       = h/2

# printing plots
plt.plot(H,fwd_E, marker=".", ms =5, color="red")
plt.plot(H,bkd_E, marker=".", ms =5, color="green")
plt.plot(H,ctr_E, marker=".", ms =5, color="black")
plt.title("Error vs Step size")
plt.legend(["Foraward Approximation","Backward Approximation", "Centered Approximation"])
plt.xlabel("Step size (h)")
plt.ylabel("Absolute error")
plt.xscale("log")
plt.yscale("log")
plt.grid()
plt.show()

