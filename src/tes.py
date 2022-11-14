import numpy as np
import cv2
import os
# from function import *


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
            images.append(img)
    return images

#         cv2.imshow('image', resized)   #ini kalo mau ngeprint gambarnya
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()


def resize_image(folder):
    resized_images = []
    for image in load_images_from_folder(folder):
        resized = cv2.resize(image, (256, 256))
        resized_images.append(resized)
    return resized_images

path = 'test/dataset/pins_Zendaya'
matrix_img = resize_image(path)
print(matrix_img)





    
