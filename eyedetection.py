import cv2
import datetime
import time
import tkinter.messagebox
import notify2

video = cv2.VideoCapture(0)
faceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
idle_time = datetime.timedelta(seconds=0);
notify2.init("Rest Notification")
notification = notify2.notification(None)

while True:
    ImageRead, image = video.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(image, (fx, fy), (fx+fw, fy+fh), (0,255,0))
    cv2.imshow('detection', image)
    time.sleep(10)
    if len(faces) == 0:
        idle_time += datetime.timedelta(seconds=10)
    else:
        idle_time = datetime.timedelta(seconds=0)
    print(idle_time.seconds)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # if idle_time.seconds>20:
    #     #do not ever do os command. VERY DANGEROUS!!!
    #     print('Computer should have an burn in preservation system here')
    if idle_time.seconds>10:
        notification.update("Reminder", "Remember to rest your eyes. It\'s been "+idle_time.minutes+" minutes since you started working.")
