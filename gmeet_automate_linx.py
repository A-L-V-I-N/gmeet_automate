from datetime import datetime
from pynput.keyboard import Key, Controller
import time, os
keyboard = Controller()

browser = "google-chrome"
link = "jcx-sgnp-dra"
current_time = ("12:14:30")

def presstabkey(num, tym, keys):
	
	time.sleep(tym)
	while num > 0 :
		keyboard.press(keys)
		keyboard.release(keys)
		num = num-1
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

while True:
	now = datetime.now()
	if now.strftime("%H:%M:%S")  == current_time:
	    os.system("gnome-terminal -e '"+browser+" http://meet.google.com/"+link+"'")
	    presstabkey(8, 20, Key.tab)
	    break




	
