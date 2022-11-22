import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

data = r'D:\Kelvin\code\python\Algeo02-21001\test\dataset'

#load foto
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
            images.append(img)
    return images

#resize 256 256
def resize_image(folder):
    resized_images = []
    for image in load_images_from_folder(folder):
        resized = cv2.resize(image, (256, 256),interpolation= cv2.INTER_AREA)
        resized_images.append(resized)
    return resized_images

#resize jadiin 256^2 1
def imagevector(folder) :
    vector_images = []
    for image in resize_image(folder) :
        vector_images.append(np.array(image).flatten())
    return vector_images

#rata2
def meanSetImg(setImg) :                                       
    sumImg = [0 for i in range(256*256)]
    length = len(setImg)
    for i in range(length) :
        for j in range(256*256) :
            sumImg[j] += setImg[i][j]
    
    return np.divide(sumImg, length)


#tiap foto dikurangin rata2
def setDiffImg(setImg, mean) :
    setDiff = []
  
    for i in range(len(setImg)) :
        setDiff.append(np.absolute(np.subtract(setImg[i],mean)))
    return setDiff

def covarian(setImg):
    covarian = np.matmul(setImg,np.transpose(setImg))
    return covarian

def reshapeimg(img) :
    result = [[0 for i in range(256)] for j in range(256)]
    k = 0
    for i in range(256) :
        for j in range(256) :
            result[i][j] = img[k]
            k += 1
    return result