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

def mulmatrix(m1, m2):
    """Multiply two matrices of the same size"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] * m2[i][j])
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

def divmatrixnum(m1, num):
    """Divide a matrix with a number"""
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] / num)
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