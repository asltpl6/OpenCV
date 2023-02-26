# -*- coding: utf-8 -*-
"""
@author:Aslı Toplu
"""
import cv2


cam = cv2.VideoCapture(0)

fourrc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter("recording.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    
    ret,frame=cam.read()
    
    if not ret:
        print("kameradan görüntü alındı")
        break
    
    out.write(frame)
    
    cv2.imshow("kamera",frame)
    
    if cv2.waitKey(1) == ord("q"):
        print("videodan ayrıldınız.")
        break

cam.release()
out.release()
cv2.destroyAllWindows()