# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""
import cv2

resim=cv2.imread("home.jpg",0)

#blur=cv2.GaussianBlur(resim,(15,15),0)# resmi gürültüden azaltır.

#ret,th= cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret,th= cv2.threshold(resim,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(ret)

cv2.imshow("resim",resim)
cv2.imshow("th",th)

cv2.waitKey()
cv2.destroyAllWindows()