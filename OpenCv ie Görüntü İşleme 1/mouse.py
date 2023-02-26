# -*- coding: utf-8 -*-
"""
@author:Aslı Toplu
"""
import cv2
import numpy as np

def draw(event, x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
    pass


img =np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")

cv2.setMouseCallback("paint",draw)

while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
