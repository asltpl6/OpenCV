# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 15:24:22 2023

@author: Asli Toplu
"""

import cv2

def main():
    car_cascade = cv2.CascadeClassifier("car/cars.xml")
    cam = cv2.VideoCapture("car/car1.avi")
    
    while cam.isOpened():
        
        ret, frame = cam.read()
        
        if not ret:
            print("done")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        gray = cv2.equalizeHist(gray)
        
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)
        
        for x, y, w, h in cars:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 3)
            frame[y:y+h, x:x+w, 2] = 255
        
        cv2.imshow("frame",frame)
        
        if cv2.waitKey(33) & 0xFF == ord("q"):
            break
        
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    