import numpy as np
import matplotlib.pyplot as plt
from step1 import *

def qr(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
<<<<<<< Updated upstream:src/eigenfaces.py
        H[i:, i:] = householder(A[i:, i])
=======
        H[i:, i:] = make_householder(A[i:, i])
>>>>>>> Stashed changes:src/testing/eigenfaces.py
        Q = Q@H
        A = H@A
    return Q, A
 
<<<<<<< Updated upstream:src/eigenfaces.py
def householder(a):
    u = a / (a[0] + np.copysign(euclideanDistance(a,0), a[0]))
=======
def make_householder(a):
    u = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
>>>>>>> Stashed changes:src/testing/eigenfaces.py
    u[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def qreigen(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(10):
            Q,R = qr(X)
            pQ = pQ @ Q
            X = R @ Q

    return np.diag(X), pQ

<<<<<<< Updated upstream:src/eigenfaces.py
def euclideanDistance(x, y): 
    temp = np.subtract(x, y)
    sum_sq = np.dot(np.transpose(temp), temp)
    return(np.sqrt(sum_sq))


def eigface(eigvect,differenceimg):
    leneigen = round(len(differenceimg) * 0.06)
    resultarr = []
    k = 0
    for i in range(leneigen) :
        eigenfaces = np.matmul(eigvect,differenceimg)[i]
        result = [[0 for i in range(256)] for j in range(256)]
        for j in range(256):
            for l in range(256):
                result[j][l] += eigenfaces[k]
                k += 1
        k = 0
        resultarr.append(result)
    return resultarr
=======
def eigface(eigvect, normvect):
    eigfacearr = []
    eigenface = np.matmul(eigvect,normvect)
    for i in range(len(eigenface)):
        eigfacearr.append(eigenface[i])
        
>>>>>>> Stashed changes:src/testing/eigenfaces.py
