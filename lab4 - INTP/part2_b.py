# Newton's Divided Difference Method
import numpy as np
import matplotlib.pyplot as plt

# importing previous module which can manupulate Divided difference data
from part2_a import * 

def compute_y(X, Y, x):
    
        # from ith values from X, Y will be used to find the DD table 
        # and then coefficients will be picked from table
        # Using the coefficients y will be calculated for given x
    
    table = nddiff(X, Y)
    # coefficient list
    coef = []
    for n in range(1,len(table)):
        #add data to coefficient list
        coef.append(table[n][0])

    # printtable(table)
    y = 0
    for p in range(len(coef)):
        t = coef[p]
        for j in range(p):
            t = t * (x - list(X)[j])
        y += t
    return y

