# -*- coding: utf-8 -*-
"""
@author:Aslı Toplu
"""
"""
import cv2

import numpy as np

sifir=np.zeros([300,300])

bir=np.ones([300,300])

cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)

cv2.imshow("sifir",sifir)
cv2.imshow("bir",bir)

cv2.waitKey(0)

cv2.destroyAllWindows()
"""
import cv2
cam=cv2.VideoCapture(0)

print(cam.get(3))
print(cam.get(4))

cam.set(3,320)
cam.set(4,240)

print(cam.get(3))
print(cam.get(4))
if not cam.isOpened():
    print("kamera tanımadı")
    exit()

while True:
    ret,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if not ret:
        print("kameradan görüntü okunamıyor")
        break
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) & 0xFF==ord("q"): # q ile video sonlandı
        print("görüntü sonlandırıldı.")
        break
cam.release()
cv2.destroyAllWindows()





















