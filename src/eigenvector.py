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
    u = a / (a[0] + np.copysign(euclidean_distance(a,0), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def qreigen(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    # print(pQ)
    # print(X)
    for i in range(1):
            Q,R = qr(X)
            pQ = pQ @ Q
            X = R @ Q
    # for i in range(len(X)):

    return np.diag(X), pQ

def euclidean_distance(x, y): 
    temp = np.subtract(x, y)
    sum_sq = np.dot(np.transpose(temp), temp)
    return(np.sqrt(sum_sq))

# m = 4
# n = 4

# A = np.random.rand(m, n)
# # B = find_eig_qr(A)
# # print(B)

# q, r = np.linalg.qr(A)
# Q, R = qr(A)

# with np.printoptions(linewidth=9999, precision=20, suppress=True):
#     print("**** Q from qr_decomposition")
#     print(Q)
#     print("**** Q from np.linalg.qr")
#     print(q)
#     print()
    
#     print("**** R from qr_decomposition")
#     print(R)
#     print("**** R from np.linalg.qr")
#     print(r)