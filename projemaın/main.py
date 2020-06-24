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

def System():
    situation = True
    starttime=0
    eyeControlvalue=0
    lastvalueofeyecontrol=0
    counter=0
    while(True):
        time.sleep(0.01)
        ret, frame = cap.read()       
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Display the resulting frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        faces = detector(gray)
        lastvalueofeyecontrol = eyeControlvalue
    
        eyeControlvalue = eyeControl(gray, faces,frame)  
        #print(str(counter)+'  blink number')
        #print('Do you want '+systemTupel[counter]+'?')
        if eyeControlvalue == 1:
            if situation:
                situation = False
                starttime=time.time()
       
        
        if situation:
            cv2.putText(frame,'Sistemi Baslatmak icin Goz kirin 10 saniye içinde göz kirparak isteğinizi belirtin ',(0,150),font,0.1,(0,0,255),1)
            #print('Sistemi başlatmak için Bir kere Göz kırpın') 

        
        if (eyeControlvalue==1) and (lastvalueofeyecontrol==0):
            counter= counter +1
            print("Göz kırpma sayısı "+ str(counter))
            
        cv2.putText(frame,"Goz Kirpma Sayisi: "+ str(counter),(0,200),font,0.5,(0,0,255),1)    
        if ((starttime+10)<time.time()):
            if(situation==False):
                situation = True
                if (counter == 1):
                    im = cv2.imread('elma.jpg')
                if (counter == 2):
                    im = cv2.imread('armut.jpg')
                if (counter == 3):
                    im = cv2.imread('çilek.jpg') 
                if (counter == 4):
                    im = cv2.imread('muz.jpg') 
                if (counter == 5):
                    im = cv2.imread('ananas.jpg')
                if (counter == 6):
                    im = cv2.imread('nar.jpg') 
                if (counter == 7):
                    im = cv2.imread('uzum.jpg')
                if (counter == 8):
                    im = cv2.imread('seftali.jpg')
                if (counter == 9):
                    im = cv2.imread('kayısı.jpg')
                if (counter == 10):
                    im = cv2.imread('kiraz.jpg') 
                
                print('Sizin isteğiniz budur  '+systemTupel[counter] )
                im = cv2.resize(im,(320,256))
                cv2.imshow('Your selection',im)
                cv2.waitKey(2000)
                cv2.destroyAllWindows()
                counter = 0
                
                
        if (time.time()>starttime+10):
            situation = True
        cv2.imshow('frame',frame)
        
            
                
    cap.release() 
    


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
cap.set(3,320)
cap.set(4,256)
systemTupel = ("","Elma","Armut","Çilek","muz","ananas","nar","üzüm","şeftali","kayısı","","","","","","","","","","","")
font = cv2.FONT_HERSHEY_COMPLEX
System()