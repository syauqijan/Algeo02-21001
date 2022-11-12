# me-return mean dari suatu set matriks

from function import addmatrix, mulmatrixnum

def meanSetImg(setImg) :
    sumImg = [[0]*len(setImg[0])]*len(setImg[0])
    for i in range(len(setImg)) :
        sumImg = addmatrix(sumImg,setImg[i])

    return mulmatrixnum(sumImg, float(1/len(setImg)))