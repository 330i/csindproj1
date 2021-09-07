import cv2
import datetime
import time
import notify2
import sys
import pyautogui

video = cv2.VideoCapture(0)
faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
leyeClassifier = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
reyeClassifier = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

while True:
    ImageRead, image = video.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    for (fx, fy, fw, fh) in faces:
        leftEye = leyeClassifier.detectMultiScale(gray[fy:fy+fh, fx:fx+fw], 1.3, 5)
        rightEye = reyeClassifier.detectMultiScale(gray[fy:fy+fh, fx:fx+fw], 1.3, 5)
        cv2.rectangle(image[fy:fy+fh, fx:fx+fw], (fx, fy), (fx+fw, fy+fh), (0,255,0))
        for (lex, ley, lew, leh) in leftEye:
            cv2.rectangle(image, (fx+lex, fy+ley), (fx+lex+lew, fy+ley+leh), (0,255,0))
            print(lex+" from left "+ley+" from top ")
        for (rex, rey, rew, reh) in rightEye:
            cv2.rectangle(image, (fx+rex, fy+rey), (fx+rex+rew, fy+rey+reh), (0,255,0))
            print((fx-rex)+" from right "+rey+" from top ")
        
    cv2.imshow('detection', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # if idle_time.seconds>20:
    #     #do not ever do os command. VERY DANGEROUS!!!
    #     print('Computer should have an burn in preservation system here')
