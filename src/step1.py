import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

data = r'D:\Kelvin\code\python\Algeo02-21001\test\dataset'

#load foto
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

def load_images_from_foldergray(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
            images.append(img)
    return images
#resize 256 256
def resize_image(folder):
    resized_images = []
    for i in range (len(folder)):
        resized = cv2.resize(folder[i], (256, 256),interpolation= cv2.INTER_AREA)
        resized_images.append(resized)
    return resized_images

#resize jadiin 256^2 1
def imagevector(images):
    vector_images = []
    for i in range (len(images)) :
        vector_images.append(np.array(images[i]).flatten())
    return vector_images

#rata2
def meanSetImg(setImg) :                                       
    sumImg = [[0 for i in range(256)] for j in range (256)]
    length = len(setImg)
    for i in range(length) :
        for j in range(256) :
            for k in range (256) :
                sumImg[j][k] += setImg[i][j][k]/length
    
    return sumImg

def meanVect(setImg) :
    mean = [0 for i in range (256*256)]
    length = len(setImg)
    for i in range(length) :
        for j in range (256*256) :
            mean[j] += setImg[i][j]/length
    return mean


#tiap foto dikurangin rata2
# def setDiffImg(setImg, mean) :
#     setDiff = []
#     temp = [0 for i in range (256*256)]
#     for i in range(len(setImg)) :
#         for j in range (256*256):
#             temp = setImg[i][j] - mean[j]
#         setDiff.append (temp)
#     return setDiff

def normilazi(setImg):
    normal= []
    mean = meanSetImg(setImg)
    norm = [[0 for j in range(256)] for k in range(256)]
    for i in range (len(setImg)):
        norm[i] = np.subtract(setImg[i], mean)
        normal.append(norm[i])
    return normal
            

def normalvect(setImg) :
    mean = meanVect(setImg)
    setDiff = [[0 for j in range (256*256)] for i in range (len(setImg))]
    z = 0
    for i in range(len(setImg)) :
        for j in range(256*256) :
            setDiff[i][j] = setImg[i][j] - mean[j]

    return setDiff

def normimg(img, mean) :
    result = [[0 for i in range(256)] for j in range(256)]
    for i in range(256) :
        for j in range(256) :
            result[i][j] = img[i][j] - mean[i][j]
    return result
                

def covarian(setImg):
    norm = normalvect(setImg)
    length = len(setImg)
    cov = [[0 for i in range(length)] for j in range(length)]
    cov = np.matmul(norm, np.transpose(norm))
    return cov


def reshapeimg(img) :
    result = [[0 for i in range(256)] for j in range(256)]
    k = 0
    for i in range(256) :
        for j in range(256) :
            result[i][j] = img[k]
            k += 1
    return result

def summatrix(matrix) :
    sum = [[0 for i in range(256)] for j in range(256)]
    for i in range (len(matrix)) :
        sum = np.add(sum, matrix[i])
        
    return sum