import subprocess
import os
import requests
import linecache

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
cluster = linecache.getline("credentials", 2)
collection = linecache.getline("credentials", 5)
data = linecache.getline("credentials", 8)

db = database(cluster, collection, data)

class HomeScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class WindowManager(ScreenManager):
    enter_name_screen = ObjectProperty(None)
    connect_screen = ObjectProperty(None)
    home_screen = ObjectProperty(None)



class AlarmApp(MDApp):

    def build(self):
        kv = Builder.load_file(os.path.realpath("my.kv"))
        Window.size = (350, 500)
        return kv




def getMachineID():     #Returns unique ID of machine
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    return current_machine_id


def send_notify(chatID, bot_message):
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chatID + '&parse_mode=Markdown&text=' + bot_message
   requests.get(send_text)


if __name__ == "__main__":
    AlarmApp().run()
