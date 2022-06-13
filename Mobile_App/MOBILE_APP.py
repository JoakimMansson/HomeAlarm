import subprocess
import os
import requests
import linecache
import re

from datetime import datetime

from kivymd.uix.picker import MDTimePicker

from MongoDB import database
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config


from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

bot_token = re.sub("\n", "", linecache.getline("credentials", 11))
chatID = re.sub("\n", "", linecache.getline("credentials", 14))

cluster = re.sub("\n", "", linecache.getline("credentials", 2))
collection = re.sub("\n", "", linecache.getline("credentials", 5))
data = re.sub("\n", "", linecache.getline("credentials", 8))



db = database(cluster, collection, data)
db_id = 0


#   StartScreen used for
#   loading all components
#   for one frame
class StartScreen(Screen):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.start(), 1/30)

    def start(self):
        self.manager.current = "Home"


class HomeScreen(Screen):
    alarm_status = ObjectProperty(None)
    alarm_btn = ObjectProperty(None)
    camera_btn = ObjectProperty(None)
    scheme_btn = ObjectProperty(None)
    last_armed = ObjectProperty(None)


    def on_pre_enter(self, *args):
        try:
            self.last_armed.text = last_armed()

            if alarm_active():
                self.alarm_status.source = "Images/Active.png"
                self.alarm_btn.text = "Avaktivera larm"
                self.camera_btn.disabled = False
            else:
                self.alarm_status.source = "Images/De-activated.png"
                self.alarm_btn.text = "Aktivera larm"
                self.camera_btn.disabled = True

        except Exception as e:
            print(e)

    def alarm_action(self) -> None:
        toast("Laddar")
        if alarm_active():
            self.deactivate_alarm()
        else:
            self.activate_alarm()

    def activate_alarm(self) -> None:
        current_time = datetime.now().strftime("%H:%M:%S")

        try:
            db.update_element(db_id, "system_signal", 1)
            db.update_element(db_id, "action_time", "Aktiverat " + current_time)

            self.alarm_status.source = "Images/Active.png"
            self.alarm_btn.text = "Avaktivera larm"
            self.camera_btn.disabled = False
            self.last_armed.text = "Aktiverat " + current_time

            send_notify("Alarmet har aktiverats")
            toast("Aktiverat")
        except Exception as e:
            print(e)

        Clock.schedule_once(lambda dt: self.check_alarm(1), 5)


    def deactivate_alarm(self) -> None:
        current_time = datetime.now().strftime("%H:%M:%S")

        try:
            db.update_element(db_id, "system_signal", 2)
            db.update_element(db_id, "action_time", "Avaktiverat " + current_time)

            self.alarm_status.source = "Images/De-activated.png"
            self.alarm_btn.text = "Aktivera larm"
            self.camera_btn.disabled = True
            self.last_armed.text = "Avaktiverat " + current_time

            send_notify("Alarmet har avaktiverats")
            toast("Avaktiverat")
        except Exception as e:
            print(e)

        Clock.schedule_once(lambda dt: self.check_alarm(2), 5)


    def check_alarm(self, expectedState: int):
        current_time = datetime.now().strftime("%H:%M:%S")
        
        if expectedState == 1 and db.get_element(db_id, "alarm_on") == False:
            toast("Misslyckades")
            self.alarm_status.source = "Images/De-activated.png"
            self.alarm_btn.text = "Aktivera larm"
            self.camera_btn.disabled = True
            self.last_armed.text = "Misslyckades " + current_time
            db.update_element(db_id, "action_time", self.last_armed.text)
        elif expectedState == 2 and db.get_element(db_id, "alarm_on") == True:
            toast("Misslyckades")
            self.alarm_status.source = "Images/Active.png"
            self.alarm_btn.text = "Avaktivera larm"
            self.camera_btn.disabled = False
            self.last_armed.text = "Misslyckades " + current_time
            db.update_element(db_id, "action_time", self.last_armed.text)
        else:
            pass


    def go_settings(self):
        self.manager.current = "Settings"

    def go_home(self):
        self.manager.current = "Home"


class SettingsScreen(Screen):

    def RestartAlarmModule(self):
        pass


class CameraScreen(Screen):

    #Sends 1 to database for picture
    def RequestPicture(self):
        try:
            db.update_element(db_id, "request_cam", 1)
            toast("Skickar bild")
        except Exception as e:
            print("Failed to request picture")

    #Sends 2 to database for 10-second video
    def Request10Video(self):
        try:
            db.update_element(db_id, "request_cam", 2)
            toast("Skickar video")
        except Exception as e:
            print("Failed to request 10 video")

    #Sends 3 to database for 20-second video
    def Request20Video(self):
        try:
            db.update_element(db_id, "request_cam", 3)
            toast("Skickar video")
        except Exception as e:
            print("Failed to request 20 video")


class SchemeScreen(Screen):
    start_time = ObjectProperty(None)
    end_time = ObjectProperty(None)

    def on_pre_enter(self, *args):
        self.start_time.text = db.get_element(db_id, "start_time")
        self.end_time.text = db.get_element(db_id, "end_time")

    def pick_time_start(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_start)
        time_dialog.open()

    def pick_time_end(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time_end)
        time_dialog.open()

    def get_time_start(self, instance, time):
        self.start_time.text = str(time)[0:5]

    def get_time_end(self, instance, time):
        self.end_time.text = str(time)[0:5]

    def save_time_scheme(self):
        toast("Sparat")
        send_notify("Schemaläggning från: " + self.start_time.text + " till " + self.end_time.text + " sparad")
        db.update_element(db_id, "start_time", self.start_time.text)
        db.update_element(db_id, "end_time", self.end_time.text)

    def delete_time_scheme(self):
        send_notify("Schemaläggningen från: " + self.start_time.text + " till " + self.end_time.text + " har tagits bort")
        db.update_element(db_id, "start_time", "--:--")
        db.update_element(db_id, "end_time", "--:--")
        self.start_time.text = "--:--"
        self.end_time.text = "--:--"


class WindowManager(ScreenManager):
    Home = HomeScreen()
    Settings = SettingsScreen()



class AlarmApp(MDApp):

    def build(self):
        kv = Builder.load_file(os.path.realpath("my.kv"))
        Window.size = (350, 500)
        return kv



def alarm_active():
    alarm_status = db.get_element(db_id, "alarm_on")
    return alarm_status


def last_armed():
    armed_time = db.get_element(db_id, "action_time")
    return armed_time


def send_notify(bot_message):
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
   requests.get(send_text)


if __name__ == "__main__":
    AlarmApp().run()
