import numpy as np
import cv2
import os
from function import *


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        resized = cv2.resize(img, (256, 256))
        if img is not None:
            images.append(img)
            
            printmatrix(resized)
#         cv2.imshow('image', resized)   #ini kalo mau ngeprint gambarnya
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

# tes = load_images_from_folder(path)
# print(tes)
path = 'test/dataset/pins_Zendaya'
load_images_from_folder(path)




    
