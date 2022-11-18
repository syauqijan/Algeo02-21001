# me-return mean dari suatu set matriks
import numpy as np

# def meanSetImg(setImg) :
#     sumImg = [[0 for i in range(256)] for j in range(256)]
#     for i in range(len(setImg)) :
#         sumImg = np.add(sumImg,setImg[i])

#     return np.multiply(sumImg, float(1/len(setImg)))

def meanSetImg(setImg) :                                       #ini nyoba buat 1 gambar aja
    sumImg = [[0 for i in range(256)] for j in range(256)]
    for i in range(1) :
        sumImg = np.add(sumImg,setImg[i])

    return np.multiply(sumImg, (1/1))