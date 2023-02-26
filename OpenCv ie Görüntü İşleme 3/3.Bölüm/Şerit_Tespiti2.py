# -*- coding: utf-8 -*-
"""
@author: Asli Toplu
"""
import cv2
import numpy as np

cam = cv2.VideoCapture("car8.mp4")
x, y = int(cam.get(3)),int(cam.get(4))
sapma = 0
k = []
k2 = []

def crop_ver(image, sapma=sapma):
    """
    Parameters
    ----------
    image : TYPE
        DESCRIPTION.
    sapma : TYPE, optional
        DESCRIPTION. The default is sapma.

    Returns
    -------
    value : TYPE
        DESCRIPTION.

    """
    x,y = image.shape[:2]
    value= np.array([
        [(sapma,x-sapma),(int((y*3.5)/8),int(x*0.6)),
         (int((y*4.5)/8),int(x*0.6)),(y,x-sapma)]],np.int32)
    return value

def new_crop(line_l, line_r):
    try:
        lx1, ly1, lx2, ly2 = line_l
        rx1, ry1, rx2, ry2 = line_r
        value= np.array([
            [(lx1,ly1),(lx2,ly2),
             (rx1, ry1),(rx2,ry2)]],np.int32)
    except:
        value= np.array([
            [(0,0),(0,0),
             (0, 0),(0,0)]],np.int32)
        return value
    return value

def crop_al(image, value):
    x,y = image.shape[:2]
    mask = np.zeros(shape = (x, y), dtype=np.uint8)
    mask = cv2.fillPoly(mask, value, 255)   
    masked = cv2.bitwise_and(image, image, mask=mask)
    return masked

def edge_filtre(image):
    image = cv2.erode(image, np.ones((1,9), np.uint8))
    image = cv2.dilate(image, np.ones((3,9), np.uint8))
    image = cv2.medianBlur(image, 9)
    image = cv2.Canny(image,0,200)
    return image

def draw_polylines(img, matris):
    dst = np.array([[matris[0][1,0],matris[0][1,1]],
                    [matris[0][0,0],matris[0][0,1]],
                    [matris[0][3,0],matris[0][3,1]],
                    [matris[0][2,0],matris[0][2,1]]],np.int32)
    cv2.polylines(img, [dst], True, (0,200,200), 2)
    return img

def hough(image, threshold=20):
    left_av = []
    right_av = []
    lines = cv2.HoughLines(image, 1, np.pi/180, 
                           threshold)
    if not isinstance(lines, type(None)):
        for line in lines:
            for rho, theta in line:
                # print(theta)
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                
                x1 = int(x0 + 10000*(-b))
                y1 = int(y0 + 10000*(a))
                x2 = int(x0 - 10000*(-b))
                y2 = int(y0 - 10000*(a))
                
                try:
                    slope = (y2-y1)/(x2-x1)
                    # 0'a bölme hatası verebilir
                except:
                    slope = 0.00001
                if slope > 0.54:
                    right_av.append((x1,y1,x2,y2))
                elif slope < -0.54:
                    left_av.append((x1,y1,x2,y2))
                    
        right_avg = np.average(right_av, axis=0)
        left_avg = np.average(left_av, axis=0)
        
        if not isinstance(right_avg, type(np.nan)):
            if not isinstance(left_avg, type(np.nan)):
                return right_avg, left_avg
            else:
                return right_avg, None
        else:
            if not isinstance(left_avg, type(np.nan)):
                return None, left_avg
            else:
                return None,None
    else:
        return None, None

def draw_line(image, lines, r=10, color=(0,255,0)):
    img = image.copy()
    x,y = image.shape[:2]
    crop_img = image[0:int(x*0.6),:]
    lines = np.int0(np.around(lines))
    if lines is not None:
        x1, y1, x2, y2 = lines
        cv2.line(img, (x1,y1), (x2,y2), color, r)
    img[0:int(x*0.6),:] = crop_img
    return img

def pers(img, matris, resize_x=300, resize_y=200):
    x, y = img.shape[:2]
    src = np.float32([
        [matris[0][1,0],matris[0][1,1]],
        [matris[0][2,0],matris[0][2,1]],
        [matris[0][0,0],matris[0][0,1]],
        [matris[0][3,0],matris[0][3,1]]])
    dst = np.float32([
        [0,0],
        [y-1,0],
        [0,x-1],
        [y-1,x-1]])
    M = cv2.getPerspectiveTransform(src,dst)
    img_output = cv2.warpPerspective(img, M, (y,x))
    img_output = cv2.resize(img_output, (resize_x, resize_y))
    return img_output


while cam.isOpened():
    ret, img_org = cam.read()
    if not ret:
        break
    
    img = img_org.copy()

    value = crop_ver(img)

    img = crop_al(img, value)
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # lower = np.array([0,0,200])
    # upper = np.array([255,45,255])

    lower = np.array([0,0,200])
    upper = np.array([255,255,255])

    # lower = np.array([0,0,220])
    # upper = np.array([255,255,255])

    mask = cv2.inRange(img_hsv,lower,upper)
    # res = cv2.bitwise_and(img,img,mask=mask)
    
    edges = edge_filtre(mask)
    
# =============================================================================
    # Gorsellestirme amacli

    img_org[:200,600:900] = cv2.resize(img_org, (300,200))
    img_org[:200,300:600] = cv2.cvtColor(cv2.resize(edges, (300,200)), 
                                         cv2.COLOR_GRAY2BGR)
    img_org[:200,:300] = pers(img_org, value)
# =============================================================================
    
    right_lines, left_lines = hough(edges)
    
    img_org2 = img_org.copy()
    crop_img1 = img_org2[0:int(x*0.6),:]
    crop_img2 = img_org2[x-sapma:x,:]

    value_new = new_crop(left_lines, right_lines)
    zeros = np.zeros_like(img)
    zeros = cv2.fillPoly(zeros, [value_new], (50,50,0))
    img_org = cv2.addWeighted(img_org,1,zeros,1,0)
    img_org[0:int(x*0.6),:] = crop_img1
    img_org[x-sapma:x,:] = crop_img2

    zeros = np.zeros_like(img)

    # sonuc cizgilerinin ortalama alma islemleri
    # sadece 10 degerin ortalaması alınır
    # yeni gelen olursa önceki dizide en eski eleman silinir
# =============================================================================
    # sol cizgi ortalama
    try:
        if left_lines is not None:
            k.append(left_lines)
            if len(k) == 10:
                left_lines = sum(k)/len(k)
                del k[0]
            zeros = draw_line(zeros, left_lines)
            img_org = cv2.addWeighted(img_org,1,zeros,1,0)
            img_org = draw_line(img_org, left_lines, 3, (0,255,0))
        else:
            left_lines = sum(k)/len(k)
            del k[0]
            zeros = draw_line(zeros, left_lines)
            img_org = cv2.addWeighted(img_org,1,zeros,1,0)
            img_org = draw_line(img_org, left_lines, 3, (0,255,0))
    except:
        pass
# =============================================================================
    # sag cizgi ortalama
    try:
        if right_lines is not None:
            k2.append(right_lines)
            if len(k2) == 10:
                right_lines = sum(k2)/len(k2)
                del k2[0]
            zeros = draw_line(zeros, right_lines)
            img_org = cv2.addWeighted(img_org,1,zeros,1,0)
            img_org = draw_line(img_org, right_lines, 3, (0,255,0))
        else:
            right_lines = sum(k2)/len(k2)
            del k2[0]
            zeros = draw_line(zeros, right_lines)
            img_org = cv2.addWeighted(img_org,1,zeros,1,0)
            img_org = draw_line(img_org, right_lines, 3, (0,255,0))
    except:
        pass
# =============================================================================

    img_org = draw_polylines(img_org, value)
    cv2.imshow("img_org",img_org)
    
    if cv2.waitKey(33) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()