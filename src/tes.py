import numpy as np
import cv2
import os
import numpy as np
from meanSetImg import *
from setDiffImg import *
from covariance import *
from tes_eigen import *


# def load_images_from_folder(folder):
#     images = []
#     for filename in os.listdir(folder):
#         img = cv2.imread(os.path.join(folder,filename),0)
#         if img is not None:
#             images.append(img)
#     return images

#         cv2.imshow('image', resized)   #ini kalo mau ngeprint gambarnya
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()


# def resize_image(folder):
#     resized_images = []
#     for image in load_images_from_folder(folder):
#         resized = cv2.resize(image, (256, 256))
#         resized_images.append(resized)
#     return resized_images

def resize(path):                                  #ini nyoba buat 1 gambar aja
    img = cv2.imread(path,0)
    resized = cv2.resize(img, (256, 256))
    return resized

path = 'test/dataset/pins_Zendaya/Zendaya22_1857.jpg'
matrix_img = np.array(resize(path))
print((matrix_img))

matrix_mean = meanSetImg(matrix_img)
print(matrix_mean)
matrix_selisih = setDiffImg(matrix_img, matrix_mean)
print(matrix_selisih)
matrix_cov = covarianceMatrix(matrix_selisih)
print(matrix_cov)

# val, vec = find_eig_qr(matrix_cov)
# print(val, vec)

    
    










    
