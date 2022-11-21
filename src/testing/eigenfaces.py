import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def qr(A):
  #source: #https://rosettacode.org/wiki/QR_decomposition#Python
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        #calculate Householder matrix i: rows and i: columns from A i: rows and ith column
        H[i:, i:] = make_householder(A[i:, i])
        Q = Q@H
        A = H@A
    return Q, A
 
def make_householder(a):
    #find prependicular vector to mirror
    u = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    u[0] = 1
    H = np.eye(a.shape[0])
    #finding Householder projection
    H -= (2 / np.dot(u, u)) * u[:, None] @ u[None, :]
    return H


#eigenvektor
def find_eig_qr(A):
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