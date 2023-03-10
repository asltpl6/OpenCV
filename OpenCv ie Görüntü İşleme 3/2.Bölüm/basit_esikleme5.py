# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""
import cv2
import matplotlib.pyplot as plt

resim=cv2.imread("wp.jpeg",0)

ret, th=cv2.threshold(resim,120,255,cv2.THRESH_BINARY)

thresh=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,33,4)

thresh2=cv2.adaptiveThreshold(resim,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,33,4)

plt.subplot(2,2,1),plt.imshow(resim,"gray"),plt.title("original image")
plt.subplot(2,2,2),plt.imshow(th,"gray"),plt.title("global threshold")
plt.subplot(2,2,3),plt.imshow(thresh,"gray"),plt.title("thresh mean")
plt.subplot(2,2,4),plt.imshow(thresh2,"gray"),plt.title("thresh2 gaussian")

plt.show()