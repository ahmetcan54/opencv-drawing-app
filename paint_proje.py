# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 14:36:53 2025

@author: ahmetcan
"""

import cv2
import numpy as np

cizim =False
mod = False
xi,yi = -1,-1


def draw(event,x,y,flags,param):
    
    global cizim,xi,yi,mod
    
    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi=x,y
        cizim=True
    elif event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
            if mod:
                cv2.circle(img, (x,y), 2, (255,0,255),-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),(0,255,0),-1)
        else:
            pass
    elif event ==cv2.EVENT_LBUTTONUP:
        cizim =False
    
img = np.ones((512,512,3),np.uint8)

cv2.namedWindow("paint")

cv2.setMouseCallback("paint", draw)


while True:
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod
        
cv2.destroyAllWindows()