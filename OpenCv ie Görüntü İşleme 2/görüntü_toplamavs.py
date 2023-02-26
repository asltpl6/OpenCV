# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 13:52:23 2022

@author: Asli Toplu
"""

import cv2
import numpy as np

img1 = cv2.imread("cv2.png")
img2 = cv2.imread("d.jpg")


toplam=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow("resim",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()