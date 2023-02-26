# -*- coding: utf-8 -*-
"""
@author:Aslı Toplu
"""
import cv2
from matplotlib import pyplot as plt

resim=cv2.imread("Moon.jpg",0)#0 resmi siyah beyaz yapıyor

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",resim) 
cv2.imshow("resim penceresi",resim) 

plt.imshow(resim,cmap="gray")
plt.show

k=cv2.waitKey(0)
if k==27:
    print("ESC tuşuna basıldı")
elif k== ord("q"):
   print("q tuşuna basıldı,Resim kayıt edildi.")
   cv2.imwrite("MoonBlack.jpg",resim)

#cv2.waitKey(0) & 0xFF #Resmin ekranda durması için 
#cv2.destroyWindows("resim penceresi")
cv2.destroyAllWindows()