
from datetime import datetime
from pynput.keyboard import Key, Controller
import time, os
import webbrowser
keyboard = Controller()

link = "ttd-hnxt-iyi"         #set the link here
meet_time = ("12:26:00")      #set the time here

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
	if now.strftime("%H:%M:%S") == meet_time:
	    webbrowser.open("http://meet.google.com/"+link)
	    presstabkey(8, 8, Key.tab)
	    break
