# a computer program to form a Divided Difference Table for any given set of data points
def ndd(X,Y):
    table = nddiff(X,Y)
    printtable(table)

# returns the divided difference value
def func(fxi, fxj, xi, xj):
    return ((fxi - fxj)/(xi - xj))

# returns dividede difference table as 2D array
def nddiff(X, Y):
    
    #    X = [x1, x2, x3, x4,....]
    #    Y = [y1, y2, y3, y4,....]
    
    table = []  # initiate empty list
    table.append(list(X))   # add first and second column in the DD table
    table.append(list(Y))
    
    #  creating divided differenance table
    for i in range(len(table[0])-1):
        fdd = []
        for j in range(len(table[-1])-1):
            fdd_val = func(table[-1][j], table[-1][j+1], table[0][j], table[0][i+j+1])
            fdd.append(fdd_val)
        table.append(fdd)
    return table

# function to print divided difference table
def printtable(table):
    for i in range (len(table[0])):
        print('%0.0f\t' %(i), end = "")
        for j in range(len(table)-i):
            print('%f\t' %(table[j][i]), end = "")
        print("")

