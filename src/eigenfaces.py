import numpy as np
import matplotlib.pyplot as plt
from step1 import *

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
    u = a / (a[0] + np.copysign(euclideanDistance(a,0), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H

def euclideanDistance(x, y): 
    temp = np.subtract(x, y)
    sum_sq = np.dot(np.transpose(temp), temp)
    return(np.sqrt(sum_sq))


def qreigen(A):
    pQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(10):
            Q,R = qr(X)
            pQ = pQ @ Q
            X = R @ Q

    return np.diag(X), pQ

def eigface(eigvect, normvect):
    eigfacearr = []
    eigenface = np.matmul(eigvect,normvect)
    z = 0
    for i in range(round(len(eigenface)*0.08)):
        result = [[0 for i in range(256)] for j in range(256)]
        for j in range(256):
            for l in range(256):
                result[j][l] += eigenface[i][z]
                z += 1
        z = 0
        eigfacearr.append(result)
    return eigfacearr
        
        
