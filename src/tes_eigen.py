import numpy as np
from typing import Union

def find_householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    tau = 2 / (v.T @ v)
    
    return v,tau

def find_qr(A: np.ndarray) -> Union[np.ndarray, np.ndarray]:
    m,n = A.shape
    R = A.copy()
    Q = np.identity(m)
    
    for j in range(0, n):
        v, tau = find_householder(R[j:, j, np.newaxis])
        
        H = np.identity(m)
        H[j:, j:] -= tau * (v @ v.T)
        R = H @ R
        Q = H @ Q
        
    return Q[:n].T, np.triu(R[:n])

def find_eig(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(10):
            Q,R = find_qr(X)
            pQ = pQ @ Q;
            X = R @ Q;
    return np.diag(X), pQ


# m = 4
# n = 4

# A = np.array([[2., 1., 1.],[1., 3., 2.],[1., 0., 0]])
# # B = find_eig_qr(A)
# # print(B)

# q, r = np.linalg.eig(A)
# Q, R = find_eig(A)

# with np.printoptions(linewidth=9999, precision=20, suppress=True):
#     print("**** Q from qr_decomposition")
#     print(Q)
#     print("**** Q from np.linalg.eig")
#     print(q)
#     print()
    
#     print("**** R from qr_decomposition")
#     print(R)
#     print("**** R from np.linalg.eig")
#     print(r)
