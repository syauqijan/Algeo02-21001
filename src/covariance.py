# kovarian dari hasil pengurangannya
import numpy as np
from setDiffImg import setDiffImg

# def covarianceMatrix(setImg) :
#     diff = setDiffImg(setImg)
#     cov = [[0 for i in range(256)] for j in range(256)]
#     for i in range(len(setImg)) :
#         a = np.dot(diff[i],np.transpose(diff[i]))
#         cov = np.add(cov,a)
#     return np.multiply(cov,1/(len(setImg)))

def covarianceMatrix(setImg) :
    concat = setImg[0]
    for i in range(1, len(setImg)) :
        concat = np.concatenate((concat, setImg[i]), axis=1)
    matrix_cov = np.matmul(concat, np.transpose(concat))
    return matrix_cov