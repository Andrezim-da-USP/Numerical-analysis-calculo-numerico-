# lsm 
import numpy as np

def lsm(x,y,n:int)->np.ndarray:
    '''This funcion returns
    the coefficientes of the polynomial that better fits
    the input data in x and y. The degree of the polynomial is
    determined by the 3rd parameter n. So if you wanna make a linear 
    regression, you must use n = 1'''
    if n <= 0: raise Exception("You must enter a positive value for degree of the polynomial")
    k = len(x)
    u = np.zeros((n+1, k), dtype=float) 
    m = np.zeros((n+1,n+1), dtype=float) #m stands for the matrix of the inner products 
    s = np.zeros((n+1,1), dtype=float) # s stands for the column matrix of the inner product of the y elements with the u elements
    for i in range(n+1):
        u[i] = x**i
    for i in range(n+1):
        for j in range(n+1):
            m[i,j] = np.inner(u[j],u[i])
    for i in range(n+1):
        s[i] = np.inner(y,u[i])
    return np.linalg.solve(m,s) # the coefficients of the polynomial are the solution of the linear system.


# a little test to check using an example from Neide's book of 'Calculo numerico'
x = np.array([-1,0,1,2])
y = np.array([0,-1,0,7])
print(lsm(x,y,2))