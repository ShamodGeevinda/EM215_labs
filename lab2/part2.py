import numpy as np
import matplotlib.pyplot as plt

# functions
f1x = np.linspace(0.1,15,2000)
f2x = 4 * np.log(f1x)
f2_dashx = 4/ f1x 

# printing graphs
plt.plot(f1x, f1x , color = "green")
plt.plot(f1x, f2x, color = "black")
plt.plot(f1x, f2_dashx, color = "red")
plt.legend(["x","4log(x)","4/x"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphs of x, 4log(x), 4/x")
plt.grid()
plt.show()