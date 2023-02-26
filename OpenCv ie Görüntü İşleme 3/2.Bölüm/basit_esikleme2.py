# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""
import cv2
resim=cv2.imread("cat.jpg",0)

def nothing(x):
    pass

cv2.namedWindow("resim")
cv2.createTrackbar("esik","resim",0,255,nothing)

while(1):
    thresh=cv2.getTrackbarPos("esik","resim")
    _,threshold_image=cv2.threshold(resim,thresh,255,cv2.THRESH_BINARY)
    
    cv2.imshow("resim",resim)
    cv2.imshow("threshold_image",threshold_image)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    
cv2.destroyAllWindows()
        