# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 20:01:14 2017

@author: mayank
"""


import matplotlib.pyplot as plt
import cv2
import numpy as np

lower = np.array([0, 10, 60], dtype = "uint8")
upper = np.array([20, 150, 255], dtype = "uint8")


try:
    
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'DIVX')
    output=cv2.VideoWriter('D:/Development/Python Dev/capture1.mp4',fourcc,1.0,(640,480),True)
       
    while(True):
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask=cv2.inRange(hsv,lower,upper)
        hsv=cv2.bitwise_and(frame,frame,mask=mask)
        output.write(hsv)
        cv2.resizeWindow('Cam',640,460)
        cv2.imshow('Cam',frame)
        if cv2.waitKey(1)==ord('q'):
            break
       
    cap.release()
    output.release()
    cv2.destroyAllWindows()
    cap=cv2.VideoCapture('D:/Development/Python Dev/capture1.mp4')
    while(cap.isOpened()):
        ret,f=cap.read()
        cv2.resizeWindow('Cam',640,460)
        cv2.imshow('Cam',f)
        if cv2.waitKey(1)==ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()        
except:
    cap.release()
    output.release()
    cv2.destroyAllWindows() 
       
