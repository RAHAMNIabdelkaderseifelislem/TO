"""
createb by : aek426rahmani
date : 29-12-2022
"""
"""
this code is for solving linear programming problem
using simplex method
"""
import numpy as np

def simplex(A, b, c, x, m, n):
    B = np.zeros((m, m))
    for i in range(m):
        B[i][i] = 1
    xB = np.zeros(m)
    xN = np.zeros(n)
    for i in range(m):
        xB[i] = x[i]
    for i in range(n):
        xN[i] = x[m+i]
    cB = np.zeros(m)
    for i in range(m):
        cB[i] = c[xB[i]]
    cN = np.zeros(n)
    for i in range(n):
        cN[i] = c[xN[i]]
    Binv = np.linalg.inv(B)
    cBt = np.transpose(cB)
    cNt = np.transpose(cN)
    while True:
        z = np.matmul(np.matmul(cBt, Binv), b)
        y = np.matmul(cBt, Binv)
        rN = np.matmul(y, A) - cN
        rNt = np.transpose(rN)
        rNt = np.array(rNt)
        rNt = np.append(rNt, [1])
        rNt = np.array(rNt)
        rNt = np.reshape(rNt, (1, n+1))
        if np.all(rNt >= 0):
            break
        j = np.argmin(rNt)
        if j == n:
            print("No feasible solution")
            return
        d = np.matmul(Binv, A[:, j])
        if np.all(d <= 0):
            print("No unbounded solution")
            return
        theta = np.zeros(m)
        for i in range(m):
            if d[i] > 0:
                theta[i] = b[i]/d[i]
        i = np.argmin(theta)
        xB[i] = xN[j]
        xN[j] = xB[i]
        B[:, i] = A[:, j]
        Binv = np.linalg.inv(B)
        cB = np.zeros(m)
        for i in range(m):
            cB[i] = c[xB[i]]
        cN = np.zeros(n)
        for i in range(n):
            cN[i] = c[xN[i]]
        cBt = np.transpose(cB)
        cNt = np.transpose(cN)
    print("Optimal solution is : ", z)
    print("Optimal solution vector is : ", xB)
    print("Optimal solution vector is : ", xN)

if __name__ == "__main__":
    A = np.array([[1, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1]])
    b = np.array([100, 80, 40, 50])
    c = np.array([10, 6, 4, 0, 0, 0])
    x = np.array([0, 1, 2, 3, 4, 5])
    m = 4
    n = 6
    simplex(A, b, c, x, m, n)
    