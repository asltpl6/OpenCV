# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim=cv2.imread("closing.png",0)

#_,resim=cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#gri resmi siyah beyaz yaptı

kernel=np.ones((9,9),np.uint8)

erosion=cv2.erode(resim,kernel,iterations=1)
dilation=cv2.dilate(resim,kernel,iterations=1)
opening=cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel)
closing=cv2.morphologyEx(resim,cv2.MORPH_CLOSE,kernel)
tophat=cv2.morphologyEx(resim,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(resim,cv2.MORPH_BLACKHAT,kernel)
gradient=cv2.morphologyEx(resim,cv2.MORPH_GRADIENT,kernel)


plt.subplot(241),plt.imshow(resim,"gray"),plt.title("orginal")
plt.subplot(242),plt.imshow(erosion,"gray"),plt.title("erosion")
plt.subplot(243),plt.imshow(dilation,"gray"),plt.title("dilation")
plt.subplot(244),plt.imshow(opening,"gray"),plt.title("opening")
plt.subplot(245),plt.imshow(closing,"gray"),plt.title("closing")

plt.subplot(246),plt.imshow(dilation,"gray"),plt.title("tophat")
plt.subplot(247),plt.imshow(opening,"gray"),plt.title("blackhat")
plt.subplot(248),plt.imshow(closing,"gray"),plt.title("gradient")


plt.show()