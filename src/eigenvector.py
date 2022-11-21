import numpy as np

# yang di return eigenvalue, eigenvector.
# yang dipanggil qreigen(A)

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = householder(A[i:, i])
        Q = Q@H
        A = H@A
    return Q, A
 
def householder(a):
    u = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def qreigen(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    # print(pQ)
    # print(X)
    for i in range(100):
            Q,R = qr(X)
            pQ = pQ @ Q
            X = R @ Q
    # for i in range(len(X)):

    return np.diag(X), pQ