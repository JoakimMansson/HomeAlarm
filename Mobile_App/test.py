import linecache
import os
import re
import telepot
from datetime import datetime
import re
import threading

current_time = int(re.sub(":", "", datetime.now().strftime("%H:%M")))
os.remove('testing.py')
threading.Timer(5.0)

def sayHello():
    print("Hello")