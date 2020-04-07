#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)
time.sleep(2)
frame1=0
for i in range(30):
    ret,frame1=cap.read()
    
while cap.isOpened:
    ret,frame2=cap.read()
    if ret==False:
        break
    hsv=cv2.cvtColor(frame2,cv2.COLOR_BGR2HSV)
    l_r=np.array([0,120,70])
    u_r=np.array([10,255,255])
    m1=cv2.inRange(hsv,l_r,u_r)
    
    l_r=np.array([170,120,70])
    u_r=np.array([180,255,255])
    m2=cv2.inRange(hsv,l_r,u_r)
    m1=m1 + m2
    
    kernal=np.ones((2,2),np.uint8)
    m1=cv2.morphologyEx(m1,cv2.MORPH_OPEN,kernal,2)
    m1=cv2.morphologyEx(m1,cv2.MORPH_DILATE,kernal,2)
    
    m2=cv2.bitwise_not(m1)
    r1=cv2.bitwise_and(frame1,frame1,mask=m1)
    r2=cv2.bitwise_and(frame2,frame2,mask=m2)
    result=cv2.addWeighted(r1,1,r2,1,0)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(result,'MY MAGIC',(10,50),font,1,(0,255,255))
    
    cv2.imshow('MY MAGIC',result)
    k=cv2.waitKey(10)
    if k== ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows() 

