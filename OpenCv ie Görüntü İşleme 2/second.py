# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:52:23 2022

@author: Asli Toplu
"""

import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("image.jpg")

kirp=resim[500:800,500:800]

resim[100:400,100:400]=kirp

plt.subplot(121)
plt.imshow(resim)
plt.subplot(122)
plt.imshow(kirp)
plt.show()