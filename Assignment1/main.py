import numpy as np
def ss(a, n):                    #function takes array and its size as arguments
    a = np.flip(a)               #after this coefficients in this order: a_k, .. , a_0, b_0
    new_coef = a[1:] / a[0]      #calculating coefficients: y^{k}=(-b_{0}/a_{k})-a_{0}/a_{k}*y+..+(-a_{k-1}/a_{k}*y^{k-1}), without minus sign
    A = np.zeros((n - 1, n - 1))     #filling matrix with zeros
    A[0, 0:] = -new_coef         #calculating coefficients: y^{k}=-a_{0}/a_{k}*y+..+(-a_{k-1}/a_{k}*y^{k-1}), with minus sign, putting in matrix
    A[1:, 0:(n - 2)] = np.eye(n - 2) #making diagonal next to main diagonal filled with 1's
    print(A)                     #displaying matrix A of State Space model
