# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""

import cv2
import matplotlib.pyplot as plt

resim=cv2.imread("cat.jpg",0)

_,resim_thresh1 = cv2.threshold(resim,182,255,cv2.THRESH_BINARY)
_,resim_thresh2= cv2.threshold(resim,182,255,cv2.THRESH_BINARY_INV)
_,resim_thresh3 = cv2.threshold(resim,182,255,cv2.THRESH_TRUNC)
_,resim_thresh4 = cv2.threshold(resim,182,255,cv2.THRESH_TOZERO)
_,resim_thresh5 = cv2.threshold(resim,182,255,cv2.THRESH_TOZERO_INV)

resimler=[resim,resim_thresh1,resim_thresh2,
          resim_thresh3,resim_thresh4,resim_thresh5]
baslıklar=["orginal resim","binary","binary_inv",
           "trunc","to_zero","to_zero_inv"]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(resimler[i],"gray")
    plt.title(baslıklar[i])
plt.show()