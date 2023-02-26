# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:01:31 2022

@author: Asli Toplu
"""

import cv2

url="http://192.168.1.101:8080/video"

cam=cv2.VideoCapture(url)

while cam.isOpened():
    ret,frame=cam.read()
    
    if not ret:
        print("Kamera görüntü okumadı")
    
    cv2.imshow("görüntü", frame)
    
    if cv2.waitKey(1)== ord("q"):
        break
    
cv2.destroyAllWindows()