from step1 import *
from eigenfaces import *
from eucidilian import *
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

data = r'D:\Kelvin\code\python\Algeo02-21001\test\compress\test'

images = resize_image(data)

mean = meanSetImg(images)

imgvect = imagevector(images)

normvect = normalvect(imgvect)

covariance = covarian(imgvect)

tempval, eigvect = find_eig_qr(covariance)



# eigfacearr = eigface(eigvect,imgvect)


