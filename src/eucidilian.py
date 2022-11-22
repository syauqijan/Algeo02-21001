from step1 import *
from eigenfaces import *
import matplotlib.pyplot as plt
import numpy as np
import cv2

def weighttest(resultarr,testimg, mean):
    mean = reshapeimg(mean)
    for i in range(256):
        for j in range(256):
            testimg[i][j] -= mean[i][j]
    wtest = [[0 for i in range(256)] for j in range(256)]
    for k in range(len(resultarr)):
        wtest = np.add(wtest,(np.matmul(testimg,resultarr[k])))
    return wtest


def weightdata(resultarr,differenceimg):
    w = []
    for i  in range(len(differenceimg)):
        temp = [[0 for i in range(256)] for j in range(256)] 
        for j in range(len(resultarr)):
            temp = (np.add(temp,(np.matmul(differenceimg[i],resultarr[j]))))
        w.append(temp)
    return w


# plt.imshow(resultarr[0], cmap = 'gray')
# plt.show()
def euclidean_distance(x, y):
    sum = 0
    for i in range(256):
        # print("a")
        for j in range(256):
            x[i][j] = x[i][j] - y[i][j]
    for i in range(256):
        for j in range(256):
            sum += x[i][j]**2
    return np.sqrt(sum)
   

def distance(wtest, w):
    h = 0
    min = euclidean_distance(wtest,w[0])
    for i in range(1, len(w)):
        distance = euclidean_distance(wtest,w[i])
        print(distance)
        if distance < min :
            min = distance
            h = i
    return h

def showimg(images,h):
    images[h] = reshapeimg(images[h])
    # plt.imshow(images[h], cmap = 'RGB')
    # plt.show()
    images[h] = np.array(images[h])
    # cv2.imshow('image', images[h])
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
