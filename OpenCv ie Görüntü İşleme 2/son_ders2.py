# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:20:16 2022

@author: Asli Toplu
"""
import cv2
import numpy as np


img=cv2.imread("1.jpeg")

print(img.shape)

rows,cols=img.shape[:2]

#src_points=np.float32([
#    [0,0]
#    [cols-1,0],
#    [0,rows-1],
#    [cols-1,rows-1]
#    ])

#dst_points=np.float32([
#    [0,0]
#    [cols-1,0],
#    [0,rows-1],
#    [cols-1,rows-1]
#    ])

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
def draw(event,x,y,flags,param):
    print(x,y)
    pass

"""src_points=np.float32([
    [80,100]
    [400,90],
    [50,400],
    [400,400]
    ])"""

"""dst_points=np.float32([
    [0,0]
    [cols-1,0],
    [0,rows-1],
    [cols-1,rows-1]
    ])

projective_matrix=cv2.getPerspectiveTransform(src_points,dst_points)
img_output=cv2.warpPerspective(img,projective_matrix,(cols,rows))
"""
cv2.setMouseCallback("img",draw)

while(1):
    cv2.imshow("img",img)
    #cv2.imshow("img_output",img_output)
    if cv2.waitKey(1)==ord("q"):
        break
cv2.waitKey()
cv2.destroyAllWindows()