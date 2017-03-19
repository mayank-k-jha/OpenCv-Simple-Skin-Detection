# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 00:43:20 2017

@author: mayank
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of skin color in HSV
    lower = np.array([0, 10, 60], dtype = "uint8") 
    upper = np.array([20, 150, 255], dtype = "uint8")
    # Threshold the HSV image to get only skin colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
