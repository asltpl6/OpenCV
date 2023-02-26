# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""

import cv2
import asli

resim=cv2.imread("siyah_beyaz.jpg",0)

ret,resim_thresh = cv2.threshold(resim,182,255,cv2.THRESH_BINARY)

ret2,resim_thresh2 = asli.threshold(resim, 182, 255)


cv2.namedWindow("resim",cv2.WINDOW_NORMAL) #Resmin boyutu ile oynamak için yazıyoruz
cv2.namedWindow("resim_thresh",cv2.WINDOW_NORMAL)
cv2.namedWindow("resim_thresh2",cv2.WINDOW_NORMAL) 
   
cv2.imshow("resim",resim)
cv2.imshow("resim_thresh",resim_thresh)
cv2.imshow("resim_thresh2",resim_thresh2)
cv2.waitKey()
cv2.destroyAllWindows()