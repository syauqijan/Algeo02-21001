import numpy as np
import matplotlib.pyplot as plt
from step1 import *

def qr(M):
    row, col = M.shape
    Q = np.eye(row)
    for i in range(col - (row == col)):
        house_holder = np.eye(row)
        house_holder[i:, i:] = householder(M[i:, i])
        Q = np.dot(Q, house_holder)
        M = np.dot(house_holder, M)
    return Q, M
 
def householder(a):
    u = a / (a[0] + np.copysign(euclideanDistance(a,0), a[0]))
    u[0] = 1
    house_holder = np.eye(a.shape[0])
    house_holder -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return house_holder

def euclideanDistance(x, y): 
    temp = np.subtract(x, y)
    sum_sq = np.dot(np.transpose(temp), temp)
    return(np.sqrt(sum_sq))


def qreigen(M):
    pQ = np.eye(M.shape[0])
    X=M.copy()
    for i in range(10):
            Q,R = qr(X)
            pQ = np.dot(pQ,Q)
            X = np.dot(R,Q)

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
        
        
