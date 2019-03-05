# -*- coding: utf-8 -*-
"""
Created on Tue Mar 05 16:08:53 2019

@author: Trevor
"""

import numpy as np
import cv2
import datetime
import os

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('C:/ProgramData/Anaconda3/Library/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0) #url for ipcam streaming/video('http://192.168.0.103:8080/video')

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
       # Image Naming #

        sysTime = datetime.datetime.now()
        deviceTime=sysTime.strftime("%d_%m_%Y_%H_%M_%S_%f")
        imageName = "Cam1"+deviceTime+".png"
        
        #  Image block complete #
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(57,255,20),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        sub_face = img[y:y+h, x:x+w]
        #cv2.imwrite(imageName,img)
        cv2.imwrite(os.path.join(path , imageName), sub_face)
       

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
