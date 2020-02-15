import numpy as np

def ss(a, n):  # function takes array and its size as arguments
    A = []
    row = []
    for i in range(n):
        row.append(-a[n - i - 1] / a[n])
    A.append(row)
    for i in range(n - 1):
        row = []
        for j in range(n):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        A.append(row)
    return A