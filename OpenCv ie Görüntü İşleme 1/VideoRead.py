# -*- coding: utf-8 -*-
"""
@author:Aslı Toplu
"""
import cv2
cam=cv2.VideoCapture("video.mp4")
while cam.isOpened():
    ret,frame=cam.read()
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if not ret:
        print("kameradan görüntü okunamıyor")
        break
    cv2.imshow("görüntü",frame)
    if cv2.waitKey(1)& 0xFF ==ord("q"):
        print("Video kapandı")
        break
cam.release()
cv2.destroyAllWindows()
