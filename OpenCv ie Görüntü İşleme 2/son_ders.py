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

#translation_matrix=np.float32([
#    [1,0,-100],
#    [0,1,25]
 #   ])

#img_translation=cv2.warpAffine(img,translation_matrix,(cols+50,rows+50))
#res=cv2.resize(img,(300,300))

#res=cv2.resize(img,None,fx=0.5,fy=1)

#res=cv2.resize(img,None,fx=0.5,fy=0.5, interpolation=cv2.INTER_CUBIC)

#rotation_matrix=cv2.getRotationMatrix2D((cols/2,rows/2),30,0.7)
#img_rotation=cv2.warpAffine(img,rotation_matrix,(cols,rows))

src_points=np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1]
    ])

dst_points=np.float32([
    [0,0],
    [int(0.6*(cols-1)),0],
    [int(0.4*(cols-1)),rows-1]
    ])

affine_matrix=cv2.getAffineTransform(src_points,dst_points)
img_output=cv2.warpAffine(img,affine_matrix,(cols,rows))



cv2.imshow("img",img)
cv2.imshow("img_output",img_output)
#cv2.imshow("res",res)
#cv2.imshow("img_translation",img_translation)
#cv2.imshow("img_rotation",img_rotation)
cv2.waitKey()
cv2.destroyAllWindows()