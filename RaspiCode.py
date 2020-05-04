#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:19:00 2020
@author: btknzn
"""
#You Have 22 selections, Just blink in 10 seconds and select the food you want to eat
#Our system counts your blink number from your first blick to 10 seconds later
import numpy as np
import cv2
import dlib
from math import hypot
import time
from picamera.array import PiRGBArray
from picamera import PiCamera


def System():
    situation = True
    starttime=0
    eyeControlvalue=0
    lastvalueofeyecontrol=0
    counter=0
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    while(True):
        time.sleep(0.1)
        camera.capture(rawCapture, format="bgr")
        frame = rawCapture.array       
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        faces = detector(gray)
        lastvalueofeyecontrol = eyeControlvalue
        eyeControlvalue = eyeControl(gray, faces,frame)
        cv2.putText(frame,str(counter)+'blink number ',(0,400),font,1,(0,0,255),1)
        cv2.putText(frame,'Do you want '+systemTupel[counter]+'?',(50,50),font,1,(255,0,0),1)
        if eyeControlvalue == 1:
            cv2.putText(frame,"Blinking",(50,150),font,1,(0,0,255),1)
            if situation:
                situation = False
                starttime=time.time()

       
        if eyeControlvalue == 0:
            cv2.putText(frame,"not Blinking",(50,150),font,1,(0,0,255),1)
         
            
        if eyeControlvalue == None:
            cv2.putText(frame,'no eye contact',(50,150),font,1,(0,0,255),1)
       
        
        if situation:
            cv2.putText(frame,'To start system just blink. You Have 10 second to make selecton:) ',(50,250),font,1,(0,0,255),1) 

    
        cv2.putText(frame,'To stop system press q ',(225,350),font,1,(0,0,255),1)
        
        
        if (eyeControlvalue==1) and (lastvalueofeyecontrol==0):
            counter= counter +1
            
        if ((starttime+10)<time.time()):
            if(situation==False):
                situation = True
                counter = 0
        
        
        cv2.imshow('frame',frame)

            
        if (time.time()>starttime+10):
            situation = True
            
            
    cap.release()
    cv2.destroyAllWindows()    
    
    
def changeSituation(situation,starttimesecond):
    timenow = time.time()
    starttimeplustensecond = starttimesecond+10
    if  timenow > starttimeplustensecond: 
        situation = not situation



def eyeControl(gray, faces,frame):
    for face in faces:
        features = predictor(gray,face)
        
        R_Hori_left_x = features.part(36).x
        R_Hori_left_y = features.part(36).y
        R_Hori_left = (R_Hori_left_x,R_Hori_left_y)
        R_Hori_right_x = features.part(39).x
        R_Hori_right_y = features.part(39).y
        R_Hori_right = (R_Hori_right_x,R_Hori_right_y)
        cv2.line(frame,R_Hori_left,R_Hori_right,(0,255,0),1)
        R_upper_mid_x = int((features.part(37).x + features.part(38).x)/2)
        R_upper_mid_y = int((features.part(37).y + features.part(38).y)/2)
        R_upper_mid = (R_upper_mid_x,R_upper_mid_y)
        R_bottom_mid_x = int((features.part(41).x + features.part(40).x)/2)
        R_bottom_mid_y = int((features.part(41).y + features.part(40).y)/2)
        R_bottom_mid = (R_bottom_mid_x,R_bottom_mid_y)
        cv2.line(frame,R_upper_mid,R_bottom_mid,(0,255,0),1)
   #    find the lenght for both horizontal and vertical line
        R_hori_lenght = hypot(R_Hori_left_x - R_Hori_right_x, R_Hori_left_y - R_Hori_right_y)
        R_ver_lenght = hypot(R_upper_mid[0] - R_bottom_mid[0], R_upper_mid[1] - R_bottom_mid[1])
        features = predictor(gray,face)
        L_Hori_left_x = features.part(42).x
        L_Hori_left_y = features.part(42).y
        L_Hori_left = (L_Hori_left_x,L_Hori_left_y)
        L_Hori_right_x = features.part(45).x
        L_Hori_right_y = features.part(45).y
        L_Hori_right = (L_Hori_right_x,L_Hori_right_y)
        cv2.line(frame,L_Hori_left,L_Hori_right,(0,255,0),1)
        L_upper_mid_x = int((features.part(43).x + features.part(44).x)/2)
        L_upper_mid_y = int((features.part(43).y + features.part(44).y)/2)
        L_upper_mid = (L_upper_mid_x,L_upper_mid_y)
        L_bottom_mid_x = int((features.part(47).x + features.part(46).x)/2)
        L_bottom_mid_y = int((features.part(47).y + features.part(46).y)/2)
        L_bottom_mid = (L_bottom_mid_x,L_bottom_mid_y)
        cv2.line(frame,L_upper_mid,L_bottom_mid,(0,255,0),1)
        L_hori_lenght = hypot(L_Hori_left_x-L_Hori_right_x,L_Hori_left_y-L_Hori_right_y)
        L_ver_lenght = hypot(L_upper_mid[0]-L_bottom_mid[0],L_upper_mid[1]-L_bottom_mid[1])
        L_ratio = L_hori_lenght/(L_ver_lenght+0.000000001)
        R_ratio = R_hori_lenght/(R_ver_lenght+0.000000001)
        ratio = (L_ratio + R_ratio)/2
        if ratio > 5:
            return 1
        return 0


cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
systemTupel = ("Pear","Quince","Apple","Plum","Cocount","Fig","Banana","Watermelon","Melon","Apricot","Cherry","Kiwi","Meat","Poultry","Fish","Seafood","Waffle","Ham","Bread","Creal","Orange Juice" , "Muffin")
font = cv2.FONT_HERSHEY_COMPLEX
System()

