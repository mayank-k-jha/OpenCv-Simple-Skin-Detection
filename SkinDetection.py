# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:48:31 2017

@author: mayank
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
lower = np.array([0, 10, 60], dtype = "uint8")
upper = np.array([20, 150, 255], dtype = "uint8")
while(True):
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(frame,lower,upper)
    cv2.resizeWindow('cam',640,320)
    cv2.imshow('cam',mask)
    if cv2.waitKey(1)==ord('q') :
        break;
        
cap.release()        
cv2.destroyAllWindows()    
