from datetime import datetime
from pynput.keyboard import Key, Controller
import time, os
keyboard = Controller()

browser = "google-chrome"     # replace it with your browser
link = "jcx-sgnp-dra"        # set your link here
meet_time = ("12:14:30")   # set your time here

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
	if now.strftime("%H:%M:%S")  == meet_time:
	    os.system("gnome-terminal -e '"+browser+" http://meet.google.com/"+link+"'")
	    presstabkey(8, 20, Key.tab)
	    break




	
