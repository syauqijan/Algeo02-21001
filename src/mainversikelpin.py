from step1 import *
from eigenfaces import *
from eucidilian import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

data = r'D:\Kelvin\code\python\Algeo02-21001\test\dataset'

images = load_images_from_foldergray(data)
colorimg = load_images_from_folder(data)
images = resize_image(images)

mean = meanSetImg(images)

imgvect = imagevector(images)

normvect = normalvect(imgvect)

covariance = covarian(imgvect)

tempval, eigvect = qreigen(covariance)

eigfacearr = eigface(eigvect,imgvect)


test = r'D:\Kelvin\code\python\Algeo02-21001\test\compress\Rihanna149_3980.jpg'

testimg = cv2.imread(test,0)

testimg = cv2.resize(testimg,(256,256),interpolation = cv2.INTER_AREA)

normtest = normimg(testimg,mean)
normdata = normilazi(images)

wtest = weighttest(eigfacearr,normtest)

w = weightdata(eigfacearr,normdata)

x = distance(wtest,w)

showimg(colorimg,x)


