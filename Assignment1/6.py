import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


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


def size(A: list):  # return size of matrix
    n = len(A)
    if n == 0:
        return [0, 0]
    else:
        m = len(A[0])
    for i in range(len(A)):
        if len(A[i]) != m:
            print("Incorrect matrix")
            raise RuntimeError
    return [n, m]


def sum(A, B):
    an, am = size(A)
    bn, bm = size(B)
    if an != bn and am != bm:
        print("Incorrect matrix")
        raise RuntimeError
    sum = []
    for i in range(an):
        row = []
        for j in range(am):
            row.append(A[i][j] + B[i][j])
        sum.append(row)
    return sum


def mult(A, B):
    an, am = size(A)
    bn, bm = size(B)
    if am != bn:
        print("Incorrect matrix")
        raise RuntimeError
    product = []
    for i in range(an):
        row = []
        for j in range(bm):
            sum = 0
            for g in range(am):
                sum += A[i][g] * B[g][j]
            row.append(sum)
        product.append(row)
    return product


def linear_method(x, t, a: float, b: float, d):
    x1, x2 = x
    dx1dx2 = [-a * x1 - b * x2 - d(t), x1]
    return dx1dx2


def state_space(x, t, a, n, func):
    b = [[-func(t)], [0]]
    X = [[x[0]], [x[1]]]
    A = ss(a, n)
    prod = mult(A, X)
    res = sum(prod, b)
    return [res[0][0], res[1][0]]


x0 = [0, -3]
t = np.linspace(0, 10, 200)
func = lambda t: -np.sin(4 * t)
ode = odeint(linear_method, x0, t, args=(2, -3, func))
y1 = []
for val in ode:
    y1.append(val[1])
ode = odeint(state_space, x0, t, args=([1, 2, -3], 2, func))
ys = []
y2 = []
for val in ode:
    y2.append(val[1])

plt.plot(t, y1, label="Linear")
plt.plot(t, y2, label="State Space")
plt.show()