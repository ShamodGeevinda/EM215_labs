import math as m

# Defining equations to be solved
# in diagonally dominant form
f1 = lambda x1 ,x2, x3, x4    : (2.1+x2-x3-x4)/15
f2 = lambda x1 ,x2, x3, x4    : (6.7-5*x1-3*x3-x4)/10
f3 = lambda x1 ,x2, x3, x4    : (5.8-6*x1-7*x2+x4)/20
f4 = lambda x1 ,x2, x3, x4    : (4.3-12*x1-2*x2-3*x3)/(-30)

# Initial setup
x1_0 = 0
x2_0 = 0
x3_0 = 0
x4_0 = 0
count = 1

# Reading tolerable error
tolerance = float(input('Enter tolerable error: '))

# Implementation of Jacobi Iteration
print('\nCount\tx1\t\tx2\t\tx3\t\tx4\n')

condition = True

while condition:
    x1new = f1(x1_0,x2_0,x3_0, x4_0)
    x2new = f2(x1_0,x2_0,x3_0, x4_0)
    x3new = f3(x1_0,x2_0,x3_0, x4_0)
    x4new = f4(x1_0,x2_0,x3_0, x4_0)
   
    print('%d\t%0.6f\t%0.6f\t%0.6f\t%0.6f\n' %(count, x1new,x2new, x3new, x4new))
    
    # norm of solutions
    e1 = m.pow((x1new-x1_0),2)
    e2 = m.pow((x2new-x2_0),2)
    e3 = m.pow((x3new-x3_0),2)
    e4 = m.pow((x4new-x4_0),2)
    
    count += 1
    
    x1_0 = x1new
    x2_0 = x2new
    x3_0 = x3new
    x4_0 = x4new
    
    calculated_tolerance = m.sqrt(e1+e2+e3+e4)
    condition = calculated_tolerance > tolerance

print('\nSolution: x1=%0.3f, x2=%0.3f, x3 = %0.3f and x4 =%0.3f\n'% (x1new,x2new,x3new, x4new))
