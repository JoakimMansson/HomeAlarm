from turtle import bgcolor
from xml.dom.minidom import parseString
import cv2
from cv2 import cvtColor
import numpy
import Main as alarm
import time
import os
from MongoDB import database



video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
isRecording = False

def video_stream():
    global isRecording

    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml") #Pre-trained classifier
    while True:
        ret, frame = video.read()
        if not ret:
            pass
        else:
            if(alarm.db.get_element(alarm.db_id, "alarm_on") == True):
                gray_scale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_scale_img = cv2.equalizeHist(gray_scale_img)
                bodies = body_cascade.detectMultiScale(gray_scale_img, 1.25, 5)
                #print("Checking")
            
                for (x, y, w, h) in bodies:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.imwrite("frame.jpg", frame)
                    alarm.motionDetected()
                    alarm.sendPicture()
                    record_send_video(30)
                    


def take_send_picture():
    os.remove("frame.jpg")
    ret, frame = video.read()
    if not ret:
        pass
    else:
        cv2.imwrite("frame.jpg", frame)
        alarm.sendPicture()

def record_send_video(capture_duration: int):
    global isRecording
    if isRecording:
        pass
    else:
        isRecording = True
        os.remove("output.avi")
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
        start_time = time.time()
        while(int(time.time() - start_time) < capture_duration):
            ret, frame = video.read()
            if ret == True:
                #frame = cv2.flip(frame,0)
                out.write(frame)
            else:
                print("FAILED CAPTURING")
                #break
        alarm.sendVideo()
        isRecording = False

