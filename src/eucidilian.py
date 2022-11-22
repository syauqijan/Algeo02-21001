from step1 import *
from eigenfaces import *
import matplotlib.pyplot as plt
import numpy as np
import cv2

def weighttest(resultarr,testimg):
    wtest = [[0 for i in range(256)] for j in range(256)]
    wtest = np.matmul(testimg,summatrix(resultarr))
    return wtest


def weightdata(resultarr,differenceimg):
    w = []
    for i  in range(len(differenceimg)):
        temp = [[0 for i in range(256)] for j in range(256)] 
        temp = np.matmul(differenceimg[i],summatrix(resultarr))
        w.append(temp)
    return w


def euclidean_distance(wtest, wdata):
    wdata = np.subtract(wtest,wdata)
    wdata = np.square(wdata)
    dis = np.sum(wdata)
    # dis = np.sqrt(range)
    return dis

    
   

def distance(wtest, w):
    h = 0
    min = euclidean_distance(wtest,w[0])
    for i in range(1, len(w)):
        distance = euclidean_distance(wtest,w[i])
        print(distance)
        if distance < min :
            min = distance
            h = i
    print(min)
    return h

def showimg(images,h):
    # plt.imshow(images[h], cmap = 'RGB')
    # plt.show()
    images[h] = np.array(images[h])
    cv2.imshow('image', images[h])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
