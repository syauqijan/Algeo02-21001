import numpy as np

def QR_Decomposition(A):
    n, m = A.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = A[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):

        u[:, i] = A[:, i]
        for j in range(i):
            u[:, i] -= (A[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = A[:, j] @ Q[:, i]

    return Q, R

m = 4
n = 4

A = np.random.rand(m, n)
q, r = np.linalg.qr(A)
Q, R = QR_Decomposition(A)

with np.printoptions(linewidth=9999, precision=20, suppress=True):
    print("**** Q from qr_decomposition")
    print(Q)
    print("**** Q from np.linalg.qr")
    print(q)
    print()
    
    print("**** R from qr_decomposition")
    print(R)
    print("**** R from np.linalg.qr")
    print(r)