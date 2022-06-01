import subprocess
import os
import requests
import linecache
import re

from MongoDB import database
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu

from kivy.config import Config

bot_token = linecache.getline("credentials", 11)
cluster = re.sub("\n", "",linecache.getline("credentials", 2))
collection = re.sub("\n", "",linecache.getline("credentials", 5))
data = re.sub("\n", "",linecache.getline("credentials", 8))
print(cluster)
print(collection)
print(data)


db = database(cluster, collection, data)
db_id = 0

class HomeScreen(Screen):
    alarm_status = ObjectProperty(None)

    def on_enter(self, *args):
        if alarm_active():
            self.alarm_status.source = "Images/Active.png"
        else:
            self.alarm_status.source = "Images/De-activated.png"

class SettingsScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass



class AlarmApp(MDApp):

    def build(self):
        kv = Builder.load_file(os.path.realpath("my.kv"))
        Window.size = (350, 500)
        return kv




def alarm_active():
    return db.get_element(db_id, "alarm_active")


def send_notify(chatID, bot_message):
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
   requests.get(send_text)


if __name__ == "__main__":
    AlarmApp().run()
