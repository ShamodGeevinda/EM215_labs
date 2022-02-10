import numpy as np
import matplotlib.pyplot as plt

# actual function
f = (lambda x : 1 + 10*x)

# Derived Polynomial
def F(C,x):
    res = 0
    for i in range(len(C)):
        # print(C[i][0], x**i)
        res += C[i][0] * (x**i)
    return res

# generating equally divided x values.
x = np.linspace(0.1,0.2,11)

# calling functions and generating corresponding values
y = f(x) 

# print(x)
# print(y)

matrix = [] 
b = []

# Using Direct Method
# Generate A, b -------------------> A.x = b format
for i in range(len(x)):
    row = []
    b_row = []
    for j in range(len(x)):
        row.append(list(x)[i]**j)
    matrix.append(row)
    b.append([list(y)[i]])

A = np.array(matrix) # coefficient matrix
b = np.array(b)      # matrix b

# inverse of A
invA = np.linalg.inv(A)

# getting dot product of the functions
coef = np.dot(invA,b)
print(coef)
f = F(coef, x)
# print(f)

# Plot both the curves and the error
plt.plot(x,y, 'b')
plt.plot(x,f,'r.')
plt.title("Original and Derived Equation Plot")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Original", "Derived"])
plt.grid()
plt.show()

# calculating the absolute error
err = abs(y - f)

# plotting error
plt.plot(x,err,'g-')
plt.title("Approximation Error abs(e) vs x")
plt.xlabel("x")
plt.ylabel("abs(e)")
plt.grid()
plt.show()