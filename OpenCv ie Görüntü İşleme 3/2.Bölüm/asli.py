# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""

def threshold(src,thresh,maxval):
    
    """
    Bu fonksiyon ile basit eşikleme işlemi yapılabilir.
    src=image
    thresh=0...255
    maxval=0...255
    """
    img=src.copy()
    rows,cols=img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if img[i,j]< thresh:
                img[i,j]=0
            else:
                img[i,j]=maxval
                
    return thresh, img