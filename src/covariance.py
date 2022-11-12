from function import multimatrix, transposematrix, addmatrix, mulmatrixnum
from setDiffImg import setDiffImg

def covarianceMatrix(setImg) :
    diff = setDiffImg(setImg)
    cov = [[0 for i in range (len(diff[0]))] for j in range(len(diff[0]))]
    for i in range(len(setImg)) :
        a = multimatrix(diff[i],transposematrix(diff[i]))
        cov = addmatrix(cov, a)
    return mulmatrixnum(cov,1/(len(setImg)))