# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("kizkulesi.jpg",0)

sobelX= cv2.Sobel(img,-1,1,0,ksize=5)
sobelY= cv2.Sobel(img,-1,0,1,ksize=5)
sobel=cv2.Sobel(img,-1,1,1,ksize=5)

sobelX2=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelX2=np.absolute(sobelX2)
sobelX2=np.uint8(sobelX2)

laplacian=cv2.Laplacian(img,-1,ksize=1)

canny=cv2.Canny(img,0,1)

plt.subplot(3,3,1),plt.imshow(img,"gray"),plt.title("orijinal")
plt.subplot(3,3,2),plt.imshow(sobelX,"gray"),plt.title("sobelX")
plt.subplot(3,3,3),plt.imshow(sobelY,"gray"),plt.title("sobelY")
plt.subplot(3,3,4),plt.imshow(sobel,"gray"),plt.title("sobel")
plt.subplot(3,3,5),plt.imshow(sobelX2,"gray"),plt.title("sobelX2")
plt.subplot(3,3,6),plt.imshow(laplacian,"gray"),plt.title("laplacian")
plt.subplot(3,3,7),plt.imshow(canny,"gray"),plt.title("canny")

plt.show()


