from threading import *
import sys
import time
import os
import requests

import numpy as np
import cv2
import telepot
import Camera as camera
import re

from turtle import bgcolor
from types import TracebackType
from datetime import datetime
from MongoDB import database

bot_token = "bot_token"
chatID = "ChatID"
cluster = "cluster"
collection = "collection"
data = "data"

bot = telepot.Bot(bot_token)

db = database(cluster, collection, data)
db_id = 0


def setup():

    db.update_element(db_id, "system_signal", 0)
    send_notify("Startar larmenhet...")
    main_loop()
    camera.video_stream()

old_time = None
def main_loop():
    #print("Running..")
    global old_time

    newThread = Thread(target=main_loop)
    try:
        system_signal = db.get_element(db_id, "system_signal")
        request_cam = db.get_element(db_id, "request_cam")
        scheme_set = db.get_element(db_id, "scheme_set")

    except Exception as e:
        print("Failed fetching start values")

    if(system_signal == 1):

        try:
            db.update_element(db_id, "alarm_on", True)
            db.update_element(db_id, "system_signal", 0)
            send_notify("Alarm aktiverat ✅")

        except Exception as e:
            try:
                send_notify("Misslyckades att aktivera ⭕️")
            except:
                pass
            print("Failed turning on alarm")

        newThread.start()
    
    elif(system_signal == 2):

        try:
            db.update_element(db_id, "alarm_on", False)
            db.update_element(db_id, "system_signal", 0)
            send_notify("Alarm avaktiverat ❎")

        except Exception as e:
            try:
                send_notify("Misslyckades att avaktivera ⭕️")
            except:
                pass
            print("Failed turning off alarm")

        newThread.start()
    
    elif(request_cam != 0):

        try:
            db.update_element(db_id, "request_cam", 0)
            if request_cam == 1:
                send_notify("Skickar bild... 📸")
                camera.take_send_picture()
            elif request_cam == 2:
                send_notify("Skickar 10 sekunders video... 📹")
                camera.record_send_video(10)
            elif request_cam == 3:
                send_notify("Skickar 20 sekunders video... 📹")
                camera.record_send_video(20)

        except Exception as e:
            try:
                send_notify("Misslyckades att skicka ⭕️")
            except:
                pass
            print("Failed to update camera")
        
        newThread.start()
    elif(scheme_set == True):

        try:
            scheme_start = int(re.sub(":", "", db.get_element(db_id, "start_time")))
            scheme_end = int(re.sub(":", "", db.get_element(db_id, "end_time")))
            current_time = int(re.sub(":", "", datetime.now().strftime("%H:%M")))

            if(current_time == scheme_start and old_time != current_time):
                db.update_element(db_id, "alarm_on", True)
                db.update_element(db_id, "action_time", "Aktiverat " + datetime.now().strftime("%H:%M:%S"))
                send_notify("Alarm aktiverat ✅")
            if(current_time == scheme_end and old_time != current_time):
                db.update_element(db_id, "alarm_on", False)
                db.update_element(db_id, "action_time", "Avaktiverat " + datetime.now().strftime("%H:%M:%S"))
                send_notify("Alarm avaktiverat ❎")

            old_time = current_time

        except Exception as e:
            try:
                send_notify("Misslyckades att aktivera/avaktivera ⭕️")
            except:
                pass
            print("Failed scheme")
        
        time.sleep(3)
        newThread.start()
    else:
        time.sleep(3)
        newThread.start()


def motionDetected():
    try:
        send_notify("Rörelse upptäckt ‼️")
    except:
        pass


def send_notify(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(chatID) + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)


def sendPicture():
    bot.sendPhoto(chatID, photo=open("frame.jpg", "rb"))


def sendVideo():
    bot.sendVideo(chatID, video=open("output.avi", "rb"))


if __name__ == "__main__":
    setup()

    try:
        while(True):
            pass
    except KeyboardInterrupt:
        print("Exiting")
    except:
        print("Exiting with exception")
        os._exit(0)
    
