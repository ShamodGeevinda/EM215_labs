import numpy as np

#Interpolates the value of the function at x=alpha
#using Lagrange Interpolation on the two input vectors X and Y
def lagrange(X, Y, alpha):
    
    #   returns the f(a) value for given x = a and coordinate set(xi, yi)
    #   X = [x1, x2, x3, x4,...., xn]
    #   Y = [y1, y2, y3, y4,...., yn]
    
    #Initialize f(a) value
    fa = 0;
    
    for i in range(len(X)):

        #Calculate Li(x) for current term
        Li = 1
        for j in range(len(X)):
            if j != i:
                Li *= (alpha - X[j])/(X[i] - X[j])

        #Add current term to polynomial
        fa += Li * Y[i]

    #Finally return value of f(a)
    return fa


