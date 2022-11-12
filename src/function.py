import numpy as np

def addmatrix(m1, m2):
    """Add two matrices of the same size"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] + m2[i][j])
    return result

def submatrix(m1, m2):
    """Subtract two matrices of the same size"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] - m2[i][j])
    return result

def abssubmatrix(m1, m2):
    """Subtract two matrices of the same size with absolute"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(abs(m1[i][j] - m2[i][j]))
    return result

def multimatrix(m1, m2):
    result = np.dot(m1, m2)
    return result

def divmatrix(m1, m2):
    """Divide two matrices of the same size"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] / m2[i][j])
    return result

def mulmatrixnum(m1, num):
    """Multiply a matrix with a number"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] * num)
    return result

def determinantmatrix(m1):
    det = np.linalg.det(m1)
    return det

def transposematrix(m1):
    result = np.transpose(m1)
    return result

def inversematrix(m1):
    result = np.linalg.inv(m1)
    return result

def kovarian(m1):
    result = multimatrix(m1, transposematrix(m1))
    return result

def printmatrix(m1):
    for i in range(len(m1)):
        print(m1[i])